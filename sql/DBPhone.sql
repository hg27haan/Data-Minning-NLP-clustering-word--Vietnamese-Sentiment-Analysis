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
    phone_name NVARCHAR(MAX),
    specifications NVARCHAR(MAX)
);
GO

-- Tạo bảng comment
CREATE TABLE comment (
    id INT IDENTITY PRIMARY KEY,
    user_id INT,
    comment NVARCHAR(MAX),
    predict NVARCHAR(MAX)
    FOREIGN KEY (user_id) REFERENCES users(id)
);
GO

-- Tạo bảng comment_phone
CREATE TABLE comment_phone (
    id_phone INT NOT NULL, 
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
INSERT INTO phone (phone_name, specifications) VALUES
(N'iPhone 12', '[12MP, 4GB, 64GB, 2815mAh, Iphone(Apple)]'),
(N'iPhone 12 Pro', '[12MP, 6GB, 128GB, 2815mAh, Iphone(Apple)]'),
(N'iPhone 12 Pro Max', '[12MP, 6GB, 128GB, 3687mAh, Iphone(Apple)]'), 
(N'iPhone 13', '[12MP, 4GB, 128GB, 3240mAh, Iphone(Apple)]'),
(N'iPhone 13 Pro', '[12MP, 6GB, 128GB, 3095mAh, Iphone(Apple)]'),
(N'iPhone 13 Pro Max', '[12MP, 6GB, 128GB, 4352mAh, Iphone(Apple)]'),
(N'iPhone 14', '[12MP, 6GB, 128GB, 3279mAh, Iphone(Apple)]'),
(N'iPhone 14 Pro', '[48MP, 6GB, 128GB, 3200mAh, Iphone(Apple)]'),
(N'iPhone 14 Pro Max', '[48MP, 6GB, 512GB, 4323mAh, Iphone(Apple)]'),
(N'Samsung Galaxy S21', '[12MP, 8GB, 128GB, 4000mAh, Samsung]'),
(N'Samsung Galaxy S21 Ultra', '[108MP, 12GB, 128GB, 5000mAh, Samsung]'),
(N'Samsung Galaxy Note 20', '[12MP, 8GB, 256GB, 4300mAh, Samsung]'),
(N'Samsung Galaxy Note 20 Ultra', '[108MP, 8GB, 256GB, 4500mAh, Samsung]'),
(N'Samsung Galaxy Z Fold 3', '[12MP, 12GB, 256GB, 4400mAh, Samsung]'),
(N'Samsung Galaxy Z Flip 3', '[12MP, 8GB, 128GB, 3300mAh, Samsung]'),
(N'Xiaomi Mi 11', '[108MP, 8GB, 256GB, 4600mAh, Xiaomi]'),
(N'Xiaomi Mi 11 Ultra', '[50MP, 12GB, 412GB, 5000mAh, Xiaomi]'),
(N'Xiaomi Redmi Note 10', '[48MP, 6GB, 128GB, 5000mAh, Xiaomi]'),
(N'OnePlus 9', '[50MP, 8GB, 128GB, 4500mAh, OnePlus]'),
(N'OnePlus 9 Pro', '[50MP, 12GB, 256GB, 4500mAh, Google]'),
(N'Google Pixel 5', '[12.2MP, 8GB, 128GB, 4085mAh, Google]'),
(N'Google Pixel 6', '[50MP, 8GB, 128GB, 4614mAh, Google]'),
(N'Google Pixel 6 Pro', '[50MP, 12GB, 128GB, 5003mAh, Google]'),
(N'Oppo Find X3 Pro', '[50MP, 12GB, 256GB, 4500mAh, OPPO]'),
(N'Oppo Reno 6', '[64MP, 8GB, 128GB, 4300mAh, OPPO]'),
(N'Vivo X60 Pro', '[48MP, 12GB, 256GB, 4200mAh, Vivo]'),
(N'Sony Xperia 1 III', '[12MP, 12GB, 256GB, 4500mAh, Sony]'),
(N'Sony Xperia 5 III', '[12MP, 8GB, 256GB, 4500mAh, Sony]'),
(N'Asus ROG Phone 5', '[64MP, 16GB, 256GB, 6000mAh, Asus]'),
(N'Nokia 8.3', '[64MP, 8GB, 128GB, 4500mAh, Asus]');
