import boto3
from pypdf import PdfReader
import sys
import textwrap


def pdf_to_speech(pdf_path, output_mp3_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        if not text.strip():
            print("Error: No text could be extracted from the PDF.")
            return

        polly_client = boto3.client("polly")

        chunks = textwrap.wrap(text, 3000)

        with open(output_mp3_path, "wb") as f:
            for chunk in chunks:
                response = polly_client.synthesize_speech(
                    Text=chunk,
                    OutputFormat="mp3",
                    VoiceId="Joanna"
                )
                with response["AudioStream"] as stream:
                    f.write(stream.read())

        print(f"Successfully converted '{pdf_path}' to '{output_mp3_path}'")

    except FileNotFoundError:
        print(f"Error: The file '{pdf_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_speech.py <path_to_pdf> <output_mp3_filename>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    mp3_file = sys.argv[2]
    pdf_to_speech(pdf_file, mp3_file)
