# Function to analyze and compare server responses
def analyze_response(default_response, test_response, payload):
    if len(default_response) == len(test_response):
        print(f"Payload '{payload}' produced a similar response (likely true condition).")
    else:
        print(f"Payload '{payload}' produced a different response (likely false condition).")
