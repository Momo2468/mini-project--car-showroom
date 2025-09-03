-- Car Showroom Database Setup

CREATE DATABASE IF NOT EXISTS CarShowroom;
USE CarShowroom;

-- Table for car models
CREATE TABLE IF NOT EXISTS models (
    model_id INT PRIMARY KEY AUTO_INCREMENT,
    model_name VARCHAR(50) NOT NULL,
    price INT NOT NULL
);

-- Table for customer orders
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    model_id INT,
    customer_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (model_id) REFERENCES models(model_id)
);

-- Insert sample models
INSERT INTO models (model_name, price) VALUES
('Swift', 500000),
('Baleno', 700000),
('Innova', 1500000),
('Creta', 1200000);
