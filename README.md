# OpenAI API Quickstart - Python example app

This is an example pet name generator app used in the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

![Text box that says name my pet with an icon of a dog](/static/pnga.png)

如上，这是一个简单的 OpenAI API 官方应用示例，“给我的宠物取个超级英雄的名字”，Python Flask 框架构建。使用方式是输入一种动物名称后点击生成名称按钮，AI会返回三个超级英雄的名字给你。

## 阅读程序代码

见文件：`app.python`  和 `/templates/index.html`

重点关注 Open AI API 的调用逻辑：

```python
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
```
```html
<body>
  <img src="{{ url_for('static', filename='dog.png') }}" class="icon" />
  <h3>给我的宠物取三个超级英雄的名字</h3>
  <form action="/" method="post">
    <input type="text" name="animal" placeholder="输入一种动物" required />
    <input type="submit" value="生成名称" />
  </form>
  {% if result %}
  <div class="result">{{ result }}</div>
  {% endif %}
</body>
```

## 创建并激活虚拟环境

```bash
$ python -m venv venv
$ source venv/bin/activate
```

## 安装依赖

修改 `requirements.txt` 文件中的相关依赖及版本，在终端 shell 中执行：

```bash
$ pip install -r requirements.txt
```

## 运行应用程序

点击运行按钮运行应用程序，运行前确保运行命令配置正确（flask run），并指定了host和8080端口（flask run -h 0.0.0.0 -p 8080）
