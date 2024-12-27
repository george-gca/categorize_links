[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fgeorge-gca%2Fcategorize_links&demo-title=Categorize%20Links&demo-description=Web%20app%20to%20help%20split%20links.&demo-url=https%3A%2F%2Fcategorizelinks.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)

# Categorize Links

This is a simple tool to categorize links. Paste your links in the left box and click on the "Categorize" button. The links will be split into 2 types: research links and other links. Research links are basically the links that you want to read or use for research. Other links are the remaining links. To get the current open links in my browser session I like to use the [Session Buddy](https://sessionbuddy.com/) extension.

## Site

https://categorizelinks.vercel.app/

## How it Works

This project uses the Web Server Gateway Interface (WSGI) with Flask to enable handling requests on Vercel with Serverless Functions.

## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.

## One-Click Deploy

Deploy this project using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fgeorge-gca%2Fcategorize_links&demo-title=Categorize%20Links&demo-description=Web%20app%20to%20help%20split%20links.&demo-url=https%3A%2F%2Fcategorizelinks.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)