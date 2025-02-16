Email Scheduler
This Python script allows you to schedule an email from one Gmail account to another. It is designed exclusively for Gmail accounts and does not support any other email providers.

Features
Schedule an email to be sent at a specific date and time.
Secure authentication using a 16-digit Google App Password.
Ensures compatibility with two-step verification.

Prerequisites
A Gmail account.
A 16-digit Google App Password (generated from your Google account settings).
Python installed on your system.

How to Generate a 16-digit Google App Password
Go to your Google Account: Google Account Security
Under "Signing in to Google," select "App Passwords."
Generate a new 16-digit App Password for "Mail."
Use this password instead of your normal Gmail password.

How to Use
Clone or download this repository.
Open a terminal or command prompt and navigate to the script's directory.
Run the script using Python: python emai_scheduler.py

Enter the required details:
Sender's Gmail address
Receiver's Gmail address
16-digit Google App Password
Email subject and body
Scheduled date and time (YYYY-MM-DD HH:MM:SS format, 24-hour format)
The script will wait until the scheduled time and then send the email automatically.

Important Notes
This script only supports Gmail accounts.
Ensure you have enabled "Less secure app access" if required (Google may block login attempts otherwise).
The script must be running at the scheduled time for the email to be sent.

Troubleshooting
Authentication Error: Ensure you are using the correct 16-digit App Password.
Incorrect Time Format: Enter the scheduled time in YYYY-MM-DD HH:MM:SS format (24-hour format).
Email Not Sent: Ensure your internet connection is active at the scheduled time.

Author
Katyayani
Contact: katyayani05102005@gmail.com

License
This project is open-source and available under the MIT License.

