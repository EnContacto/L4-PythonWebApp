# L4-PythonWebApp
Web application developed in Python and Flask that shows remaining days and elapsed hours.

## Description
This is a simple web application built with Flask and Pyhton. 
  - Days to go before Sunday arrives
  - Hours remaining until the end of the day 

The application is designed to run on port `5055` by default.

## Prerequisites
To run this application, ensure that the following are installed on your system:
- **Python** (version 3.12 or later)
- **Flask**
- **Werkzeug**

## How to Run the Application

### Running Locally
To run the application on your local machine:
1. Clone or download this repository to your computer.
   ```bash
   git clone https://github.com/EnContacto/L4-PythonWebApp.git
   cd L4-PythonWebApp
2. Open a terminal in the root directory of the project and install requirements.txt.
   ```bash
   pip install -r requirements.txt
3. Start app with:
   ```bash
   python app.py
Open your web browser and visit `http://localhost:5055` to see the application at work.
 
### Running with Docker
You can also run this application using Docker for a containerized environment.
1. In the project’s root directory, open a terminal and run:
   ```bash
   docker build -t python-webapp .

2. After the image is built, run the container using:
   ```bash
   docker run -p 5055:5055 python-webapp
The application should now be accessible at `http://localhost:5055` in your web browser.

## Troubleshooting
  - Ensure Docker is installed and running correctly if using the Docker setup.
  - Make sure no other application is using port `5055` before running the server.
