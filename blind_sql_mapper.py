import argparse
from sql_tester import test_sql_injection
from url_utils import extract_id


def main():
    parser = argparse.ArgumentParser(description="Automate blind SQL injection tasks.")
    parser.add_argument("target_url", help="The URL of the vulnerable endpoint to target")
    args = parser.parse_args()

    id_value = extract_id(args.target_url)
    if id_value:
        test_sql_injection(args.target_url, id_value)
    else:
        print("Error: No 'id' parameter found in the URL.")


if __name__ == "__main__":
    main()
