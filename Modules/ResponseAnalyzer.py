# Function to analyze and compare responses
def analyze_response(default_response, test_response, payload):
    # Check if the response is the same as the default response
    if test_response == default_response:
        print(f"Payload '{payload}' produced a similar response to the default (likely true condition).")
        return True  # True condition
    else:
        # Response is different from the default
        print(f"Payload '{payload}' produced a different response from the default (likely false condition).")
        return False  # False condition
