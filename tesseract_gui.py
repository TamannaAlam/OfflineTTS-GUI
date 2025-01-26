from gooey import Gooey, GooeyParser
import subprocess

@Gooey(program_name="Offline TTS", language='english', default_size=(800, 600))
def main():
    parser = GooeyParser(description="Tesseract OCR Options")

    # Input file
    parser.add_argument(
        "Input_File",
        help="Select the image file for OCR processing",
        widget="FileChooser"
    )

    # Output file
    parser.add_argument(
        "Output_File",
        help="Specify the base name for the output file (no extension)",
        widget="FileSaver",
        default="output"
    )

    # Language
    parser.add_argument(
        "-l", "--Language",
        choices=["English", "Japanese"],  
        help="Select OCR language (default is English)",
        default="eng"
    )

    # OEM mode
    parser.add_argument(
        "-oem", "--Engine_Mode",
        choices=["0 - Legacy", "1 - LSTM", "2 - Combined", "3 - Default"],
        help="OCR Engine Mode",
        default="3 - Default"
    )

    # Output format
    parser.add_argument(
        "-f", "--Format",
        choices=["txt", "hocr", "pdf", "tsv"],
        help="Specify the output file format",
        default="txt"
    )

    args = parser.parse_args()

    # Build the Tesseract command
    input_file = args.Input_File
    output_file = args.Output_File
    language = args.Language
    engine_mode = args.Engine_Mode.split(" - ")[0]
    format_option = args.Format

    # Run Tesseract command
    command = [
        "tesseract",
        input_file,
        output_file,
        "-l", language,
        "--oem", engine_mode,
        format_option
    ]

    try:
        # Execute Tesseract command
        subprocess.run(command, check=True)
        print(f"Success! Output saved to: {output_file}.{format_option}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
