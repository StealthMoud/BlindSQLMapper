import argparse
from sql_tester import test_sql_injection
from url_utils import extract_id

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Automate blind SQL injection tasks.")
    parser.add_argument("target_url", help="The URL of the vulnerable endpoint to target")
    args = parser.parse_args()

    # Extract the id value from the URL
    target_url = args.target_url
    id_value = extract_id(target_url)

    if id_value:
        # Run the SQL injection tests
        test_sql_injection(target_url, id_value)
    else:
        print("Error: No 'id' parameter found in the URL.")
