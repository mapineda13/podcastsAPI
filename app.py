from flask import Flask, render_template, request, jsonify, json
import urllib.request

app = Flask(__name__)


@app.route('/api/v1/show_podcasts/', methods=['GET'])
def show_podcasts_info():
    data_podcasts = get_podcasts_info()
    return jsonify(data_podcasts)


@app.route('/api/v1/show_podcasts_by_name/<artist_name>', methods=['GET'])
def search_podcasts_by_name(artist_name):
    data_podcasts = get_podcasts_info()
    data_podcasts = list(filter(lambda x: x["artistName"] == artist_name.strip(), data_podcasts))
    return jsonify(data_podcasts)


def get_podcasts_info():
    source = urllib.request.urlopen(
        'https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json'
    ).read()
    list_podcasts = json.loads(source)
    list_podcasts = list_podcasts['feed']
    list_podcasts = list_podcasts['results']
    return list_podcasts
