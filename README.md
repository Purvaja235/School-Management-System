# School Management System

## What this system looks like:

### 1. Login

 <img src="https://github.com/prakashtaz0091/school-management-system/blob/master/sms_dashboard/static/sms_dashboard/images/demo1.png" height="100%" /> 
 
###  2. Dashboard
 <img src="https://github.com/prakashtaz0091/school-management-system/blob/master/sms_dashboard/static/sms_dashboard/images/demo2.png" height="100%" /> 
 
###  3. Dashboard - Light Mode
 <img src="https://github.com/prakashtaz0091/school-management-system/blob/master/sms_dashboard/static/sms_dashboard/images/demo3.png" height="100%" /> 
 
###  4. Admit new student
 <img src="https://github.com/prakashtaz0091/school-management-system/blob/master/sms_dashboard/static/sms_dashboard/images/demo4.png" height="100%"/>

### 5. View Students

 <img src="https://github.com/prakashtaz0091/school-management-system/blob/master/sms_dashboard/static/sms_dashboard/images/demo5.png" height="100%" />

### 6. Edit student's info

 <img src="https://github.com/prakashtaz0091/school-management-system/blob/master/sms_dashboard/static/sms_dashboard/images/demo6.png" height="100%" />

### 7. Preview and Download ID card as .png

 <img src="https://github.com/prakashtaz0091/school-management-system/blob/master/sms_dashboard/static/sms_dashboard/images/demo7.png" height="100%" />

### 8. Add new Staff

 <img src="https://github.com/prakashtaz0091/school-management-system/blob/master/sms_dashboard/static/sms_dashboard/images/demo8.png" height="100%" />

### 9. Add new Class

 <img src="https://github.com/prakashtaz0091/school-management-system/blob/master/sms_dashboard/static/sms_dashboard/images/demo9.png" height="100%" />

### 10. View enrolled students

 <img src="https://github.com/prakashtaz0091/school-management-system/blob/master/sms_dashboard/static/sms_dashboard/images/demo10.png" height="100%" />

## Follow the instructions to run this system

## 1. Clone this repo

```
git clone https://github.com/prakashtaz0091/school-management-system
```

## 2. Create virtualenv of your choice for example in linux

```
pip install virtualenv

virtualenv myenv

source myenv/bin/activate

```

## 3. Create virtualenv in windows NOTE: switch to cmd instead of powershell

```
python -m venv env

env\Scripts\activate


```

## 3. Move to project directory

```
cd project
```

## 4. Install required packages and libraries

```
pip install -r requirements.txt
```

## 5. Run database migrations and migrate them

```
python manage.py makemigrations

python manage.py migrate
```

## 5. Start the development server,

### Note : If python doesn't works for you, try python3 or your installed version of python

```
python manage.py runserver
```

## 6. Open link in browser

```
http://localhost:8000
```
