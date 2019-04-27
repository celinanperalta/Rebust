from clarifai.rest import ClarifaiApp
import json

app = ClarifaiApp(api_key='efac6c485194474790aa9732ed895aa2')
model = app.public_models.general_model
response = model.predict_by_url('https://samples.clarifai.com/metro-north.jpg')
results = response["outputs"][0]["data"]["concepts"]
for i in results:
    print(i["name"])
    print(i["value"])