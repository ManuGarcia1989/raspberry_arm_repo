import RPi.GPIO as GPIO
import serial

def init():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    global arduino
    global distancias
    global posicion_origen
    global posicion_final
    global posicion_new
    global microPausa
    global cont
    
    with open('set_point.txt',"r") as file:
        list_data = list()
        for line in file:
            list_data.append(int(line))
    
    arduino = serial.Serial('/dev/ttyACM0', 115200)
    distancias = [0,6,12,18,24,30,36,42,48,54]

    posicion_origen = list_data[0]
    posicion_final = list_data[1]
    posicion_new = posicion_origen
    microPausa = 0.3
    cont = 0
    
    global SENSOR_1
    global SENSOR_2
    global SENSOR_3
    global SENSOR_4
    global SENSOR_5
    global SENSOR_6
    global SENSOR_7
    global SENSOR_8
    global SENSOR_9
    global SENSOR_10
    
    SENSOR_1 = 13
    SENSOR_2 = 6
    SENSOR_3 = 5
    SENSOR_4 = 11
    SENSOR_5 = 9
    SENSOR_6 = 10
    SENSOR_7 = 22
    SENSOR_8 = 27
    SENSOR_9 = 17
    SENSOR_10 = 4
    
    GPIO.setup(SENSOR_1, GPIO.IN)
    GPIO.setup(SENSOR_2, GPIO.IN)
    GPIO.setup(SENSOR_3, GPIO.IN)
    GPIO.setup(SENSOR_4, GPIO.IN)
    GPIO.setup(SENSOR_5, GPIO.IN)
    GPIO.setup(SENSOR_6, GPIO.IN)
    GPIO.setup(SENSOR_7, GPIO.IN)
    GPIO.setup(SENSOR_8, GPIO.IN)
    GPIO.setup(SENSOR_9, GPIO.IN)
    GPIO.setup(SENSOR_10, GPIO.IN)
    
    comando = "<" + str(posicion_origen) + ">"
    arduino.write(comando.encode())
    posicion_new = posicion_origen
    arduino.close()
    arduino = serial.Serial('/dev/ttyACM0', 115200)