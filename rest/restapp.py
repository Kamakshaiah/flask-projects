from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

languages = [{'language':'java'}, {'language': 'python'}, {'language': 'r'}]

@app.route('/', methods = ['GET'])
def home():
    return jsonify({'languages':languages})

@app.route('/<string:name>', methods = ['GET'])
def lang_name(name):
    langua = [lang for lang in languages if lang['language'] == name]
    return jsonify({'language':langua[0]})



if __name__ == '__main__':
    app.run()
