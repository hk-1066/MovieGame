import flask
from init import socketio
from flask_socketio import emit, join_room
import tmdbsimple as tmdb

tmdb.API_KEY = '701bd419040c3b2b3f50ba8ff3f1c2b9' #Collin got this KEY from creating an acount with tmdb...I think

@socketio.on('getMovie')
def getMovie(data):
    print("inside API getMovie")

    search = tmdb.Search()
    response = search.movie(query= data['movie_title'])
    for s in search.results:
        print(s['title'], s['id'], s['release_date'], s['popularity'])
