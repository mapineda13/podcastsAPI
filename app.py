from flask import Flask, jsonify, json
import urllib.request

app = Flask(__name__)


def get_podcasts_info():
    source = urllib.request.urlopen(
        'https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json'
    ).read()
    list_podcasts = json.loads(source)
    list_podcasts = list_podcasts['feed']
    list_podcasts = list_podcasts['results']
    return list_podcasts


@app.route('/api/v1/show_podcasts/', methods=['GET'])
def show_podcasts_info():
    data_podcasts = get_podcasts_info()
    return jsonify(data_podcasts)


@app.route('/api/v1/show_podcasts_by_name/<artist_name>', methods=['GET'])
def search_podcasts_by_name(artist_name):
    data_podcasts = get_podcasts_info()
    data_podcasts = list(filter(lambda x: x["artistName"] == artist_name.strip(), data_podcasts))
    return jsonify(data_podcasts)


@app.route('/api/v1/save_top20_podcasts/', methods=['POST'])
def save_top20_podcasts():
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


@app.route('/api/v1/save_top20_from_bottom_podcasts/', methods=['POST'])
def save_top20_from_bottom_podcasts():
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

