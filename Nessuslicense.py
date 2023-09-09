import os
import platform
import subprocess
import requests
import random
import string
import re

print("""
▒█▄░▒█ █▀▀ █▀▀ █▀▀ █░░█ █▀▀ 　 ▒█░▄▀ █▀▀ █░░█ █▀▀▀ █▀▀ █▀▀▄ 
▒█▒█▒█ █▀▀ ▀▀█ ▀▀█ █░░█ ▀▀█ 　 ▒█▀▄░ █▀▀ █▄▄█ █░▀█ █▀▀ █░░█ 
▒█░░▀█ ▀▀▀ ▀▀▀ ▀▀▀ ░▀▀▀ ▀▀▀ 　 ▒█░▒█ ▀▀▀ ▄▄▄█ ▀▀▀▀ ▀▀▀ ▀░░▀""")
print("==== Developed - Harsh Dhamaniya - Consultant ====")

def get_mail():
    S = 15
    D = 7
    E = [".com", ".in", ".co", ".cn", ".org", ".info", ".eu", ".ru", ".de", ".net"]
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    domain = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    extension = E[random.randint(0, 9)]
    mail_id = name + "@" + domain + extension
    return mail_id

def generate_nessus_pro():
    data = {
        "first_name": "moahn",
        "last_name": "lal",
        "email": get_mail(),
        "phone": random.randrange(0000000000, 9999999999, 10),
        "code": "",
        "country": "IN",
        "region": "",
        "zip": "505474",
        "title": "security engineer",
        "company": "secyrask",
        "consentOptIn": "true",
        "essentialsOptIn": "false",
        "pid": "",
        "utm_source": "",
        "utm_campaign": "",
        "utm_medium": "",
        "utm_content": "",
        "utm_promoter": "",
        "utm_term": "",
        "alert_email": "",
        "_mkto_trk": "id:934-XQB-568&token:_mch-tenable.com-1667551532394-27662",
        "mkt_tok": "",
        "queryParameters": "utm_promoter=&utm_source=&utm_medium=&utm_campaign=&utm_content=&utm_term=&pid=&lookbook=&product_eval=nessus",
        "referrer": "https://www.tenable.com/products/nessus/nessus-professional?utm_promoter=&utm_source=&utm_medium=&utm_campaign=&utm_content=&utm_term=&pid=&lookbook=&product_eval=nessus",
        "lookbook": "",
        "apps": ["nessus"],
        "companySize": "10-49",
        "preferredSiteId": "",
        "tempProductInterest": "Nessus Professional",
        "partnerId": ""
    }

    response = requests.post('https://www.tenable.com/evaluations/api/v1/nessus-pro', json=data)

    try:
        regex = r"\"code\":\"(.*)\","
        matches = re.search(regex, response.text)
        activation_code = matches.group(1)
        print("Nessus Activation Code: " + activation_code)
        return activation_code
    except AttributeError:
        print("Failed to retrieve Nessus Activation Code.")
        return None

