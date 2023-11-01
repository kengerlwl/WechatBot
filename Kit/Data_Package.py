# from flask import current_app as app, request
# import functools
# import flask
# from flask import abort
# from flask import request
# from flask import jsonify, make_response

# import Kit

# rsp_code = {
#     "OK": 92000,
#     "Bad Request": 94000,
#     "Forbidden": 94030,
#     "Not Found": 94040,
#     "Internal Server Error": 95000,
#     "Bad Gateway": 95020
# }

# def common_rsp(data, status='OK'):
#     if status in rsp_code.keys():
#         code = rsp_code[status]
#     else:
#         code = 95001
#     rsp_format = request.args.get('format')
#     if rsp_format == 'raw':  # 如果指定了数据格式
#         return data
#     else:
#         return jsonify({
#             'code': code,
#             'status': status,
#             'time': Kit.str_time(),
#             'method': Kit.func_name(2),  # 出错的方法名
#             'timestamp': Kit.unix_time(),
#             'data': data
#         })

# # # 仅仅加入cors的headers，但是不作任何封装处理
# # def only_rsp_cors(data, status='OK'):
# #     resp = make_response(data)
# #     # 2、headers 中进行设置
# #     resp.headers["Content-Type"] = "application/json;chartset=UTF-8"  # 设置响应头
# #     resp.headers['Access-Control-Allow-Origin'] = '*'
# #     resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'  # 如果有其它方法（delete,put等），断续添加
# #     resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
# #     return resp