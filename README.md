# Project Visionary: AI Image Analysis Platform 📸

Project Visionary is a full-stack web application that allows users to upload an image and receive an AI-generated caption describing it. The entire application is containerized with Docker and deployed on a cloud server.

**Live Application:** [https://ishan-visionary.tech](https://ishan-visionary.tech)

---

## Core Technologies

* **Backend:** Python, FastAPI
* **AI Model:** Hugging Face Transformers (`Salesforce/blip-image-captioning-large`)
* **Frontend:** HTML, CSS, Vanilla JavaScript
* **Containerization:** Docker
* **Cloud Hosting:** DigitalOcean Droplet
* **Web Server / Reverse Proxy:** Nginx
* **Security:** Let's Encrypt (for HTTPS/SSL)

---

## How It Works

1.  A user selects an image on the web interface and clicks "Analyze."
2.  The frontend sends the image to the FastAPI backend.
3.  The backend uses a pre-trained computer vision model from the Hugging Face `transformers` library to generate a descriptive caption.
4.  The API returns the caption as a JSON response.
5.  The frontend displays the returned caption to the user.

---

## Local Development Setup

To run this project on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/project-visionary.git](https://github.com/YourUsername/project-visionary.git)
    cd project-visionary
    ```
2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```
3.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```
4.  Open your browser and navigate to `http://localhost:8000`.

---

## Deployment

This application is deployed on a DigitalOcean Droplet using Docker.

1.  **Build the Docker Image:**
    ```bash
    docker build -t visionary-app .
    ```
2.  **Run the Docker Container:**
    ```bash
    docker run -d -p 8000:8000 visionary-app
    ```
3.  **Nginx Configuration:** Nginx is used as a reverse proxy to handle incoming traffic on port 80 and forward it to the application running on port 8000.
4.  **HTTPS:** Certbot is used to automatically provision and renew a free SSL certificate from Let's Encrypt, enabling secure `https` traffic.
