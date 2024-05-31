# Sentiment Analysis Service

## Setup

1. Clone the repository:
git clone <repository_url>
cd <repository_name>

2. Build the Docker image:
docker build -t sentiment-analysis .

3. Run the Docker container:
docker run -p 8000:8000 sentiment-analysis


4. Open your browser and go to `http://localhost:8000`.

## Usage

1. Enter text in the text area.
2. Click the "Analyze" button.
3. The sentiment analysis result will be displayed below.

## Project Structure

- `sentiment_analysis/`: The main Django project.
- `analysis/`: The Django app.
- `Dockerfile`: The Docker configuration.
- `requirements.txt`: The list of dependencies.
- `README.md`: Instructions and project information.

