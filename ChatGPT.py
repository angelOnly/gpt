# -*- coding: utf-8 -*-

# @File    : ChatGPT.py
# @Date    : 2023-03-07
# @Author  : jiang
# conda activate py38
import sys
import os

sys.path.append("..")
base_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s-%(levelname)s: -> %(message)s')
logger = logging.getLogger(__name__)
import traceback
import openai
import random


class ChatGPT(object):
    def __init__(self):
        self.api_key_list = [
            
        ]
        # openai.api_key = "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"
        self.model = "gpt-3.5-turbo"
        self.role_comment = "user"
        self.comment_content = "You are a commentator, expressing opinions on other people's comments with humor, originality, and thoughtfulness"
        self.role = self.role_comment

    def chat(self, params):
        try:
            api_key = random.sample(self.api_key_list, 1)[0]
            openai.api_key = api_key
            content = params['content']
            # msg = {"role": self.role_comment, "content": self.comment_content}

            completion = openai.ChatCompletion.create(model=self.model,
                                                      messages=[{"role": "user", "content": content}])
            return completion.choices[0].message.content
        except Exception as e:
            if 'RateLimitError' in str(e):
                logger.info(f"chat {traceback.format_exc()} {params} ")
            else:
                logger.error(f"chat {traceback.format_exc()} {params} ")
        return ""

    def chat_comment(self, content, role=None, role_content=None):
        try:
            if role and role_content:
                msg = {"role": role, "content": role_content}
            else:
                msg = {"role": self.role_comment, "content": self.comment_content}

            completion = openai.ChatCompletion.create(model=self.model,
                                                      messages=[msg, {"role": role, "content": content}])
            return completion.choices[0].message.content
        except Exception as e:
            logger.error(f"chat {content} {traceback.format_exc()}")
        return ""


chatGPT = ChatGPT()
