import requests

def postX(hostIP, CID, UID, file_path):
    """
    Function to upload competitor-generated receiver software.

    Parameters:
    - hostIP (str): the IP address of the host
    - CID (str): channel ID
    - UID (str): user ID
    - file_path (str): the path to the file to upload

    Returns:
    - True if the file was uploaded successfully, False otherwise.
    """
    with open(file_path, 'rb') as file:
        file_data = file.read()
    files = {'file': file_data}
    url = f"{hostIP}/postX.php?CID={CID}&UID={UID}"
    response = requests.post(url, files=files)
    if response.status_code == 200:
        return True
    else:
        return False