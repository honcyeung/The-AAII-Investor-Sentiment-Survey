# AAII Sentiment Telegram Notifier
A serverless automation that scrapes the weekly AAII Investor Sentiment Survey data and delivers it as a formatted message to a Telegram chat.

## Overview
This repository contains the code for a fully automated workflow that tracks the weekly sentiment of individual investors. The process is entirely serverless, leveraging Pipedream for scheduled code execution and IFTTT for notifications.
The core of the project is a Python script that runs on a weekly schedule, scrapes the data from the AAII website, and then sends it to a custom IFTTT webhook. IFTTT, in turn, forwards the data to a designated Telegram chat, providing a timely and hands-off sentiment update.

## Pipeline Diagram
```text
+--------------------------------------+
| [Pipedream] 1. Weekly Trigger        |
+--------------------------------------+
                  |
                  v
+--------------------------------------+
| [Pipedream] 2. Execute Python Script |
|     (Scrapes & formats data)         |
+--------------------------------------+
                  |
                  v
+--------------------------------------+
| [Pipedream] 3. POST to IFTTT Webhook |
|     (Sends formatted payload)        |
+--------------------------------------+
                  |
                  v
+--------------------------------------+
| [IFTTT] 4. Applet Triggered          |
|     (Receives JSON payload)          |
+--------------------------------------+
                  |
                  v
+--------------------------------------+
| [IFTTT] 5. Telegram Action Executed  |
|     (Formats and sends message)      |
+--------------------------------------+
                  |
                  v
+--------------------------------------+
| [Telegram] 6. Message Delivered      |
+--------------------------------------+
```

## Setup & Configuration
To deploy this automation, follow the steps below to build the data pipeline shown in the diagram.

Prerequisites
- Pipedream Account
- IFTTT Account
- Telegram Account

Deploy on Pipedream (Steps 1-3): It involves setting up a Pipedream workflow. This workflow starts with a scheduler that triggers the process weekly. The trigger runs the provided Python script, which fetches the latest sentiment data from the AAII website and formats it. Finally, the script sends this data to the IFTTT webhook URL you created in the first step, completing the connection between the two services and activating the full pipeline.

Configure IFTTT (Steps 4-6): It involves creating an IFTTT Applet. This Applet acts as the receiver. It generates a unique webhook URL that listens for incoming data. When data arrives, the Applet is configured to automatically trigger the Telegram service, which then sends a pre-formatted message to the specified chat. This handles the entire notification end of the pipeline.
