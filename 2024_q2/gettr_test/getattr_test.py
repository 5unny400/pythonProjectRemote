"""
@FileName：getattr_test
@Description：
@Author：shenxinyuan
@Time：2024/6/27
"""
dict_1 = {'a': 1, 'b': 2, 'c': 3}
class class_1:
    def __init__(self):
        self.a = 1
        self.json=None
clasaa = class_1()
gett = getattr(clasaa, 'json', {})
print(gett)

# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
#
# # demo1
# @app.route('/example', methods=['POST'])
# def example():
#     # 使用 get_json(silent=True) 处理没有 JSON 数据的情况
#     json_data = request.get_json(silent=True) or {}
#
#     return jsonify(json_data)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
# # demo2
# @app.route('/example', methods=['POST'])
# def example():
#     # 使用 getattr 处理没有 JSON 数据的情况
#     json_data = getattr(request, 'json', None) or {}
#
#     return jsonify(json_data)
