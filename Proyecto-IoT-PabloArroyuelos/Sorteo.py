import requests
import random

api_key = 'PFO57L8J0NCC18IH'
channel_id = '2393608'
field1 = 'barik_N'
url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}&results=20'

try:
    response = requests.get(url)
    data = response.json()

    if 'feeds' in data:
        barik_participations = {}

        for entry in data['feeds']:
            barik_number = entry['field1']

            if barik_number not in barik_participations:
                barik_participations[barik_number] = 1
            else:
                barik_participations[barik_number] += 1

        total_participations = sum(barik_participations.values())


        cumulative_probabilities = {}
        cumulative_probability = 0
        for barik_number, participations in barik_participations.items():
            probability = participations / total_participations
            cumulative_probability += probability
            cumulative_probabilities[barik_number] = cumulative_probability


        random_number = random.uniform(0, 1)
        winner = None
        for barik_number, probability in cumulative_probabilities.items():
            if random_number <= probability:
                winner = barik_number
                break
	
        print('Datos de participaciones por Barik:')
        for barik_number, participations in barik_participations.items():
            print(f'Barik_{barik_number}: {participations} participaciones ({(participations / total_participations) * 100:.2f}%)')

        print('\n¡Ganador del sorteo!')
        print(f'Barik_{winner} es el ganador con {barik_participations[winner]} participaciones.')

    else:
        print('No se encontraron datos en el canal de ThingSpeak.')

except Exception as e:
    print(f'Error al obtener datos de ThingSpeak: {e}')


