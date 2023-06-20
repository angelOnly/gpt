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
            # "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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",
            "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"
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
