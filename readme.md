# **Awesome Quiz Application** 🎉  

A dynamic and interactive web application for quizzes, built with Django, designed to enhance the user experience with a clean interface, user authentication, and personalized quiz history tracking.

---

## **Features** ✨  
- **User Authentication**: Secure login, registration, and logout functionality.  
- **Quiz Functionality**: Interactive quizzes with multiple-choice questions.  
- **Personalized Quiz History**: Tracks user quiz performance.  
- **Dark Mode**: A sleek dark mode for a comfortable user experience.  
- **Responsive Design**: Mobile-friendly interface.  
- **Admin Panel**: Manage quizzes, users, and history directly from the Django admin panel.

---

## **Tech Stack** 🛠️  
- **Backend**: Python, Django  
- **Frontend**: HTML, CSS, JavaScript  
- **Database**: SQLite (default) or any preferred database supported by Django  
- **Styling**: Custom CSS for an enhanced user interface  

---

## **Getting Started** 🚀  

### **Prerequisites**  
Ensure you have the following installed on your system:
- Python (>=3.8)  
- Git  

### **Installation**  

1. Clone the repository:  
   ```bash
   git clone https://github.com/Shivansh-Ahirwal/Quiz-Application.git
   cd QuizApp
   ```

2. Create a virtual environment:  
   ```bash
   python -m venv venv
   venv/Scripts/activate   # For Linux: venv/bin/activate
   ```

3. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

4. Create database migrations:  
   ```bash
   python manage.py makemigrations
   ```

5. Apply database migrations:  
   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:  
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:  
   ```bash
   python manage.py runserver
   ```

8. Open the application in your browser:  
   ```
   http://127.0.0.1:8000/
   ```

---

## **Usage**  
1. **Register or Login** to the application.  
2. Select a **quiz subject** and answer the questions.  
3. View your **results and performance history** on your profile page.  
4. Access the **admin panel** to manage content:  
   ```
   http://127.0.0.1:8000/admin/
   ```

---

## **Contributing** 🤝  
Contributions are welcome! Here's how you can help:  
- Submit bug reports or feature requests.  
- Fork the repository, make your changes, and submit a pull request.  

---

## **License** 📜  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact** 📧  
For any inquiries, reach out to:  
- **Author**: Shivansh Ahirwal 
- **LinkedIn**: [Shivansh Ahirwal](https://www.linkedin.com/in/shivansh-ahirwal-software-engineer/)  