def update_nessus_key_windows(activation_code):
    try:
        # Check if the script is running with administrator privileges on Windows
        if platform.system() == "Windows" and not os.environ.get("ADMIN"):
            params = f"\"{activation_code}\""
            script = os.path.abspath(__file__)
            # Re-run the script with administrator privileges
            subprocess.run(f'powershell -Command "Start-Process python -ArgumentList \'{script} {params}\' -Verb RunAs"', shell=True)
            return

        # Code to stop Nessus service (OS-specific)
        stop_command = ""
        start_command = ""
        fix_reset_command = ""
        if platform.system() == "Windows":
            stop_command = "net stop \"Tenable Nessus\""
            start_command = "net start \"Tenable Nessus\""
            fix_reset_command = r"C:\Program Files\Tenable\Nessus\nessuscli.exe fix --reset"
        elif platform.system() == "Linux":
            stop_command = "/etc/init.d/nessusd stop"
            start_command = "/etc/init.d/nessusd start"
            fix_reset_command = "/opt/nessus/sbin/nessuscli fix --reset"
        elif platform.system() == "Darwin":
            stop_command = "sudo launchctl stop com.tenablesecurity.nessusd"
            start_command = "sudo launchctl start com.tenablesecurity.nessusd"
            fix_reset_command = "/Library/Nessus/run/sbin/nessuscli fix --reset"
        else:
            print("Unsupported OS for Nessus Professional.")
            return

        print(f"OS Identified: {platform.system()}")

        print("Stopping Nessus service...")
        stop_output = subprocess.run(stop_command, capture_output=True, shell=True, text=True)
        print(stop_output.stdout)

        # Run nessuscli fix --reset command
        fix_reset_output = subprocess.run(fix_reset_command, capture_output=True, shell=True, text=True)
        print(fix_reset_output.stdout)

        # Code to update the Nessus key (Linux and MacOS)
        update_command = ""
        if platform.system() == "Windows":
            nessus_path = r"C:\Program Files\Tenable\Nessus"
            update_command = f"{nessus_path}\\nessuscli fetch --register {activation_code}"
            print("Updating Nessus key...")
            update_output = subprocess.run(update_command, capture_output=True, shell=True, text=True, cwd=nessus_path)
            print(update_output.stdout)
        elif platform.system() == "Linux":
            update_command = f"/opt/nessus/sbin/nessuscli fetch --register {activation_code}"
            print("Updating Nessus key...")
            update_output = subprocess.run(update_command, capture_output=True, shell=True, text=True)
            print(update_output.stdout)
        elif platform.system() == "Darwin":
            update_command = f"/Library/Nessus/run/sbin/nessuscli fetch --register {activation_code}"
            print("Updating Nessus key...")
            update_output = subprocess.run(update_command, capture_output=True, shell=True, text=True)
            print(update_output.stdout)
        else:
            print("Unsupported OS for Nessus Professional.")
            return

        # Code to start Nessus service (OS-specific)
        print("Starting Nessus service...")
        start_output = subprocess.run(start_command, capture_output=True, shell=True, text=True)
        print(start_output.stdout)

        print("Nessus key has been updated successfully.")
    except Exception as e:
        print("Error updating Nessus key:", str(e))

def generate_nessus_expert():
    random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 10)))
    random_first_name = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10)))
    random_last_name = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(4, 8)))
    random_phone = ''.join(random.choice(string.digits) for _ in range(10))

    payload = {
        "first_name": random_first_name,
        "last_name": random_last_name,
        "email": f"{random_name}@harsh-dhamaniya.com",
        "phone": random_phone,
        "code": "",
        "country": "IN",
        "region": "",
        "zip": "110008",
        "title": "consultant",
        "company": "nangia andersen",
        "consentOptIn": True,
        "essentialsOptIn": False,
        "pid": "",
        "alert_email": "",
        "apps": ["expert"],
        "companySize": "100-249",
        "preferredSiteId": "",
        "tempProductInterest": "Nessus Expert",
        "partnerId": "",
        "gclid": ""
    }

    url = "https://www.tenable.com/evaluations/api/v1/nessus-expert"

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Please use the below mentioned Email for the Registration of Nessus Expert")
        print("--------------------------------------")
        print(f"Email: {random_name}@harsh-dhamaniya.com")
        print("--------------------------------------")
    else:
        print("Request failed.")

def main():
    while True:
        print("Welcome To Nessus Subscription Generator")
        print("1. Nessus Professional Key")
        print("2. Nessus Expert Email")
        user_input = input("Please Select Your Subscription: ")
        if user_input == "1":
            activation_code = generate_nessus_pro()
            if activation_code:
                update_key_input = input("Do you want to update the key? (y/n): ").lower()
                if update_key_input == "y":
                    update_nessus_key_windows(activation_code)
            break
        elif user_input == "2":
            generate_nessus_expert()
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == '__main__':
    main()
