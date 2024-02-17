from tkinter import *
from PIL import ImageTk, Image
import requests
import datetime


def onem2m_get_request(url, headers=None):
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("GET request successful!")
        return response.json()  # Assuming the response is JSON data
    else:
        print(f"GET request failed with status code: {response.status_code}")
        return None
    

def update_sensor_data():
    global temp_value_label, humidity_value_label, time_value_label, day_value_label, co2_value_label
    
    resource_url = "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-SR/SR-AQ/SR-AQ-KH95-00/Data/la"
    headers = {"X-M2M-Origin":"iiith_guest:iiith_guest", "Content-Type": "application/json"}
    response_data = onem2m_get_request(resource_url, headers)
    if response_data:
        con_value = response_data['m2m:cin']['con'].split(',')
        
        # Update temperature value
        temp_value_label.config(text=f"{str(con_value[2])} \u00b0C")
        
        # Update humidity value
        humidity_value_label.config(text=f"{str(con_value[3][:-1])} %")
        
        # Update CO2 value
        co2_value_label.config(text=f"{str(con_value[1])} ppm ")
    
    # Get the current day and time
    current_datetime = datetime.datetime.now()
    current_day = current_datetime.strftime("%A")
    current_time = current_datetime.strftime("%H:%M:%S")
    day_value_label.config(text=current_day)
    time_value_label.config(text=current_time)
    root.after(1000, update_sensor_data)


root = Tk()
root.title('Sensor Data')
root.geometry('750x750')
root.configure(background='#0A0A0A')

# Add label for "Welcome to"
welcome_label = Label(root, text="WELCOME TO", fg='white', bg='#0A0A0A', font=('Amasis MT Pro Black', 30, 'bold'))
welcome_label.pack(pady=20)

# Load logo image
logo_img = ImageTk.PhotoImage(Image.open(r"smartCity_livingLab.png").resize((200, 200)))
logo_label = Label(root, image=logo_img, bg='#0A0A0A')
logo_label.pack(pady=(20, 10))

# Frame to hold the readings
readings_frame = Frame(root, bg='#0A0A0A')
readings_frame.pack(pady=(0,0))

# Load images for the visual indicators
temp_img = ImageTk.PhotoImage(Image.open(r"temperature_icon3.png").resize((70, 70)))
humidity_img = ImageTk.PhotoImage(Image.open(r"humidity_icon2.png").resize((70, 70)))
time_img = ImageTk.PhotoImage(Image.open(r"time_icon2.png").resize((70, 70)))
day_img = ImageTk.PhotoImage(Image.open(r"day_icon.png").resize((70, 70)))
co2_img = ImageTk.PhotoImage(Image.open(r"co2_icon2.png").resize((70, 70)))

# Create labels for each visual indicator
temp_label = Label(readings_frame, image=temp_img, bg='#0A0A0A')
temp_label.grid(row=0, column=0, padx=(0, 100))  # Increased padx between icons
temp_value_label = Label(readings_frame, text="", fg='white', bg='#0A0A0A', font=('Arial', 12, 'bold'))
temp_value_label.grid(row=1, column=0, padx=(0, 110),pady=(0,100))

humidity_label = Label(readings_frame, image=humidity_img, bg='#0A0A0A')
humidity_label.grid(row=0, column=4, padx=(10,0))  # Increased padx between icons
humidity_value_label = Label(readings_frame, fg='white', bg='#0A0A0A', font=('Arial', 12, 'bold'))
humidity_value_label.grid(row=1, column=4, padx=(15,0),pady=(0,100))

time_label = Label(readings_frame, image=time_img, bg='#0A0A0A')
time_label.grid(row=2, column=0, padx=(0, 100))
time_value_label = Label(readings_frame, fg='white', bg='#0A0A0A', font=('Arial', 12, 'bold'))
time_value_label.grid(row=3, column=0, padx=(0, 100))

day_label = Label(readings_frame, image=day_img, bg='#0A0A0A')
day_label.grid(row=2, column=4, padx=(10,0))
day_value_label = Label(readings_frame, text="", fg='white', bg='#0A0A0A', font=('Arial', 12, 'bold'))
day_value_label.grid(row=3, column=4, padx=(10,0))

co2_label = Label(readings_frame, image=co2_img, bg='#0A0A0A')
co2_label.grid(row=1, column=3, padx=(0,100))
co2_value_label = Label(readings_frame, text=" ppm ", fg='white', bg='#0A0A0A', font=('Arial', 12, 'bold'))
co2_value_label.grid(row=1, column=3, padx=(0,100),pady=(100,1.5))

# Start the data update process
update_sensor_data()

root.mainloop()