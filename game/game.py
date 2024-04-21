import easyocr


def extract_text(image_path, languages=['en']):
    """
    Extract text from an image using easyocr.

    Args:
    - image_path (str): The path to the image file.
    - languages (list): A list of language codes to use for OCR. Default is English.

    Returns:
    - result (list): A list of tuples containing the detected text and its bounding box coordinates.
    """
    # Initialize the reader
    reader = easyocr.Reader(languages)

    # Read text from the image
    result = reader.readtext(image_path)

    return result


def main():
    # Prompt user for image file path
    image_path = input("Enter the path to the image file: ")

    # Extract text from the image
    text_result = extract_text(image_path)

    # Print the extracted text
    if text_result:
        print("Extracted text:")
        for detection in text_result:
            print(detection[1])  # Print the detected text
    else:
        print("No text detected in the image.")


if __name__ == "__main__":
    main()
