from init import  app, socketio
import view

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

if __name__ == '__main__':
    socketio.run(app, debug=True)
