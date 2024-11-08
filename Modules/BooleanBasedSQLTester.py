from Modules.ResponseAnalyzer import analyze_response
from Modules.URLUtils import construct_test_url
from Modules.RequestHandler import send_payload
# SQL injection payloads for testing
boolean_based_test = [" AND {}%23", "' AND {}%23", '" AND {}%23']
# test_2_payloads = [" AND 1=2", "' AND '1'='2", '" AND "1"="2']
time_based_payloads = [" AND SLEEP({})", "' AND SLEEP({})%23", '" AND SLEEP({})%23']


def test_boolean_based_sql_injection(target_url, id_value):
    print(f"\nTesting default request: {target_url}")
    default_response = send_payload(target_url)
    print(f"Default response: {default_response}")

    # Test: Check for Boolean-based vulnerabilities
    print("\nTesting with Boolean-based conditions:")
    test_1_responses = []  # Store responses for True conditions
    for payload in boolean_based_test:
        formatted_payload = payload.format("1=1")  # Insert a true condition
        new_url = construct_test_url(target_url, id_value, formatted_payload)
        response = send_payload(new_url)
        if analyze_response(default_response, response, formatted_payload):  # True condition matches default response
            test_1_responses.append(response)  # Store true responses

    # Check for False conditions using the same placeholders
    print("\nTesting with False conditions:")
    for payload in boolean_based_test:
        formatted_payload = payload.format("1=2")  # Insert a false condition
        new_url = construct_test_url(target_url, id_value, formatted_payload)
        response = send_payload(new_url)

        # Test for SQLi by confirming:
        # 1. Test 1 response == Default response
        # 2. Test 2 response != Test 1 response (indicating vulnerability)
        if default_response == test_1_responses[0] and response != test_1_responses[0]:
            print(f"Payload {formatted_payload} indicates a likely vulnerability (Boolean-based SQLi).")
            return "boolean", formatted_payload, default_response

    # If no vulnerabilities found, return None
    return None, None
