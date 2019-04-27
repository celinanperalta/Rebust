from rebust import Rebust

rebust = Rebust()

img = input("Enter URL or image path: ")

res = rebust.get_image_predictions(img)

for i in res:
    print(i)
