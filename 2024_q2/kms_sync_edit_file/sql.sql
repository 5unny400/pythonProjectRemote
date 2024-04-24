# 创建文档 CRDT 操作表

CREATE TABLE document_ops (
    id INT PRIMARY KEY AUTO_INCREMENT,
    document_id INT NOT NULL,
    op_type ENUM('INSERT', 'DELETE', 'UPDATE') NOT NULL,
    op_content TEXT NOT NULL,
    op_version INT NOT NULL,
    op_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX (document_id, op_version)
);

# 创建文档版本表

CREATE TABLE document_versions (
    id INT PRIMARY KEY AUTO_INCREMENT,

    document_id INT NOT NULL,
    version INT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    INDEX (document_id, version)
);

# 用户表

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

# 文档权限表
CREATE TABLE document_permissions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    document_id INT NOT NULL,
    user_id INT NOT NULL,
    permission ENUM('READ', 'WRITE', 'DELETE') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    INDEX (document_id, user_id)
);