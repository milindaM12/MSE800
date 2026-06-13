# User Management System

## Project Overview

The User Management System is a web-based application designed to provide secure user account management and authentication services. The system follows a modular architecture to ensure maintainability, scalability, and readability.

Users can register, log in, manage their personal information, and recover forgotten passwords through a secure password reset process. Administrators can manage users, roles, and monitor system activities.

---

## Objectives

- Provide secure user registration and authentication.
- Allow users to manage their personal information.
- Implement a secure Forgot Password mechanism.
- Maintain a modular and scalable architecture.
- Demonstrate software engineering best practices.

---

## Features

### User Account Management
- User Registration
- User Login
- User Logout
- Profile Management
- Update Personal Information
- Delete Account

### Personal Information
The system stores the following user information:

- Full Name
- Date of Birth
- Email Address
- Username

### Authentication
- Secure Login Validation
- Session Management
- Email Verification

### Forgot Password
- Password Reset Request
- Reset Link Generation
- Token Verification
- Password Update

### Administration
- Manage Users
- Manage User Roles
- Monitor User Activities

### Reporting
- User Statistics
- Activity Reports

---

## Functional Decomposition

```
Main System
│
├── User Account Management
│   ├── Register User
│   ├── Login User
│   └── Profile Management
│       ├── Full Name
│       ├── Date of Birth
│       ├── Update Profile
│       └── Delete Account
│
├── Authentication
│   ├── Login Validation
│   ├── Session Management
│   └── Email Verification
│
├── Password Recovery
│   ├── Forgot Password
│   ├── Send Reset Email
│   ├── Verify Token
│   └── Reset Password
│
├── Administration
│   ├── Manage Users
│   ├── Manage Roles
│   └── Audit Logs
│
└── Reporting
    ├── User Statistics
    └── Activity Reports
```

---

## System Architecture

The project follows a layered architecture:

### Presentation Layer
- User Interface
- Forms
- Validation Messages

### Business Logic Layer
- Authentication Services
- User Management Services
- Password Recovery Services

### Data Access Layer
- Database Operations
- Repository Classes

### Database Layer
- User Data
- Roles
- Audit Logs

---

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Java Spring Boot / PHP / Node.js (Choose according to implementation)

### Database
- MySQL

### Version Control
- Git
- GitHub

---

## Database Schema

### User Table

| Field | Type | Description |
|---------|---------|---------|
| id | INT | Primary Key |
| full_name | VARCHAR(100) | User Full Name |
| date_of_birth | DATE | Date of Birth |
| email | VARCHAR(100) | User Email |
| username | VARCHAR(50) | Username |
| password | VARCHAR(255) | Encrypted Password |
| created_at | TIMESTAMP | Account Creation Date |

---

## Project Structure

```text
user-management-system
│
├── src
│   ├── controllers
│   ├── services
│   ├── repositories
│   ├── models
│   └── utilities
│
├── resources
│   ├── templates
│   └── static
│
├── database
│   └── schema.sql
│
├── docs
│   └── diagrams
│
└── README.md
```

---

## Security Features

- Password Encryption
- Session Management
- Input Validation
- Secure Password Reset Tokens
- Email Verification

---

## Future Enhancements

- Two-Factor Authentication (2FA)
- Social Login (Google, Facebook)
- User Activity Dashboard
- Account Locking Mechanism
- Role-Based Access Control (RBAC)

---