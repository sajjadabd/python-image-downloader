import requests
from tqdm import tqdm

URL = "http://172.16.32.4:83/Content/Upload/User/"
extension = ".jpg"

start = 6200
end = 6290
tTotal = end - start

"""
id = start
pbar = tqdm(total=tTotal)
while id < end :
    eachURL = URL + str(id) + extension
    response = requests.get(eachURL)
    open( str(id) + ".jpg", "wb").write(response.content)
    pbar.update( start-end / tTotal )
    id +=1 
pbar.close()
"""


for i in tqdm(range(start,end)):
    eachURL = URL + str(i) + extension
    response = requests.get(eachURL)
    open( str(i) + ".jpg", "wb").write(response.content)
    


