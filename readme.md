# LLM-Ready Retrieval Demo | GitHub Auto Deployment with Render

A end-to-end project built using **Python**, **Flask**, **GitHub**, and **Render** to demonstrate:

- LLM-ready retrieval style data modeling
- common-key based integrated view across sample enterprise datasets
- lightweight search over SAP FICO-style records
- automatic deployment from GitHub to Render

## Live Demo
Add your Render URL here:

`https://llm-retrieval-render-demo.onrender.com`

## Project Summary

This project is a  prototype created to show how retrieval-oriented data modeling can be combined with Git-based deployment automation.

The application uses sample SAP FICO-style data and models it as searchable chunks with a shared **common key**. A simple retrieval flow scores matching records for a user query and returns the most relevant results.

The same project is connected from **GitHub to Render**, so every time code is pushed to the `main` branch, Render automatically rebuilds and redeploys the application.

## Why I Built This

I built this project to demonstrate practical understanding of:

- LLM-ready data preparation
- retrieval-friendly chunk design
- common key integration across separated datasets
- lightweight search and ranking
- GitHub to Render deployment automation

## Tech Stack

- Python
- Flask
- Gunicorn
- GitHub
- Render

## Project Features

- Home page with project overview
- Health endpoint
- Records endpoint
- Search endpoint
- Automatic deployment through GitHub + Render
- Version-based redeployment testing

## Endpoints

### Home
`/`

Shows the project overview and current version.

### Health
`/health`

Returns service status and version.

### Records
`/records`

Returns the sample enterprise data records used in the demo.

### Search
`/search?q=vendor invoice payment`

Performs lightweight retrieval against the sample records and returns the top matches.

## Example Use Case

A user can search for finance-related phrases such as:

`vendor invoice payment`

The application checks the sample chunks, scores the matches, and returns the most relevant records using simple similarity logic.

This demonstrates the idea of retrieval-oriented modeling in a very lightweight way.

## Automatic Deployment Flow

This project is connected to GitHub and deployed on Render.

Deployment flow:

1. Update code locally or in Google Colab
2. Commit and push changes to GitHub
3. Render detects the new commit on the linked branch
4. Render rebuilds the application
5. Render redeploys the latest version automatically

## Deployment Configuration

### Build Command
```bash
pip install -r requirements.txt
