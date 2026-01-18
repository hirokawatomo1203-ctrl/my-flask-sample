
from flask import Flask, request, render_template_string
app = Flask(__name__)

names = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            names.append(name)
    html = """
    <h1>名前入力フォーム</h1>
    <form method="post">
        <input type="text" name="name" placeholder="名前を入力">
        <button type="submit">追加</button>
    </form>
    <h2>登録済みの名前一覧</h2>
    <ul>{% for n in names %}<li>{{ n }}</li>{% endfor %}</ul>
    """
    return render_template_string(html, names=names)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
``
