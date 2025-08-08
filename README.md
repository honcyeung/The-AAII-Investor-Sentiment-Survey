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

Step 1: Configure the Notification Service (Pipeline Steps 4-6)
This first step sets up the receiving end of the pipeline in IFTTT. You will create an Applet that listens for incoming data from Pipedream (Step 4), triggers a Telegram action (Step 5), and delivers the final message to your chat (Step 6).

Create a new Applet in your IFTTT account.

For the If This condition, select the Webhooks service and choose the Receive a web request with a JSON payload trigger.

Define an Event Name (e.g., aaii_sentiment_update) and create the trigger.

For the Then That action, select the Telegram service.

Choose the Send message action. Connect your Telegram account if prompted.

In the Message text field, use the {{value1}} ingredient. This corresponds to the formatted message sent from the Python script.

Select the target chat for notifications and finish the applet.

Navigate to the Webhooks service page and click Documentation. Copy your unique key from the URL provided. This key is required for Pipedream to authorize its requests.

Step 2: Deploy the Data Processing Workflow (Pipeline Steps 1-3)
This second step configures the Pipedream workflow, which handles the start of the pipeline. The workflow initiates on a schedule (Step 1), executes the Python script to fetch and format the sentiment data (Step 2), and sends that data to the IFTTT webhook you just created (Step 3).

Create a new Workflow in your Pipedream account.

Select Schedule as the trigger and configure your desired interval (e.g., weekly).

Add a Run Python Code step.

Paste the code from the pipedream_code.py file into the editor.

In the Python step, create an Environment Variable.

Set the name to IFTTT_AAII_SENTIMENT_KEY and paste your IFTTT key from Step 1.8 as the value.

Ensure the event_name variable in the Python script matches the event name from Step 1.3.

Deploy and enable the workflow.

The automation is now live and will execute based on the defined schedule.
