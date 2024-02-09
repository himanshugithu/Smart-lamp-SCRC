import requests

def onem2m_get_request(url, headers=None):
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("GET request successful!")
        return response.json()  # Assuming the response is JSON data
    else:
        print(f"GET request failed with status code: {response.status_code}")
        return None

# Example usage:
resource_url = "https://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SR/SR-AQ/SR-AQ-KH95-00/Data/la"
headers = {"X-M2M-Origin":"iiith_guest:iiith_guest", "Content-Type": "application/json"}
response_data = onem2m_get_request(resource_url, headers)
con_value =response_data['m2m:cin']['con'].split(',')

print(con_value)
print(con_value[2])