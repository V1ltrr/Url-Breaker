# Url Breaker

## Description

**url-breaker** is a lightweight Python tool designed to perform URL fuzzing.  
It automatically generates various "broken" or modified variants of a target URL and tests each one to identify unexpected behaviors or potential server-side vulnerabilities.

This tool is particularly useful for web security testing, allowing you to verify if certain paths or URL variants not intended by the application are accessible or produce different responses.

## Key Features
- Automatic generation of URL variants including encodings, special sequences, path manipulations, and more.  
- Support for a custom wordlist (`wordlist.txt`) to test additional variants.  
- Sends HTTP requests to each variant and displays the HTTP status code.  
- Colorized terminal output for easier result interpretation.  
- Robust error handling to prevent process interruptions due to network issues.  
- Interactive console interface with usage mode selection.

## Requirements
- Python 3.6 or higher  
- Python packages:
  - `requests`  
  - `colorama`

## Installation
1. Clone the repository or download the source files :

```bash
git clone https://github.com/your-username/url-breaker.git
cd url-breaker
```
2. Install dependencies via pip :

```bash
git clone https://github.com/your-username/url-breaker.git
cd url-breaker
```
## Usage
Run the script by providing a base URL as an argument :
```bash
python url_breaker.py
```
### Steps
1. Select the fuzzing mode:  
   - Default built-in list  
   - Custom wordlist from `wordlist.txt`  
   - Exit the program

2. Enter the target URL:  
   - Must include the protocol (`http://` or `https://`)  
   - No spaces allowed  
   - Example: `https://example.com/admin`

3. The tool will test each URL variant and display a summary table with the HTTP status codes.
## wordlist.txt
- Optional: You can create a `wordlist.txt` file in the script directory.  
- Each line should contain a relative path to test (e.g., `admin`, `login`, `../../etc/passwd`).  
- The script reads these paths and uses them as URL variants.

## Project Structure

```text
url-breaker/
├── url_breaker.py       # Main script
├── wordlist.txt         # Optional custom variants file
├── README.md            # This documentation file
```

## Internal Details

- Uses `requests` for HTTP requests.  
- URL variants are built using `urllib.parse.urljoin` to ensure valid URLs.  
- Handles network exceptions gracefully.  
- Uses `colorama` for colored terminal output.  
- Interactive CLI with `print()` and `input()` for user interaction.

## Limitations and Future Work

- Current fuzzing is based on a static list; future improvements could include dynamic variant generation.  
- Adding multithreading or async requests to improve speed.  
- Content comparison to detect significant differences between responses.  
- Exporting results to CSV or JSON.  
- Supporting other HTTP methods like POST or PUT.

## Contributing

Contributions are welcome! To contribute :
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/your-feature`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push to the branch (`git push origin feature/your-feature`)  
5. Open a Pull Request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
