# Odoo Courses Module

This is a custom module for Odoo 18 developed as part of a lab exercise (Lab 1) during my ITI Full-Stack Web Development diploma. The module introduces a basic **Course Management System** inside Odoo.

## 📚 Features

- Custom model `courses.course`
- Fields include:
  - Course Name
  - Description
  - Start Date / End Date
  - Cost
  - Teacher
  - Responsible User (linked to res.users)
- Custom views:
  - Tree (list) view
  - Form view with grouped fields and notebook sections
- Accessible through a dedicated menu and action window

## 🛠 Tech Stack

- Odoo 18
- Python 3.12
- PostgreSQL
- XML for view definitions

## 📁 Directory Structure

custom-addons/
└── courses/
├── init.py
├── manifest.py
├── models/
│ └── course.py
├── views/
│ └── course_views.xml


## 🚀 Getting Started

1. Clone this repository into your Odoo `custom-addons` directory.
2. Add the path to `addons_path` in your `odoo.conf`.
3. Restart the Odoo server and update the app list.
4. Install the module "Courses" via the Apps menu.
