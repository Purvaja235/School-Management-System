📘 School Management System
Welcome to the School Management System! This project is designed to streamline school operations by managing student data, courses, attendance, grading, and more. Follow the instructions below to set up and run the system locally.

🛠️ Installation & Setup
1. Clone the Repository
Start by cloning the repository to your local machine:
git clone https://github.com/Purvaja235/School-Management-System.git

2. Set Up a Virtual Environment
Setting up a virtual environment helps keep dependencies isolated. Follow these steps based on your operating system.
⚠️ Note: Use CMD instead of PowerShell for Windows.
python -m venv env
env\Scripts\activate

3. Navigate to the Project Directory
Once inside the cloned folder, move to the project directory:
cd project

4. Install Required Packages
Install the necessary packages and libraries listed in requirements.txt:
pip install -r requirements.txt

5. Set Up the Database
Run database migrations to initialize the database schema:
python manage.py makemigrations
python manage.py migrate

6. Start the Development Server
Launch the server to view the system in action:
python manage.py runserver

⚠️ Note: If the python command doesn’t work, try using python3 or specify the exact version installed.

7. Access the Application
Once the server is up, open your browser and go to:
http://localhost:8000

🎉 Features
Student Management: Add, edit, and manage student profiles.
Course Management: Define courses, assign teachers, and organize schedules.
Attendance Tracking: Mark and monitor student attendance records.
Grade Book: Record and calculate student grades.
User Roles: Multiple roles, such as admin, teacher, and student, with role-based permissions.

🚀 Future Enhancements
Notifications: Automated notifications for students and parents.
Performance Analytics: Visual insights into student and class performance.
Mobile Compatibility: Responsive design for mobile and tablet users.

 
 
