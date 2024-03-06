import qrcode
from PIL import Image

# Function to generate QR code and save image
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# QR codes from adonix.hackillinois.org/shop/item/qr/:ITEMID
qrInfo = []

for i in range(len(qrInfo)):
    data = f"QR Code {qrInfo[i]}"
    filename = f"qrcode_{i}.png"
    generate_qr_code(data, filename)

print("QR codes generated successfully.")
