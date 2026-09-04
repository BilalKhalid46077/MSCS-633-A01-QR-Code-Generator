# QR Code Generator
# This program asks the user to enter a URL and then generates a QR code for that URL.

# The QR code is saved as an image file called "qr_code.png".

# Bilal Khalid
# Artificial Intelligence

# The qrcode library is used to create QR codes.
# We installed this library using:
# pip install qrcode[pil]

import qrcode

# The re module is used for a simple check to make sure
# the user has entered something that looks like a URL.
import re


def is_valid_url(url):
    # This function performs a basic validation of the URL.

    # This regular expression checks whether the URL starts
    # with either http:// or https://.

    url_pattern = re.compile(
        r"^https?://"
        r"(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}"
        r"|localhost"
        r"|(\d{1,3}\.){3}\d{1,3})"
        r"(:\d+)?"
        r"(/.*)?$"
    )

    # Return True if the URL matches the pattern.
    # Otherwise, return False.

    return bool(url_pattern.match(url))


def generate_qr_code(url):
    # This function creates the QR code for the URL entered by the user.

    # Create a QRCode object.
    # version controls the size of the QR code.
    # A higher error correction level makes the QR code
    # more readable even if a small part is damaged.

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    # Add the URL to the QR code.

    qr.add_data(url)

    # This automatically determines the best QR code size
    # based on the amount of information we added.

    qr.make(fit=True)

    # Create the actual QR code image.
    # The default colors are black and white, which makes
    # the QR code easy for most QR scanners to read.

    qr_image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    # Save the generated QR code as a PNG image.

    output_file = "qr_code.png"
    qr_image.save(output_file)

    # Return the filename so that the main program
    # can tell the user where the image was saved.

    return output_file


def main():
    # This is the main function of the application.

    # It displays the application title, asks the user for a URL,
    # validates the input, and generates the QR code.

    # Display a simple heading for the application.

    print("=" * 50)
    print("              QR CODE GENERATOR")
    print("=" * 50)

    print("\nThis program creates a QR code from a website URL.")
    print("Example: https://www.bioxsystems.com/")

    # Ask the user to enter the URL.

    url = input("\nEnter the URL: ").strip()

    # Check whether the user entered anything.

    if not url:
        print("\nError: You did not enter a URL.")
        return

    # Perform our basic URL validation.

    if not is_valid_url(url):
        print("\nError: Please enter a valid URL.")
        print("The URL should start with http:// or https://")
        return

    # Tell the user that the program is working.

    print("\nGenerating QR code...")

    try:
        # Call the function that generates and saves
        # the QR code image.

        output_file = generate_qr_code(url)

        # Tell the user that everything worked.

        print("\nQR code generated successfully!")
        print(f"URL: {url}")
        print(f"QR code saved as: {output_file}")

        print("\nYou can now scan the QR code using a phone.")

    except Exception as error:
        # This handles unexpected problems while generating
        # or saving the QR code.

        print("\nSomething went wrong while generating the QR code.")
        print(f"Error details: {error}")

    # Print a closing line to make the output look cleaner.

    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()