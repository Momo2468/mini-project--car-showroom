-- Car Showroom Database Setup

CREATE DATABASE IF NOT EXISTS showroom;
USE showroom;

-- Cars table
CREATE TABLE cars (
    sno INT PRIMARY KEY,
    model VARCHAR(100),
    price VARCHAR(50)
);

INSERT INTO cars VALUES
(1, 'Mercedez Benz', '18733 kwd'),
(2, 'Porsche 911', '33600 kwd'),
(3, 'Land Cruiser Prado', '12688 kwd'),
(4, 'Range Rover Velar', '25820 kwd'),
(5, 'Porsche Vision 357', '101600 kwd'),
(6, 'BMW X5', '37560 kwd'),
(7, 'Koenigsegg Gemera', '424000 kwd'),
(8, 'Ferrari SF90', '158500 kwd'),
(9, 'Rolls Royce Cullinan', '106000 kwd'),
(10, 'Lexus LC', '33950 kwd'),
(11, 'BMW Z4', '17450 kwd'),
(12, 'Ferrari 296 GTS', '116670 kwd');

-- Customer details table
CREATE TABLE customerdetails (
    car_order VARCHAR(100),
    cust_name VARCHAR(100),
    phoneNo BIGINT
);

INSERT INTO customerdetails VALUES
('Ferrari SF90', 'Rose Hathaway', 30021785),
('BMW X5', 'Adam Carlsen', 76543218),
('Koenigsegg Gemera', 'Taylor Swift', 13198922),
('Lexus LC', 'Rachel Green', 456781239),
('Land Cruiser Prado', 'Adrian Ivashkov', 13579139);
