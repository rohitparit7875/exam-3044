import qrcode

text = input("Enter text or URL to create QR code: ")

qr = qrcode.make(text)
qr.save("my_qr.png")

print("QR Code generated as my_qr.png ✔")
