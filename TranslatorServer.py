from flask import Flask, render_template, request
from flask_socketio import SocketIO
import GtransWrapper as GTW

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
clients = []
SSIDmap = []
ClientLanguageMap = {}

@app.route('/')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('ChatProcessing')
def handle_my_chat_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    for client in clients:
        json['message'] = GTW.tanslatedata(json['message'], ClientLanguageMap[client])
        socketio.emit('my response', json,room=SSIDmap[clients.index(client)], callback=messageReceived)


@socketio.on('client_language_mapping')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    SSIDmap.append(request.sid)
    clients.append(str(json['user_name']))
    ClientLanguageMap[str(json['user_name'])] = str(json['language'])


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', debug=True)
