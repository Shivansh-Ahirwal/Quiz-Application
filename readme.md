# QuizApplication

A Django-based web application for conducting quizzes with multiple-choice questions. The application allows a single user to start a quiz, answer random questions, and view results.

## Features

- Start a new quiz session.
- Automatically end any previous quiz session when a new session starts.
- Randomly display multiple-choice questions from a database.
- Track answers and categorize them as correct or incorrect.
- View results at the end of the quiz.

---

## Installation and Setup

### Prerequisites

1. Python 3.x
2. Django 4.x
3. Virtualenv (optional but recommended)

### Steps to Setup

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd QuizApplication
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Load initial questions data (optional):

   - Prepare a CSV file with the questions and use Django’s admin or a custom script to load it into the database.

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application in your web browser at:

   ```
   http://127.0.0.1:8000/
   ```

---

## Usage

### Starting a Quiz

1. Visit the homepage and click **Start Quiz**.
2. A new session will begin, and any previous sessions will be ended automatically.

### Answering Questions

- Each question will be displayed one at a time with four options (A, B, C, D).
- Select an option and submit your answer to proceed to the next question.

### Viewing Results

- After answering all questions or completing the session, the results page will display:
  - Total questions answered.
  - Number of correct answers.
  - Number of incorrect answers.

---

## Project Structure

```
QuizApp/
|-- quiz/                  # Django app for quiz functionality
|   |-- migrations/        # Database migrations
|   |-- static/            # CSS and static files
|   |-- templates/         # HTML templates
|   |-- admin.py           # Django admin configuration
|   |-- models.py          # Database models
|   |-- views.py           # Core application logic
|   |-- urls.py            # URL routing for the app
|-- QuizApp/       # Project configuration
|-- manage.py              # Django entry point
```

---

## Models

### `Question`

Represents a multiple-choice question.

- **Fields**:
  - `text`: The question text.
  - `option_a`, `option_b`, `option_c`, `option_d`: Four options for the question.
  - `correct_option`: The correct option (A, B, C, or D).

### `QuizSession`

Tracks a user's quiz session.

- **Fields**:
  - `user`: The user's name.
  - `questions_answered`: Number of questions answered in this session.
  - `correct_answers`: Number of correct answers.
  - `incorrect_answers`: Number of incorrect answers.

---

## Static Files

### CSS

Custom CSS for styling is located in:

```
quiz/static/css/
```

- `styles.css`: Contains styles for buttons, alignment, and results.

---

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- Community resources and tutorials for Django.

---

## Contact

For any questions or suggestions, feel free to contact:

- **Name**: Shivansh Ahirwal
- **Email**: [[shivanshahirwal@example.com](mailto\:shivanshahirwal@example.com)]