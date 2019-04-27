from datamuse import datamuse



api = datamuse.Datamuse()

arr = []

str = input("Enter text or img({image_name}): ")

while str != "-1":
    word = []
    word.append(str)
    str = input("Enter text or img({image_name}): ")
    while str != -2:
        word.append(str)
        str = input("Enter text or img({image_name}): ")
    arr.append(word)

print(arr)
