from flask import Blueprint, request, jsonify

def res_format(code,data,msg):
    res = {
            'code':code,
            'data':data,
            'msg':msg
        }
    return jsonify(res)

def to_list(data):
    result = []
    for item in data:
        result.append(item.to_json())
    return result

def merge_dict(*dicts):
    res = {}
    for dict in dicts:
        res.update(dict)
    return res