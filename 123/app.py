from flask import Flask, render_template # type: ignore
import json

app = Flask(__name__)

@app.route('/')
def index():
   
    with open("data/top_10.json", "r") as f:
        top_10_data = json.load(f)
    
    with open("data/type_stats.json", "r") as f:
        type_stats_data = json.load(f)
    
    # 渲染网页
    return render_template('index.html', top_10_data=top_10_data, type_stats_data=type_stats_data)

if __name__ == '__main__':
    app.run(debug=True)