# Database Configuration

## MySQL Setup
1. **Create database and user:**
   ```sql
    -- Create database (replace 'your_database_name')
    CREATE DATABASE your_database_name;

    -- Create user (replace 'your_username' and 'your_password')
    CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';

    -- Grant privileges
    GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost';
    FLUSH PRIVILEGES;
    ```

2. **Environment Variables:**
    Copy .env.example to .env and update with your credentials:
    ```ini
    SECRET_KEY=your_flask_secret_key
    DATABASE_URL=mysql+pymysql://your_username:your_password@localhost/your_database_name
    ```
