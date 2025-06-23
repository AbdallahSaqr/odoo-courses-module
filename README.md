# Odoo Courses Management - Lab 2

This module is part of the ITI Full Stack Python program (Odoo Lab 2).  
It extends the basic course management system by adding student enrollment functionality and advanced views.

## Features

### 1. Course Management (`courses.course`)
- Fields: name, description, teacher, responsible, cost, start_date, end_date
- Views: List, Form, Kanban, Pivot (by name & cost), Graph (bar chart of cost)
- Embedded One2many list of enrollments shown in a notebook tab

### 2. Student Management (`courses.student`)
- Fields: name, code, birthdate, address
- Views: List (name + code), Form
- Accessed via submenu under Academic Management

### 3. Enrollment Management (`courses.enrollment`)
- Fields: name, student (Many2one), course (Many2one), enrollment date, cost (related to course cost)
- Views: List, Form
- Displayed inside the course form using a One2many field
- Enrollment cost auto-fetched from the related course

## Menu Structure
- **Academic Management**
  - Courses
  - Students
  - Enrollments

## Access Rights
Basic access is granted to internal users (group_user) for all models (read, create, write, unlink).

## Technical Details
- Built for Odoo 18.0
- Custom models defined under `models/` directory
- Views defined under `views/` directory
- Access rights defined in `security/ir.model.access.csv`

## Author
**Abdallah Ramadan Abdelshaphy**  
ITI Alexandria - Full Stack Python Track  
