# Database Configuration

## MySQL Setup
1. Create database and user:
   ```sql
   CREATE DATABASE pycontacts;
   CREATE USER 'souvik'@'localhost' IDENTIFIED BY 'Souvik1234';
   GRANT ALL PRIVILEGES ON pycontacts.* TO 'souvik'@'localhost';
   FLUSH PRIVILEGES;