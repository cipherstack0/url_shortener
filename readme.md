# URL Shortener

A simple URL shortener built as a training project while learning Python, Flask, MySQL, pytest, Git, and GitHub Actions.

> **Note:** This is a learning project focused primarily on backend development, testing, and DevOps practices. The frontend is intentionally very simple.

## What it does

The application takes a long URL and generates a shorter URL using Base62 encoding.

For example:

    https://example.com -> http://localhost:5000/b

Visiting the shortened URL redirects the user to the original URL.

## Technologies

- Python
- Flask
- MySQL
- pytest
- Git / GitHub
- GitHub Actions


## Testing

Tests are written using pytest.

Run the test suite with:

    pytest

The project also uses GitHub Actions to automatically run the tests when changes are pushed to GitHub or a pull request is created.

The CI environment starts a MySQL service so that the database-dependent tests can run automatically.

## Running locally

### 1. Clone the repository

    git clone <repository-url>
    cd url_shortener

### 2. Create a virtual environment

    python -m venv .venv

Activate it:

    source .venv/bin/activate

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Configure MySQL

The application requires a local MySQL server.

Set the MySQL password as an environment variable:

    export MYSQL_PASSWORD="your-password"

The application will create the `short_url_db` database and required table when it starts.

### 5. Run the application

    python app.py

The application will then be available at:

    http://localhost:5000

## What I learned

This project was primarily used for practicing:

- Building a basic Flask application
- Working with MySQL from Python
- Generating Base62 short codes
- Writing unit and integration tests with pytest
- Using fixtures with pytest
- Managing Python dependencies
- Using environment variables for configuration
- Using Git and GitHub
- Setting up a CI pipeline with GitHub Actions
- Running database-dependent tests in a CI environment

## Future improvements

Possible improvements include:

- Better frontend styling
- URL validation
- More robust error handling
- Database cleanup between tests
- Dockerizing the application
- Deploying the application