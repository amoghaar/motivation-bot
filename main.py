import random
import smtplib
import datetime as dt
import chardet

# Get the current date and time
now = dt.datetime.now()

# Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
week_day = now.weekday()

# Check if it's a weekday (Monday to Friday)
if week_day in range(0, 5):

    # Detect the encoding of the quotes.txt file
    with open("quotes.txt", "rb") as f:
        result = chardet.detect(f.read())
        encoding = result["encoding"]

    # Read quotes from the file using the detected encoding
    with open("quotes.txt", encoding=encoding) as quote_file:
        all_quote = quote_file.readlines()

        # Select a random quote and remove leading/trailing whitespaces
        quote = random.choice(all_quote).strip()

    # Replace with your Gmail credentials
    my_email = ""    # type your Gmail ID
    my_password = ""    # read the ReadMe file for this

    # Connect to the Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Start the TLS connection
        connection.starttls()

        # Log in to your Gmail account
        connection.login(user=my_email, password=my_password)

        # Send the email
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",     # type the Gmail ID of the person you want to send
            msg=f"Subject:{now.weekday()}_Motivation\n\n{quote}".encode('utf-8')
        )

    print("Email sent successfully!")

else:
    print("Email not sent")
