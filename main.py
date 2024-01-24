
import qrcode


qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=5,border=1)
data="https://github.com/SarthakGangwar17"
qr.add_data(data)
qr.make(fit=True)

img=qr.make_image(fill_color='black',back_color='white')

img.save("qr.png")
img.show()