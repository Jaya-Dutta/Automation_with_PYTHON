CREATE DATABASE IF NOT EXISTS api_automation_db;

USE api_automation_db;

CREATE TABLE IF NOT EXISTS api_users (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    city VARCHAR(100)
);

INSERT IGNORE INTO api_users (id, name, email, city)
VALUES
    (1, 'John Doe', 'john@example.com', 'Kolkata'),
    (2, 'Jane Smith', 'jane@example.com', 'Siliguri'),
    (3, 'Rahul Das', 'rahul@example.com', 'Delhi');

SELECT * FROM api_users;