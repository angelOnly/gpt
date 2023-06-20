# -*- coding: utf-8 -*-

# @File    : GPTServe.py
# @Date    : 2023-04-13
# @Author  : jiang

import sys
import os

sys.path.append("..")
base_dir = os.path.abspath(os.path.join(os.getcwd(), "."))

import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s-%(levelname)s: -> %(message)s')
logger = logging.getLogger(__name__)

from flask import request
import traceback
import json
from flask import Flask, Response
from flask_cors import CORS
import time

logger.info("启动成功!!!!!")
app = Flask(__name__)
CORS(app)

from ChatGPT import chatGPT


def parse_params():
    try:
        if request.method == "GET":
            content = request.args.get("content")
        else:
            data = json.loads(request.get_data())
            content = data['content'] if 'content' in data else ""

        if content:
            return {
                       "content": content
                   }, "success"
        else:
            return None, "content is null"
    except Exception as e:
        logger.error("parse_params: {} {}".format(request.get_data(), traceback.format_exc()))
        return None, "params parse error"


@app.route('/chatgpt/serve', methods=['GET', 'POST'])
def serve():
    try:
        t = time.time()
        params, info = parse_params()
        if params:
            res = chatGPT.chat(params)
        else:
            res = ""
        ts = round(time.time() - t, 4)
        logger.info(f"耗时 {chatGPT.model} {ts}")
        res = {"data": res, "status": 200, "msg": f"time spent:{ts}"}
    except Exception as e:
        logger.error(f"chatgpt错误: {traceback.format_exc()}")
        res = {"data": "", "status": 500, "msg": e}
    return Response(json.dumps(res, ensure_ascii=False), mimetype='application/json')
