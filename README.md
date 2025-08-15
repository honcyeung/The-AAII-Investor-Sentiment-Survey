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

Pipedream (Steps 1-3): 
1. Starts with a scheduler that triggers the process weekly.
2. The trigger runs the provided Python script, which fetches the latest sentiment data from the AAII website and formats it.
3. The script sends this data to the IFTTT webhook URL.

IFTTT (Steps 4-6): 
1. The Applet acts as the receiver of data from Pipedream.
2. When data arrives, the Applet automatically triggers the Telegram service.
3. It sends a pre-formatted message to the specified Telegram channel.
