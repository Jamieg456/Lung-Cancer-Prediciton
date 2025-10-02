import os
import requests
import zipfile
import shutil

def find_repo_root():
    """
    Dynamically finds repository root folder.
    assumes root folder contains a .git folder or a README file.
    """
    current_path = os.path.abspath(os.path.dirname(__file__))
    while True:
        # look for a .git folder or a README.md file
        if os.path.exists(os.path.join(current_path, ".git")) or os.path.exists(os.path.join(current_path, "README.md")):
            return current_path
        parent_path = os.path.dirname(current_path)
        if parent_path == current_path:
            raise FileNotFoundError("Could not find the repository root containing a .git folder or README.md file.")
        current_path = parent_path

def is_dataset_downloaded(dest_folder):
    """
    Checks if the dataset (test, train, valid folders) already exist in the data folder.
    """
    required_folders = ["test", "train", "valid"]
    return all(os.path.exists(os.path.join(dest_folder, folder)) for folder in required_folders)

def download_and_extract(url, temp_folder, dest_folder):
    """
    Downloads and extracts a ZIP file from the provided URL into the specified folder.
    """
    # ensure temporary folder exists
    os.makedirs(temp_folder, exist_ok=True)

    # defines the path for the ZIP file
    zip_path = os.path.join(temp_folder, "dataset.zip")

    # downloads the file
    print(f"Downloading dataset from {url}...")
    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Raise an error for bad responses
        with open(zip_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    print(f"Download completed: {zip_path}")

    # Extract the ZIP file to the temp folder
    print("Extracting dataset...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(temp_folder)
    print(f"Dataset extracted to temporary folder: {temp_folder}")

    # navigate to the 'data/' folder within the extracted contents
    extracted_data_path = os.path.join(temp_folder, "data")
    if not os.path.exists(extracted_data_path):
        print(f"Error: 'data' folder not found inside the ZIP file.")
        return

    # move folders (test, train, valid) to the destination folder
    for folder_name in ["test", "train", "valid"]:
        src_path = os.path.join(extracted_data_path, folder_name)
        dest_path = os.path.join(dest_folder, folder_name)
        if os.path.exists(src_path):
            # If the destination folder already exists, merge the contents
            if os.path.exists(dest_path):
                for item in os.listdir(src_path):
                    shutil.move(os.path.join(src_path, item), dest_path)
            else:
                shutil.move(src_path, dest_path)
            print(f"Moved {folder_name} to {dest_folder}")

    # Clean up
    os.remove(zip_path)
    shutil.rmtree(temp_folder)
    print("Temporary files removed.")

def download_dataset():
    """
    Main function to check and download the dataset if not already available.
    """
    # Dropbox direct download link
    DROPBOX_URL = "https://www.dropbox.com/scl/fi/ebmx490nbca2ip69ypote/Data.zip?rlkey=fj622hr2m984pqcvn733l0ykq&st=iclast8b&dl=1"

    # Paths: temporary extraction folder and repo's data folder
    REPO_ROOT = find_repo_root()
    TEMP_FOLDER = os.path.join(REPO_ROOT, "temp_data")
    DEST_FOLDER = os.path.join(REPO_ROOT, "data")

    # Check if the dataset already exists
    if is_dataset_downloaded(DEST_FOLDER):
        print("Dataset already exists. Skipping download.")
        return

    # Ensure the destination folder exists (create it if necessary)
    if not os.path.exists(DEST_FOLDER):
        print(f"The destination folder '{DEST_FOLDER}' does not exist. Creating it now.")
        os.makedirs(DEST_FOLDER)

    # Download and extract the dataset
    download_and_extract(DROPBOX_URL, TEMP_FOLDER, DEST_FOLDER)

if __name__ == "__main__":
    download_dataset()
