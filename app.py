from flask import Flask, jsonify, json
import urllib.request

app = Flask(__name__)


def get_podcasts_info():
    try:
        source = urllib.request.urlopen(
            'https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json'
        ).read()
        list_podcasts = json.loads(source)
        list_podcasts = list_podcasts['feed']
        list_podcasts = list_podcasts['results']
        return list_podcasts
    except:
        return jsonify({'500': "Internal error"})


@app.route('/api/v1/show_podcasts/', methods=['GET'])
def show_podcasts_info():
    try:
        data_podcasts = get_podcasts_info()
        return jsonify(data_podcasts)
    except:
        return jsonify({'500': "Internal error"})


@app.route('/api/v1/show_podcasts_by_artist_name/<artist_name>', methods=['GET'])
def search_podcasts_by_artist_name(artist_name):
    try:
        data_podcasts = get_podcasts_info()
        data_podcasts = list(filter(lambda x: x["artistName"] == artist_name.strip(), data_podcasts))
        return jsonify(data_podcasts)
    except:
        return jsonify({'500': "Internal error"})


@app.route('/api/v1/save_top20_podcasts/', methods=['POST'])
def save_top20_podcasts():
    try:
        data_podcasts = get_podcasts_info()
        iterator = 0
        podcasts_list = []
        for podcast in data_podcasts:
            podcasts_list.append(podcast)
            iterator += 1
            if iterator == 20:
                break
        with open('json/top_20_podcasts.json', 'w') as json_file:
            json.dump(podcasts_list, json_file)
        return jsonify(podcasts_list)
    except:
        return jsonify({'500': "Internal error"})


@app.route('/api/v1/save_top20_from_bottom_podcasts/', methods=['POST'])
def save_top20_from_bottom_podcasts():
    try:
        data_podcasts = get_podcasts_info()
        iterator = 0
        reverse_data_podcasts = data_podcasts[::-1]
        podcasts_list = []
        for podcast in reverse_data_podcasts:
            podcasts_list.append(podcast)
            iterator += 1
            if iterator == 20:
                break
        with open('json/top_20_podcasts.json', 'w') as json_file:
            json.dump(podcasts_list, json_file)
        return jsonify(podcasts_list)
    except:
        return jsonify({'500': "Internal error"})


@app.route('/api/v1/remove_podcast/<int:position>', methods=['POST'])
def remove_podcast(position):
    try:
        position_remove = position - 1
        if position_remove < 0:
            return jsonify({'500': "ERROR: Can't remove zero position"})
        with open('json/top_20_podcasts.json', 'r') as podcasts_file:
            podcasts = json.load(podcasts_file)
            podcasts.pop(position_remove)
        with open('json/top_20_podcasts.json', 'w') as podcasts_file:
            json.dump(podcasts, podcasts_file)
        return jsonify(podcasts)
    except:
        return jsonify({'500': "Internal error"})
