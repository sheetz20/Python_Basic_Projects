import pyqrcode
# from pyqrcode import QRCode

url = "https://www.youtube.com/channel/UCBw617gTVLp5GtEWDb18u5Q"

fileName = pyqrcode.create(url)

fileName.svg("C://Users/sheetal/Desktop/Python/Git_Hub/myyoutube.svg", scale=8)