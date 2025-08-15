import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime
  
def web_scraping():
    url = "https://www.aaii.com/sentimentsurvey"
    
    # Fetch the webpage
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    # Parse HTML and extract the value
    soup = BeautifulSoup(response.text, "html.parser")
    weekending_divs = soup.find_all('div', class_ = 'weekending')
    
    # Extract the text content and process it
    sentiment_list = [div.get_text(strip = True) for div in weekending_divs]

    # Get the date string first; dates may have different length, eg 3/12/2025, 3/5/2025
    sentiment_data = sentiment_list[1].split("/")
    date_str = sentiment_data[0] + "/" + sentiment_data[1] + "/" + sentiment_data[2][:4]

    sentiment_list2 = [i for i in sentiment_data[2][4:].split("%") if i]
    date_obj = datetime.strptime(date_str, "%m/%d/%Y").strftime("%d %b %Y")
    sentiment_list3 = [date_obj] + sentiment_list2
    d = {k:v for k, v in zip(["Week Ending", "Bullish", "Neutral", "Bearish"], sentiment_list3)}
    
    return d

def send_message_to_ifttt(sentiment_data):

    # Format the message
    message = (
        f"Week Ending\n{sentiment_data['Week Ending']}\n\n"
        f"Bullish: {sentiment_data['Bullish']}%\n"
        f"Neutral: {sentiment_data['Neutral']}%\n"
        f"Bearish: {sentiment_data['Bearish']}%"
    )
    
    # IFTTT webhook configuration
    ifttt_key = os.environ["IFTTT_AAII_SENTIMENT_KEY"]
    ifttt_webhook_url = f"https://maker.ifttt.com/trigger/AAII_sentiment/json/with/key/{ifttt_key}"
    
    payload = {
        "value1": message
    }
    
    # Send request to IFTTT
    response = requests.post(ifttt_webhook_url, json = payload)
    response.raise_for_status()

    try:
        sentiment_data = web_scraping()
    except Exception as e:
        raise Exception(f"Failed to run: {e}")