import pyqrcode
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"

url = pyqrcode.create(s)

url.svg("qrcode.svg", scale=8)
