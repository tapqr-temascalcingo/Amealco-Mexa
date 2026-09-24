import qrcode

# URL de tu página
url = "https://tapqr-temascalcingo.github.io/Amealco-Mexa/"

# Crear el QR con fondo blanco y patrón negro
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Generar imagen (negro puro sobre blanco)
img = qr.make_image(fill_color="black", back_color="white")

# Guardar
img.save("qr_mexa.png")

print("✅ QR generado: qr_mexa.png")