from urllib.request import urlretrieve
# urllib.request = Python Package
# urlretrieve = function of the package / will download the image

link=input('Image download link: ')
fileName=input('File Name: ')

urlretrieve(link,'image/'+fileName+'.jpg')




