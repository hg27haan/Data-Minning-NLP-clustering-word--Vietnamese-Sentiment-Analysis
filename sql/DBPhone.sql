-- Tạo cơ sở dữ liệu SalesPhone
CREATE DATABASE SalesPhone;
GO

-- Sử dụng cơ sở dữ liệu SalesPhone
USE SalesPhone;
GO

-- Tạo bảng users
CREATE TABLE users (
    id INT IDENTITY PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    full_name NVARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
GO

-- Tạo bảng phone
CREATE TABLE phone (
    id INT IDENTITY PRIMARY KEY,
    phone_name NVARCHAR(MAX)
	specifications NVARCHAR(MAX)
);
GO

-- Tạo bảng comment
CREATE TABLE comment (
    id INT IDENTITY PRIMARY KEY,
    user_id INT,
    comment NVARCHAR(MAX),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
GO

-- Tạo bảng comment_phone
CREATE TABLE comment_phone (
    id_phone INT NOT NULL, ->pram
    id_comment INT NOT NULL,
    PRIMARY KEY (id_phone, id_comment),
    FOREIGN KEY (id_phone) REFERENCES phone(id),
    FOREIGN KEY (id_comment) REFERENCES comment(id)
);
GO
INSERT INTO users (username, full_name, password) VALUES
('user1', N'Nguyễn Văn A', '123'),
('user2', N'Trần Thị B', '123'),
('user3', N'Lê Văn C', '123'),
('user4', N'Phạm Thị D', '123');
GO
INSERT INTO phone (phone_name) VALUES
(N'iPhone 12'),
(N'iPhone 12 Pro'),
(N'iPhone 12 Pro Max'), 
(N'iPhone 13'),
(N'iPhone 13 Pro'),
(N'iPhone 13 Pro Max'),
(N'iPhone 14'),
(N'iPhone 14 Pro'),
(N'iPhone 14 Pro Max'),
(N'Samsung Galaxy S21'),
(N'Samsung Galaxy S21 Ultra'),
(N'Samsung Galaxy Note 20'),
(N'Samsung Galaxy Note 20 Ultra'),
(N'Samsung Galaxy Z Fold 3'),
(N'Samsung Galaxy Z Flip 3'),
(N'Xiaomi Mi 11'),
(N'Xiaomi Mi 11 Ultra'),
(N'Xiaomi Redmi Note 10'),
(N'OnePlus 9'),
(N'OnePlus 9 Pro'),
(N'Google Pixel 5'),
(N'Google Pixel 6'),
(N'Google Pixel 6 Pro'),
(N'Oppo Find X3 Pro'),
(N'Oppo Reno 6'),
(N'Vivo X60 Pro'),
(N'Sony Xperia 1 III'),
(N'Sony Xperia 5 III'),
(N'Asus ROG Phone 5'),
(N'Nokia 8.3');
GO
