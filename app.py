import os

import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # 使用环境变量 OPENAI_API_KEY
openai.api_base = os.getenv("OPENAI_API_BASE")  # 指定请求地址，使用环境变量 OPENAI_API_BASE


# run on model gpt-3.5-turbo
@app.route("/", methods=("GET", "POST"))
def turbo():
    if request.method == "POST":
        response = openai.ChatCompletion.create(  # Needs OpenAI 0.27 above )
            model="gpt-3.5-turbo",
            messages=[
              {"role": "system", "content": "您是一位动物学专家"},
              {"role": "assistant", "content": "为一种超级英雄动物提供三个名字的建议"},
              {"role": "user", "content": "猫"},
              {"role": "assistant", "content": "锋利爪队长，绒球特工，无敌猫"},
              {"role": "user", "content": "狗"},
              {"role": "assistant", "content": "守护者拉夫，奇迹犬，吠吠爵士"},
              {"role": "user", "content": "动物"}
            ]
        )
        result = response['choices'][0]['message']['content']
        return render_template("index.html", result=result)
    result = request.args.get("result")
    return render_template("index.html", result=result)
