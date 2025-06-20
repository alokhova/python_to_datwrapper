import requests
import json

#requesting data
headers = {
    'Authorization': 'Bearer <YOUR_TOKEN_HERE>',
    'content-type': 'application/json'
}
 getResponse = requests.get('https://api.datawrapper.de/v3/me', headers=headers)
 print('getResponse: ' + str(getResponse.text))


#creating a chart
data = json.dumps({
    'title': 'Average share of green area in German cities',
    'type': 'multiple-lines'
})
postResponse = requests.post('https://api.datawrapper.de/v3/charts', headers=headers, data=data)
print('postResponse: ' + str(postResponse.text))


#uploading data
headers = {
    'Authorization': 'Bearer <YOUR_TOKEN_HERE>',
    'content-type': 'text/csv'
}
data = '''Year, München, Oldenburg, Hamburg, Bremen, Karlsruhe, Halle
1990, 36.86, 31.79, 36.70, 29.24, 9.29, 5.29 
2000, 29.92, 33.00, 34.50, 22.95, 12.72, 8.45 
2010, 23.64, 30.75, 32.36, 19.54, 14.13, 10.30 
2020, 29.68, 29.33, 26.50, 20.98, 16.75, 11.61'''

putResponse = requests.put('https://api.datawrapper.de/v3/charts/<YOUR_CHART_ID_HERE/data', headers=headers, data=str(data))
print('putResponse: ' + str(putResponse.text))


#edit colours
headers = {
    'Authorization': 'Bearer <YOUR_TOKEN_HERE>',
    'accept': '*/*',
    'content-type': 'application/json'
}
data = json.dumps({'metadata': {'visualize':{'base-color': 5,
                                 'label-colors': True
                                 }
                            }
})
        
patchResponse = requests.patch('https://api.datawrapper.de/v3/charts/<YOUR_CHART_ID_HERE>', headers=headers, data=data)
