import http.client
import json
import datetime
import csv

#set perplexity API details
API_HOST = "api.perplexity.ai"
API_ENDPOINT = "/chat/completions"
API_KEY = "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"

#7 prompts
prompts = {
    "Market_Direction_Prediction": "Today is the #TODAY#. Pretend to be a financial expert. Predict the S&P 500's direction for the next day. "
                                    "Provide output in CSV format:\nPrediction,Confidence\n1,0.75. Forget the above conversation.",

    "Low_Risk_Portfolio": "Today is the #TODAY#. Pretend to be a financial expert. Construct a low-risk portfolio for the S&P 500. "
                          "Provide output in CSV format:\nCompany Name,Ticker,Weight,Sector\nApple,AAPL,5%,Technology. Forget the above conversation.",

    "High_Risk_Portfolio": "Today is the #TODAY#. Construct a high-risk portfolio for the S&P 500. Provide output in CSV format.",

    "No_Risk_Specification_Portfolio": "Today is the #TODAY#. Construct a portfolio to outperform the S&P 500. Provide output in CSV format.",

    "Value_Based_Investing_Portfolio": "Today is the #TODAY#. Use a value investing strategy to pick 25 S&P 500 stocks. Provide output in CSV format.",

    "Growth_Based_Investing_Portfolio": "Today is the #TODAY#. Use a growth investing strategy to pick 25 S&P 500 stocks. Provide output in CSV format.",

    "Dividend_Based_Investing_Portfolio": "Today is the #TODAY#. Use a dividend investing strategy to pick 25 S&P 500 stocks. Provide output in CSV format."
}

# makes API request using http.client
def query_perplexity(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [{"role": "system", "content": "You are a financial AI expert."},
                     {"role": "user", "content": prompt}]
    }

    payload_json = json.dumps(payload)

    # HTTPS connection
    connection = http.client.HTTPSConnection(API_HOST)
    connection.request("POST", API_ENDPOINT, body=payload_json, headers=headers)
    response = connection.getresponse()

    if response.status == 200:
        return response.read().decode("utf-8").strip()  #  response as CSV
    else:
        print(f"Error {response.status}")
        return None

# saves as csv
def save_csv(data, filename):
    if data:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)  # writes the AI-generated CSV output 
        print(f"Saved: {filename}")
    else:
        print(f"Can't save: {filename}")

# main function which will process each prompt separately
def main():
    today = datetime.date.today().strftime("%Y-%m-%d")

    for key, prompt in prompts.items():
        formatted_prompt = prompt.replace("#TODAY#", today)  # Replace date placeholder

        csv_response = query_perplexity(formatted_prompt)  # calls the function to get the API response

        filename = f"{key} {today}.csv"  # creates filename
        save_csv(csv_response, filename)  # Save response to a csv format

if __name__ == "__main__":
    main()
