import requests

def getX(hostIP, CID, UID):
    """
    Function to download competitor-generated receiver software.

    Parameters:
    - hostIP (str): the IP address of the host
    - CID (str): channel ID
    - UID (str): user ID

    Returns:
    - The content of the downloaded file (str).
    """
    url = f"{hostIP}/getX.php?CID={CID}&UID={UID}"
    response = requests.get(url)
    return response.content.decode('utf-8')

