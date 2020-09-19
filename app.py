from flask import Flask, render_template, request, jsonify, json
import urllib.request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_info():
    return get_podcasts_info()


def get_podcasts_info():
    source = urllib.request.urlopen(
        'https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json'
    ).read()
    list_podcasts = json.loads(source)
    return list_podcasts


