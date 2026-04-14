# github-actions-ai-log-analysis

## The Problem

When a GitHub Actions workflow fails, the logs are already trying to tell you what went wrong.
This just helps them get to the point faster.

## Let’s tie in an AI (or two) and do some log analysis

By the end of this guide, you will have:

* a GitHub Actions workflow that fails in a controlled way
* a job that captures the failure log
* a connection to OpenAI or Anthropic
* a short AI-generated explanation of the error (and potential fixes) returned directly to the GitHub Actions console# github-actions-ai-log-analysis

## Before You Run This

This repo is a simple proof of concept for sending a failed GitHub Actions workflow log to an AI provider and returning a short failure analysis directly in the workflow output.

To run it yourself, you will need:

* a GitHub account
* a GitHub repository with Actions enabled
* an OpenAI API key (or Anthropic key if you add that workflow later)

### Important

This repo does not include any API keys.

You will need to create and use your own key.

To add your key:

Go to your repository
Click **Settings**
Click **Secrets and variables → Actions**
Add a new repository secret named:
```
OPENAI_API_KEY
```

Then paste your API key value.