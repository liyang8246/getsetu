import requests
import os
import time

def getimg(i):
    html = requests.get(url, headers=ua)
    img_url = html.url
    img_path = folder_path + str(i) + ".jpg"
    img = requests.get(img_url, headers=ua)
    with open(img_path, "wb") as f:
        f.write(img.content)
        f.flush()
    f.close()
    print(str(i) + ".jpg" + " done!")
    return i

url = "https://iw233.cn/API/Random.php"
ua = {'user-agent': "Mozilla/5.0 (Windows NT 10.0Win64x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
folder_path = ".\\image\\"
if os.path.exists(folder_path) == False:
    os.makedirs(folder_path)
    start = 0
else:
    list = os.listdir(".\\image")
    list = [int(i[:-4]) for i in list]
    start = max(list) + 1

for i in range(start,4000):
    try:
        getimg(i)
    except Exception as e:
        print(e)
        time.sleep(1)

print("All Complete !")