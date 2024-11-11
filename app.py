from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def home():
    # Get current date and time
    now = datetime.now()

    # Welcome message
    welcome_message = "Welcome!"

    # Calculate days remaining for Sunday
    days_until_sunday = (6 - now.weekday()) % 7
    sunday_date = now + timedelta(days=days_until_sunday)

    # Calculate hours remaining for the end of the day
    hours_until_end_of_day = 24 - now.hour

    return f"""
    <html>
        <head>
            <title>Welcome Page</title>
        </head>
        <body style="font-family: Arial, sans-serif; text-align: center;">
            <h1>{welcome_message}</h1>
            <p><strong>Days until Sunday:</strong> {days_until_sunday} day(s)</p>
            <p><strong>Time left until the end of the day:</strong> {hours_until_end_of_day} hour(s)</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    # Run the app on port 5055
    app.run(host='0.0.0.0', port=5055)
