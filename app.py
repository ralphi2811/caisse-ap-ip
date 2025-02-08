from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import subprocess
import threading
import sys
from queue import Queue
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def enqueue_output(out, queue):
    for line in iter(out.readline, ''):
        queue.put(line)
    out.close()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('start_server')
def handle_server_start(data):
    try:
        # Arrêter le serveur précédent s'il existe
        if hasattr(handle_server_start, 'process'):
            handle_server_start.process.terminate()
            handle_server_start.thread.join()

        # Démarrer le serveur
        cmd = [
            'python3', 
            'caisse_ap_ip_server.py',
            '--port', str(data.get('port', 8888)),
            '--payment-type', data.get('payment_type', 'cbcontact'),
        ]
        
        if data.get('failure'):
            cmd.extend(['--failure', '--failure-type', data.get('failure_type', 'abandon')])
        
        if data.get('duration'):
            cmd.extend(['--duration', str(data.get('duration'))])
            
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # Rediriger stderr vers stdout
            bufsize=1,
            universal_newlines=True
        )
        
        # Stocker le processus pour pouvoir l'arrêter plus tard
        handle_server_start.process = process

        q = Queue()
        t = threading.Thread(target=enqueue_output, args=(process.stdout, q))
        t.daemon = True
        t.start()

        # Stocker le thread pour pouvoir le joindre plus tard
        handle_server_start.thread = t

        emit('server_output', {'data': 'Serveur démarré sur le port ' + str(data.get('port', 8888))})
        
        def read_output():
            while True:
                try:
                    # Vérifier si le processus est toujours en cours
                    if process.poll() is not None:
                        break
                    
                    try:
                        line = q.get_nowait()
                        socketio.emit('server_output', {'data': line.strip()})
                    except:
                        socketio.sleep(0.1)
                except Exception as e:
                    print(f"Erreur de lecture: {str(e)}")
                    break

        # Démarrer un thread pour la lecture continue
        output_thread = threading.Thread(target=read_output)
        output_thread.daemon = True
        output_thread.start()

    except Exception as e:
        emit('server_output', {'data': f'Erreur: {str(e)}'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
