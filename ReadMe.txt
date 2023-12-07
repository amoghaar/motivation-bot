# Weekday Motivation Sender

Automate sending motivational emails on weekdays! This Python script selects a random quote from a file and sends it via Gmail.

## Requirements

- Python 3.x
- smtplib library (built-in with Python)
- chardet library (`pip install chardet`)

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/weekday-motivation-sender.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd weekday-motivation-sender
    ```

3. **Install the required library:**

    ```bash
    pip install chardet
    ```

4. **Replace your Gmail credentials in the script (`my_email` and `my_password`).**

5. **Prepare your quotes file (`quotes.txt`). Ensure the file encoding is detected correctly.**

6. **Run the script:**

    ```bash
    python motivation_sender.py
    ```

## Note

- The script sends motivational emails on weekdays with a random quote.
- The `quotes.txt` file contains 400+ quotes for variety.
- Adjust the day range (0-4) in the script to match your preferred weekdays.

## Gmail 2-Step Verification

1. Enable 2-step verification in your Gmail settings.
2. Navigate to "App Passwords" and add a new app (name it "weekday-motivation-sender").
3. Copy the generated code and replace `my_password` in the script (remove spaces).

## Auto Run (Optional)

To automate the script, consider using platforms like [PythonAnywhere](https://www.pythonanywhere.com/):
- Note that PythonAnywhere operates in UTC time.
- Keep in mind that PythonAnywhere has an expiration date for free accounts.

Feel free to customize the script, add more quotes, or improve its functionality according to your needs.
