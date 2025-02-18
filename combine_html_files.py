import os
import requests

# Define the raw GitHub URL prefix
GITHUB_RAW_URL_PREFIX = "https://raw.githubusercontent.com/pxrocentral/soupcan/main/"

def find_html_files(root_dir):
    html_files = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                relative_path = os.path.relpath(os.path.join(subdir, file), root_dir)
                html_files.append(relative_path)
    return html_files

def fetch_file_content(file_path):
    url = GITHUB_RAW_URL_PREFIX + file_path
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def write_combined_html(html_files, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n")
        file.write("<meta charset='UTF-8'>\n<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
        file.write("<title>Combined Page</title>\n<link rel='stylesheet' href='styles.css'>\n</head>\n<body>\n")
        file.write("<nav>\n<ul>\n")

        for index, html_file in enumerate(html_files):
            section_id = f"section{index + 1}"
            file.write(f"<li><a href='#{section_id}'>Section {index + 1}</a></li>\n")

        file.write("</ul>\n</nav>\n")

        for index, html_file in enumerate(html_files):
            section_id = f"section{index + 1}"
            file.write(f"<section id='{section_id}'>\n")
            file.write(fetch_file_content(html_file))
            file.write("\n</section>\n")

        file.write("</body>\n</html>")

def main():
    root_dir = '.'  # Root directory of the repository
    output_file = 'combined.html'  # Output file
    html_files = find_html_files(root_dir)
    write_combined_html(html_files, output_file)
    print(f"Combined HTML file created: {output_file}")

if __name__ == "__main__":
    main()
