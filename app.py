from flask import Flask, request, jsonify
import math

app = Flask(__name__)

VERSION = "v1"

# Tiny SAP FICO-style sample data
records = [
    {
        "common_key": "INV-1001",
        "source": "sap_fico",
        "chunk": "Vendor invoice posted for office supplies payment due in 30 days cost center finance"
    },
    {
        "common_key": "INV-1002",
        "source": "sap_fico",
        "chunk": "Customer payment received and cleared against receivables document reference banking entry"
    },
    {
        "common_key": "PO-2001",
        "source": "procurement",
        "chunk": "Purchase order created for laptop accessories mapped to vendor and finance approval"
    },
    {
        "common_key": "GL-3001",
        "source": "general_ledger",
        "chunk": "General ledger posting for travel reimbursement employee expense accounting entry"
    },
    {
        "common_key": "AP-4001",
        "source": "accounts_payable",
        "chunk": "Accounts payable aging record for vendor invoice overdue payment reminder"
    }
]

def tokenize(text):
    return text.lower().split()

def vectorize(text):
    vec = {}
    for word in tokenize(text):
        vec[word] = vec.get(word, 0) + 1
    return vec

def cosine_similarity(v1, v2):
    dot = 0
    for k in v1:
        dot += v1.get(k, 0) * v2.get(k, 0)

    norm1 = math.sqrt(sum(x * x for x in v1.values()))
    norm2 = math.sqrt(sum(x * x for x in v2.values()))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return round(dot / (norm1 * norm2), 4)

@app.route("/")
def home():
    return f"""
    <h1>Mini LLM Ready Retrieval Demo</h1>
    <p><b>Version:</b> {VERSION}</p>
    <p>This is a tiny GitHub → Render auto deployment project.</p>
    <p><b>Purpose:</b> show common-key data modeling, chunked records, and lightweight retrieval.</p>
    <p>Try:</p>
    <ul>
        <li><a href="/health">/health</a></li>
        <li><a href="/records">/records</a></li>
        <li><a href="/search?q=vendor invoice payment">/search?q=vendor invoice payment</a></li>
    </ul>
    <p>Change VERSION to v2, push to GitHub, and Render should redeploy automatically.</p>
    """

@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": VERSION})

@app.route("/records")
def get_records():
    return jsonify(records)

@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    if not query:
        return jsonify({"error": "Pass query like /search?q=vendor invoice"}), 400

    query_vec = vectorize(query)
    scored = []

    for r in records:
        score = cosine_similarity(query_vec, vectorize(r["chunk"]))
        scored.append({
            "common_key": r["common_key"],
            "source": r["source"],
            "chunk": r["chunk"],
            "score": score
        })

    scored = sorted(scored, key=lambda x: x["score"], reverse=True)
    return jsonify({
        "version": VERSION,
        "query": query,
        "results": scored[:3]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)