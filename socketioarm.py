import socketio
import settings

sio = socketio.Client()
sio.connect('http://192.168.1.8:3003')

settings.init()

def send_command_to_arduino(command):
    settings.arduino.write(command.encode())
    settings.arduino.flushInput()

@sio.on('machine-angle')
def set_machine_angle(data):
    settings.posicion_new = int(data['angle'])


@sio.on('machine-action')
def message_to_magneto(data):
    
    if data['action'] == 'drop_ball':
        print("Action: " + data['action'].replace("_"," "))
        drop_ball()
        
    if data['action'] == 'set_arm' :
        comando = "<" + str(settings.posicion_new) + ">"
        self.send_command_to_arduino(comando)
        self.mov_motor()



def drop_ball():
    comando = "<999>"
    self.send_command_to_arduino(comando)
    

@sio.on('set-point')
def message_to_set_point(data):
    settings.posicion_origen = data['set-point']
    comando = "<" + settings.posicion_origen + ">"
    self.send_command_to_arduino(comando)
    self.mov_motor_origen()


def mov_motor_origen(self):
        line = settings.arduino.readline()
        if line:
            line = line.decode('utf-8', 'strict')[:2]
            print(line)
            if line == 'ok':
                settings.posicion_new = settings.posicion_origen


def mov_motor(self):
        line = settings.arduino.readline()
        if line:
            line = line.decode('utf-8', 'strict')[:2]
            if line == 'ok':
                sio.emit('machine-to-web', {'arm-status': 'arm-ok'})
