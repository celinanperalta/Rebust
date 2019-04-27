from rebust import Rebust

rebust = Rebust()

# img = input("Enter URL or image path: ")
# type = "url"
# res = rebust.get_image_predictions(img, type)

rebus1 = [[("url", "https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fyesofcorsa.com%2Fwp-content%2Fuploads%2F2017%2F01%2FAfter-Rain-Wallpaper-Download.jpg&f=1"), ("url", "https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.favourthis.co.uk%2Fwp-content%2Fuploads%2F2015%2F07%2F12-Red-Self-Adhesive-Bows.jpg&f=1")]]
rebus2 = [[("str", "q"), ("str", "c"), ("url", "https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F5%2F50%2FSnare_drum_-_Vladimir_Morozov.jpg%2F1200px-Snare_drum_-_Vladimir_Morozov.jpg&f=1"), ("str", "b"), ("url", "https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2F3.bp.blogspot.com%2F-GzjqhZpG05w%2FT_I1B_cQ7HI%2FAAAAAAAAAkU%2FRcx1PJwg3L8%2Fs1600%2Fclip_art_toilet_women.gif&f=1")]]

print(rebust.solve_word(rebus2[0]))


# rebust.get_sounds_like("q c drum b her")
# rebust.get_sounds_like("raincandy")
