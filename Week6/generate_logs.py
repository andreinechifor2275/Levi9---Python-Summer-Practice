# 1. Generate Dummy Log Data:
#     Create a module generate_logs.py within your project.
#     This module should contain a function generate_random_logs(entries_number, filename) that:
#     - Generates entries_number (e.g., 100-200) log entries.
#       Each log entry should be a dictionary with keys like:
#         - timestamp (current time, formatted between []; ex: [2025-07-22 12:54:07])
#         - level (randomly choose from "INFO", "WARNING", "ERROR")
#         - ip (a random integer using random.randint)
#         - username (a random user, e.g. "test_user", "admin", "guest")
#         - message (a random message, e.g., "User {user_name} logged in from IP {insert ip}",
#                                             "User {user_name} logged out from IP {insert ip}",
#                                             "Failed login attempt from IP ")
#             * when the error message is "ERROR", add "- Username: {username}" at the end of message
#     Writes these log entries, one per line, to the specified filename (e.g., system.log).
#
#     example: [2025-07-22 13:14:04] ERROR: Failed login attempt from IP 192.168.1.10 - Username: john
import random
from _datetime import datetime
def generate_random_logs(entries_number, filename):
    with open(filename, 'w') as log_file:

        levels = ["INFO", "WARNING", "ERROR"]
        usernames = ["admin", "guest", "test_user"]
        messages_templates = {
        "login": "User {username} logged in from IP {ip}",
        "logout": "User {username}  logged out from IP {ip}",
        "failed": "Failed login attempt from IP {ip}"}

        for i in range(entries_number):
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            level = random.choice(levels)
            username = random.choice(usernames)
            ip =f"{random.randint(100,999)}.{random.randint(0,255)}.{random.randint(0,9)}.{random.randint(10,99)}"

            if level == "INFO":
                template = messages_templates["login"]
                message = template.format(username=username, ip=ip)

            elif level == "WARNING":
                template = messages_templates["logout"]
                message = template.format(username=username, ip=ip)

            elif level == "ERROR":
                template = messages_templates["failed"]
                message = template.format(ip=ip)
                message += f" - Username: {username}"

            log_entry = f"{timestamp} {level}: {message}\n"
            log_file.write(log_entry)

if __name__ == "__main__":
    generate_random_logs(150,"log_file")

