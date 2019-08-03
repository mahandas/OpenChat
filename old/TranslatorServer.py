from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_socketio import SocketIO
import GtransWrapper as GTW

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
clientsSSImap = {}
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
    del clientsSSImap[str(json['user_name'])]
    del ClientLanguageMap[str(json['user_name'])]
    
@socketio.on('ChatProcessing')
def handle_my_chat_event(json, methods=['GET', 'POST']):
    global clientsSSImap
    global ClientLanguageMap
    print('received my event: ' + str(json))
    clientsSSImap[str(json['user_name'])] = request.sid
    for key, value in clientsSSImap.items():
        #json['message'] = GTW.tanslatedata(json['message'], ClientLanguageMap[key])
        print("response from Gtrans -> " + str(json['message']))
        socketio.emit('my response', json,room=value, callback=messageReceived)

@socketio.on('client_language_mapping')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    global clientsSSImap
    global ClientLanguageMap
    print('received my event: ' + str(json))
    clientsSSImap[str(json['user_name'])] = request.sid
    ClientLanguageMap[str(json['user_name'])] = str(json['language'])
    print(str(json['user_name']) + " mapped to " + str(json['language']))
    socketio.emit('addme', json, callback=messageReceived)

@socketio.on('Client_Session_Mapper')
def ClientSessionMappper(json, methods=['GET', 'POST']):
    clientsSSImap[str(json['user_name'])] = request.sid
    
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', debug=True)
