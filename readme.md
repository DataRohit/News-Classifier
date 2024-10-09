# News Classifier

## Overview

This project is a news classifier application that collects news articles from various RSS feeds, categorizes them, and stores them in a PostgreSQL database.

## Setup

1. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2. **Database Setup**:
    - Create a PostgreSQL database and update the `DATABASE_URL` in `app/database.py`.

3. **Run the Application**:

    ```bash
    python run.py
    ```

4. **Start Celery Worker**:

    ```bash
    celery -A app.celery_tasks worker --loglevel=info
    ```

5. **Trigger Feed Parsing**:

    Access `http://localhost:5000/parse_feeds` to start parsing feeds.

## Testing

Run the tests with:

    ```bash
    python -m unittest discover tests/
    ```

### Database Schema

Make sure to create the PostgreSQL database before running the application. The schema is created automatically when the application starts.

### Running the Application

To run the application, ensure that Redis is running for Celery and PostgreSQL is set up properly. 

1. Start Redis:

    ```bash
    redis-server
    ```

2. Start PostgreSQL and create the database.

3. Run the application:

    ```bash
    python run.py
    ```

4. In another terminal, start the Celery worker:

    ```bash
    celery -A app.celery_tasks worker --loglevel=info
    ```

5. Access `http://localhost:5000/parse_feeds` to trigger the feed parsing.

This implementation provides a functional foundation for your news classifier application. You can further enhance the functionality, implement more robust error handling, and refine the classification logic as needed.
