from abc import ABC, abstractmethod

import dotenv
from openai import OpenAI


class Summarizer(ABC):
	"""
	Summarizer接口，定义了一个summarize方法。
	"""

	@abstractmethod
	def summarize(self, transcript: str, prompt: str) -> str:
		"""
	    根据给定的transcript和prompt生成摘要。

	    :param transcript: 需要生成摘要的文本
	    :param prompt: 提示文本
	    :return: 生成的摘要
	    """
		pass


class OpenAISummarizer(Summarizer):
	"""
	OpenAISummarizer类，实现了Summarizer接口，并使用OpenAI的GPT-4模型来生成摘要。
	"""

	def __init__(self, api_key: str = None, client: OpenAI = None):
		"""
	    初始化OpenAISummarizer。

	    :type api_key: str
	    :param client: OpenAI的客户端对象
	    """
		if api_key is None:
			self.api_key = dotenv.get_key("../.env", "OPENAI_KEY")
		if client is None:
			self.client = OpenAI(api_key = api_key, base_url = "https://orisound.cn/v1")

	def summarize(self, transcript: str, video_title: str, user_intro_prompt: str = "") -> str:
		"""
	    根据给定的transcript和prompt使用OpenAI的GPT-4模型生成摘要。

	    :type transcript: 视频的文案
	    :param video_title: 视频标题
	    :param transcript: 需要生成摘要的文本
	    :param user_intro_prompt: 用户的自我介绍
	    :return: 生成的摘要
	    """
		user_intro_prompt = ""
		prompt = f"""
作为一名专业教程撰写者，你将处理一段名为‘{video_title}’的视频脚本。请根据视频脚本的主要内容和关键点，详细分析并提炼出视频中的核心思路和知识点。目标是为[{user_intro_prompt}]创建一份既包含理论知识又强调实际操作的Markdown教程。在教程中，加入清晰的步骤说明、代码示例（如果适用）、图表，并考虑加入互动元素以增强学习体验。注意使用恰当的Markdown格式和结构，以确保内容的清晰和易读性。
"""

		completion = self.client.chat.completions.create(
				model = "gpt-4-1106-preview",
				messages = [
					{ "role": "system", "content": f"{prompt}"},
					{ "role": "user", "content": f"{transcript}"}
				]
		)
		return completion.choices[0].message.content
