#G1D4MLT0UT32D5UU
import requests
import RPi.GPIO as GPIO
import time
from datetime import datetime

api_key = 'G1D4MLT0UT32D5UU'
url = f'https://api.thingspeak.com/update?api_key={api_key}'

PIN_BOTON = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_BOTON, GPIO.IN)


barik_seleccionada = 0
registrando = False
tiempo_pulsacion_1 = None
tiempo_pulsacion_2 = None
contador = 0
barik_seleccionada=input("Introduce el numero de tu barik y luego pulsa el boton: ")
try:
    while True:    

        
        estado_boton = GPIO.input(PIN_BOTON)

        if estado_boton == True:
            if contador == 0:
                print(f'Iniciando el registro para Barik_{barik_seleccionada}...')
                registrando = True
                tiempo_pulsacion_1 = datetime.now()
                contador += 1

            elif contador == 1:
                tiempo_pulsacion_2 = datetime.now()
                tiempo_transcurrido = tiempo_pulsacion_2 - tiempo_pulsacion_1

                
                response = requests.get(f'{url}&field1={barik_seleccionada}&field2={tiempo_pulsacion_1}&field3={tiempo_pulsacion_2}&field4={tiempo_transcurrido.total_seconds()}')



                if response.status_code == 200:
                    print('Datos enviados a ThingSpeak.')

                print(f'Deteniendo el registro para Barik_{barik_seleccionada}...')
               
                print(f'Barik seleccionada: {barik_seleccionada}\n')
                print(f'Primera pulsacion: {tiempo_pulsacion_1}\n')
                print(f'Segunda pulsacion: {tiempo_pulsacion_2}\n')
                print(f'Tiempo: {tiempo_transcurrido.total_seconds()}\n')

                contador = 0
                tiempo_pulsacion_1 = None
                tiempo_pulsacion_2 = None
                

        time.sleep(0.3)

except KeyboardInterrupt:
    GPIO.cleanup()




