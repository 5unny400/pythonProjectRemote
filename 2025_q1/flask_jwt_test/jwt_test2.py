# jwt_test.py
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, decode_token
from datetime import timedelta

# 初始化Flask应用
app = Flask(__name__)

# 从config.py中获取JWT配置参数
JWT_SECRET_KEY = "your_jwt_secret_key"
JWT_DECODE_LEEWAY = timedelta(seconds=5)
JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=30)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(seconds=3600)
JWT_BLACKLIST_ENABLED = False
JWT_IDENTITY_CLAIM = "sub"
JWT_TOKEN_LOCATION = ["headers", "json"]

# 设置JWT配置参数
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_DECODE_LEEWAY'] = JWT_DECODE_LEEWAY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = JWT_REFRESH_TOKEN_EXPIRES
app.config['JWT_BLACKLIST_ENABLED'] = JWT_BLACKLIST_ENABLED
app.config['JWT_IDENTITY_CLAIM'] = JWT_IDENTITY_CLAIM
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION

# 初始化JWT管理器
jwt = JWTManager(app)

def generate_jwt_token(identity):
    with app.app_context():  # 设置应用上下文
        access_token = create_access_token(identity=identity, expires_delta=JWT_ACCESS_TOKEN_EXPIRES)
    return access_token

def verify_jwt_token(token):
    with app.app_context():  # 设置应用上下文
        try:
            decoded_token = decode_token(token)
            return True, decoded_token
        except Exception as e:
            return False, str(e)

# 测试生成token
test_identity = "test_user"
token = generate_jwt_token(identity=test_identity)
print(f"Generated JWT Token: {token}")

# 测试验证token
is_valid, result = verify_jwt_token(token)
if is_valid:
    print("Token is valid.")
    print(f"Decoded token data: {result}")
else:
    print("Token is invalid.")
    print(f"Error: {result}")
