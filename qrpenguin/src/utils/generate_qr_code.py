import qrcode
"""
Function to create the QR code based on the string passed through
command line.

If there is no data, fail and error.

Parameters:
data (string): Data based to encode
file_path (string): Location to drop the file
"""

def generate_qr_code(data, file_path):
    if not data:
        raise ValueError("Error, no QR Made. Input field cannot be blank.")
   
    img = qrcode.make(data)
    img.save(file_path)
    print("Code created successfully!.")