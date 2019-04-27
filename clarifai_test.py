from rebust import Rebust

rebust = Rebust()

# img = input("Enter URL or image path: ")
# type = "url"
# res = rebust.get_image_predictions(img, type)

rebus1 = [[("img", ("url", "https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fyesofcorsa.com%2Fwp-content%2Fuploads%2F2017%2F01%2FAfter-Rain-Wallpaper-Download.jpg&f=1")), ("img", ("url", "https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.favourthis.co.uk%2Fwp-content%2Fuploads%2F2015%2F07%2F12-Red-Self-Adhesive-Bows.jpg&f=1"))]]


print(rebust.solve_word(rebus1[0]))

# rebust.get_sounds_like("q c drum b her")
# rebust.get_sounds_like("raincandy")
