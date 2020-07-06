
key = '06d38de3c75a51c8a59502c50884b828'

#url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid='+key













































import requests

city = input('Enter City:').strip()

url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid='+key


res = requests.get(url).json()

#print(res)


#print('coords:',res['coord'])


print('Country:',res['sys']['country'])
print('City:',res['name'])
print('Longitude:',res['coord']['lon'])
print('Lotitude:',res['coord']['lat'])

print('Temperature:',res['main']['temp'],'C')
print('Min.Temp:',res['main']['temp_min'],'C')
print('Max.Temp:',res['main']['temp_max'],'C')
print('Humidity:',res['main']['humidity'])
print('Pressure:',res['main']['pressure'])

