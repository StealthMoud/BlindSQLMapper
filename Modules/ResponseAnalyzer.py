# Function to analyze and compare responses
def analyze_response(default_response, test_response, payload):
    if test_response == default_response:
        return True
    else:
        return False
