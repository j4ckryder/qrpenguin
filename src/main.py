import argparse
import os
from utils.generate_qr_code import generate_qr_code  # generate_qr_code function

def main():
    parser = argparse.ArgumentParser(description="QR Code Generator CLI")
    parser.add_argument('--txt', required=True, help='Data to encode in the QR code')

    args = parser.parse_args()


    # DQC - no input
    if args.txt:
        data = args.txt
    else:
        data = input("Error: Please enter text to encode: ")

    output_file = "qr_code.png"
    output_path = os.path.join(os.getcwd(), output_file)

  
# Makes the magic happen
    try:
        generate_qr_code(data, output_file)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
