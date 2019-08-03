from flask import Flask, render_template, request, redirect, url_for, jsonify
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
    return render_template('logonpage.html')


@app.route('/ChatApp/<UUID>')
def testHarveyUI(UUID):
    y = ""
    for k,v in ClientLanguageMap.items():
      y = y + k + "-" + v + ","
    return render_template('ChatApp.html', name=UUID, valva=y[:-1])


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('removeClient_mapping')
def remove_ClientMapping(json,  methods=['GET', 'POST']):
    SSIDmap.remove(request.sid)
    clients.remove(str(json['user_name']))
    del ClientLanguageMap[str(json['user_name'])]
    
@socketio.on('ChatProcessing')
def handle_my_chat_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    SSIDmap[clients.index(str(json['user_name']))] = request.sid
    for client in clients:
        json['message'] = GTW.tanslatedata(json['message'], ClientLanguageMap[client])
        print("response from Gtrans -> " + str(json['message']))
        socketio.emit('my response', json,room=SSIDmap[clients.index(client)], callback=messageReceived)

@socketio.on('client_language_mapping')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    SSIDmap.append(request.sid)
    clients.append(str(json['user_name']))
    ClientLanguageMap[str(json['user_name'])] = str(json['language'])
    print(str(json['user_name']) + " mapped to " + str(json['language']))
    socketio.emit('addme', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', debug=True)
