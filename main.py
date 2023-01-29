from tkinter import *
# from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
import tkinter as tk
import os
from timezonefinder import TimezoneFinder
import requests
from datetime import datetime, timedelta
import pytz
from PIL import Image, ImageTk

# Color hex codes
colorBlue = "#1D71F2"
coloryWhite = "#C1E8FF"

root = Tk()
root.title("Weather Forecast App")
# root.wm_attributes("-transparent", colorOrange)
root.geometry("890x470+300+200")
root.configure(bg=colorBlue)
root.update()
root.resizable(False, False)

my_api = os.environ["weather_details_week"]
city_api = os.environ['current_weather_data']


def getweather():
    city = textfield.get().lower()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    lat = location.latitude
    lon = location.longitude

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    label_clock.config(text=current_time)

    # This api is used to extract country details
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + city + ",&appid=" + city_api
    api_link1 = requests.get(complete_api_link)
    api_data1 = api_link1.json()

    country = api_data1['sys']['country']
    city_details = f"{city.capitalize()}, {country}"
    timezone.config(text=city_details)

    #     Weather api (Actual)
    api_link = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(lat) + "&lon=" + str(lon) + "&units=metric" \
                                                                                                        "&exclude=hourly&appid=" + my_api
    api_data = requests.get(api_link).json()
    # print(api_data)

    # Current
    temp = api_data['current']['temp']
    weather_descpt = api_data['current']['weather'][0]['description']
    wind_spd = api_data['current']['wind_speed']
    hmdt = api_data['current']['humidity']
    pressure = api_data['current']['pressure']

    temp_t = f"{round(temp)}°C"
    t.config(text=temp_t)
    h.config(text=(hmdt, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind_spd, "m/s"))
    d.config(text=(weather_descpt.capitalize()))

    # days
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))

    #     Images
    main_day_image = api_data["daily"][0]['weather'][0]['icon']

    photo_main = ImageTk.PhotoImage(file=f"Weather icon set white/{main_day_image}.png")
    # print(main_day_image)
    main_image.config(image=photo_main)
    main_image.image = photo_main

    #     first day image
    first_day_img = api_data["daily"][0]['weather'][0]['icon']

    img = (Image.open(f"Weather icon set black/{first_day_img}.png"))
    resized_image = img.resize((70, 70))
    photo1 = ImageTk.PhotoImage(resized_image)
    first_image.config(image=photo1)
    first_image.image = photo1

    tempday1 = api_data['daily'][0]['temp']['day']
    despt1 = api_data['daily'][0]['weather'][0]['description']

    day1_temp.config(text=f"{round(tempday1)}°C")
    day1_desc.config(text=f"{despt1.capitalize()}")

    #     second day image
    second_day_img = api_data["daily"][1]['weather'][0]['icon']

    img = (Image.open(f"Weather icon set black/{second_day_img}.png"))
    resized_image = img.resize((70, 70))
    photo2 = ImageTk.PhotoImage(resized_image)
    second_image.config(image=photo2)
    second_image.image = photo2

    tempday2 = api_data['daily'][0]['temp']['day']
    despt2 = api_data['daily'][0]['weather'][0]['description']

    day2_temp.config(text=f"{round(tempday2)}°C")
    day2_desc.config(text=f"{despt2.capitalize()}")

    #     third day image
    third_day_img = api_data["daily"][2]['weather'][0]['icon']

    img = (Image.open(f"Weather icon set black/{third_day_img}.png"))
    resized_image = img.resize((70, 70))
    photo3 = ImageTk.PhotoImage(resized_image)
    third_image.config(image=photo3)
    third_image.image = photo3

    tempday3 = api_data['daily'][0]['temp']['day']
    despt3 = api_data['daily'][0]['weather'][0]['description']

    day3_temp.config(text=f"{round(tempday3)}°C")
    day3_desc.config(text=f"{despt3.capitalize()}")

    #     fourth day image
    fourth_day_img = api_data["daily"][3]['weather'][0]['icon']

    img = (Image.open(f"Weather icon set black/{fourth_day_img}.png"))
    resized_image = img.resize((70, 70))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourth_image.config(image=photo4)
    fourth_image.image = photo4

    tempday4 = api_data['daily'][3]['temp']['day']
    despt4 = api_data['daily'][3]['weather'][0]['description']

    day4_temp.config(text=f"{round(tempday4)}°C")
    day4_desc.config(text=f"{despt4.capitalize()}")

    #     fifth day image
    fifth_day_img = api_data["daily"][4]['weather'][0]['icon']

    img = (Image.open(f"Weather icon set black/{fifth_day_img}.png"))
    resized_image = img.resize((70, 70))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifth_image.config(image=photo5)
    fifth_image.image = photo5

    tempday5 = api_data['daily'][4]['temp']['day']
    despt5 = api_data['daily'][4]['weather'][0]['description']

    day5_temp.config(text=f"{round(tempday5)}°C")
    day5_desc.config(text=f"{despt5.capitalize()}")

    #     sixth day image
    sixth_day_img = api_data["daily"][5]['weather'][0]['icon']

    img = (Image.open(f"Weather icon set black/{sixth_day_img}.png"))
    resized_image = img.resize((70, 70))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixth_image.config(image=photo6)
    sixth_image.image = photo6

    tempday6 = api_data['daily'][5]['temp']['day']
    despt6 = api_data['daily'][5]['weather'][0]['description']

    day6_temp.config(text=f"{round(tempday6)}°C")
    day6_desc.config(text=f"{despt6.capitalize()}")

    #     seventh day image
    seventh_day_img = api_data["daily"][6]['weather'][0]['icon']

    img = (Image.open(f"Weather icon set black/{seventh_day_img}.png"))
    resized_image = img.resize((70, 70))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventh_image.config(image=photo7)
    seventh_image.image = photo7

    tempday7 = api_data['daily'][6]['temp']['day']
    despt7 = api_data['daily'][6]['weather'][0]['description']

    day7_temp.config(text=f"{round(tempday7)}°C")
    day7_desc.config(text=f"{despt7.capitalize()}")


# icon
image_icon = PhotoImage(file="Weather App Assets/partly_cloudy.png")
root.iconphoto(False, image_icon)

# Search box
search_box = PhotoImage(file="Weather App Assets/Search Bar.png")
myimage = Label(image=search_box, bg=colorBlue)
myimage.place(x=575, y=17)

search_icon = PhotoImage(file="Weather App Assets/search_icon 1.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="white", command=getweather)
myimage_icon.place(x=822, y=22)

textfield = tk.Entry(root, justify='left', width=22, font=('Open Sans semiBold', 12), bg="#FFFFFF", border=0,
                     fg="#243763")
textfield.place(x=600, y=30)
textfield.focus()

# Temperature other details
label_1 = Label(root, text="Updated on:", font=("Open Sans semiBold", 10), fg="white", bg=colorBlue)
label_1.place(x=350, y=145)

label_clock = Label(root, font=("Open Sans semiBold", 10), fg="white", bg=colorBlue)
label_clock.place(x=435, y=145)

label_winspeed = Label(root, text="Wind speed:", font=("Open Sans semiBold", 10), fg="white", bg=colorBlue)
label_winspeed.place(x=350, y=170)

label_hmdt = Label(root, text="Humidity:", font=("Open Sans semiBold", 10), fg="white", bg=colorBlue)
label_hmdt.place(x=350, y=195)

label_pressure = Label(root, text="Pressure:", font=("Open Sans semiBold", 10), fg="white", bg=colorBlue)
label_pressure.place(x=350, y=220)

t = Label(root, font=("Open Sans semiBold", 40), fg="white", bg=colorBlue)
t.place(x=430, y=50)

w = Label(root, font=("Open Sans semiBold", 10), fg="white", bg=colorBlue)
w.place(x=435, y=170)

h = Label(root, font=("Open Sans semiBold", 10), fg="white", bg=colorBlue)
h.place(x=435, y=195)

p = Label(root, font=("Open Sans semiBold", 10), fg="white", bg=colorBlue)
p.place(x=435, y=220)

d = Label(root, font=("Open Sans semiBold", 15), fg="white", bg=colorBlue)
d.place(x=400, y=120)

# Timezone
timezone = Label(root, font=('Raleway semiBold', 20), fg='white', bg=colorBlue)
timezone.place(x=325, y=20)

# day1 = Label(frame_box, bg=colorBlue)
# day1.place(x=7, y=20)

frame_box = Frame(root, width=85, height=85, bg=colorBlue)
frame_box.place(x=315, y=55)

main_image = Label(frame_box, bg=colorBlue)
main_image.place(x=0, y=0)

# Bottom
frame = Frame(root, width=900, height=210, bg=colorBlue)
frame.pack(side=BOTTOM)

day_box = PhotoImage(file="Weather App Assets/Days_rect.png")

Label(frame, image=day_box, bg=colorBlue).place(x=25, y=8)
Label(frame, image=day_box, bg=colorBlue).place(x=145, y=8)
Label(frame, image=day_box, bg=colorBlue).place(x=266, y=8)
Label(frame, image=day_box, bg=colorBlue).place(x=387, y=8)
Label(frame, image=day_box, bg=colorBlue).place(x=508, y=8)
Label(frame, image=day_box, bg=colorBlue).place(x=628, y=8)
Label(frame, image=day_box, bg=colorBlue).place(x=750, y=8)

# Days
# first cell
first_frame = Frame(root, width=100, height=160, bg=coloryWhite)
first_frame.place(x=32, y=281)

day1 = Label(first_frame, font=("Comfortaa Bold", 10), bg=coloryWhite, fg="black")
day1.place(x=6, y=5)

first_image = Label(first_frame, bg=coloryWhite)
first_image.place(x=12, y=35)

day1_temp = Label(first_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 18))
day1_temp.place(x=20, y=95)

day1_desc = Label(first_frame, bg=coloryWhite, fg="black", font=("Comfortaa Regular", 10))
day1_desc.place(x=10, y=135)

# second cell
second_frame = Frame(root, width=100, height=160, bg=coloryWhite)
second_frame.place(x=152, y=281)

day2 = Label(second_frame, font=("Comfortaa Bold", 10), bg=coloryWhite, fg="black")
day2.place(x=6, y=5)

second_image = Label(second_frame, bg=coloryWhite)
second_image.place(x=12, y=35)

day2_temp = Label(second_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 15))
day2_temp.place(x=10, y=70)

day2_temp = Label(second_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 18))
day2_temp.place(x=20, y=95)

day2_desc = Label(second_frame, bg=coloryWhite, fg="black", font=("Comfortaa Regular", 10))
day2_desc.place(x=10, y=135)

# third cell
third_frame = Frame(root, width=100, height=160, bg=coloryWhite)
third_frame.place(x=273, y=281)

day3 = Label(third_frame, font=("Comfortaa Bold", 10), bg=coloryWhite, fg="black")
day3.place(x=6, y=5)

third_image = Label(third_frame, bg=coloryWhite)
third_image.place(x=12, y=35)

day3_temp = Label(third_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 15))
day3_temp.place(x=10, y=70)

day3_temp = Label(third_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 18))
day3_temp.place(x=20, y=95)

day3_desc = Label(third_frame, bg=coloryWhite, fg="black", font=("Comfortaa Regular", 10))
day3_desc.place(x=10, y=135)

# fourth cell
fourth_frame = Frame(root, width=100, height=160, bg=coloryWhite)
fourth_frame.place(x=394, y=281)

day4 = Label(fourth_frame, font=("Comfortaa Bold", 10), bg=coloryWhite, fg="black")
day4.place(x=6, y=5)

fourth_image = Label(fourth_frame, bg=coloryWhite)
fourth_image.place(x=12, y=35)

day4_temp = Label(fourth_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 15))
day4_temp.place(x=10, y=70)

day4_temp = Label(fourth_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 18))
day4_temp.place(x=20, y=95)

day4_desc = Label(fourth_frame, bg=coloryWhite, fg="black", font=("Comfortaa Regular", 10))
day4_desc.place(x=10, y=135)

# fifth cell
fifth_frame = Frame(root, width=100, height=160, bg=coloryWhite)
fifth_frame.place(x=515, y=281)

day5 = Label(fifth_frame, font=("Comfortaa Bold", 10), bg=coloryWhite, fg="black")
day5.place(x=6, y=5)

fifth_image = Label(fifth_frame, bg=coloryWhite)
fifth_image.place(x=12, y=35)

day5_temp = Label(fifth_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 15))
day5_temp.place(x=10, y=70)

day5_temp = Label(fifth_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 18))
day5_temp.place(x=20, y=95)

day5_desc = Label(fifth_frame, bg=coloryWhite, fg="black", font=("Comfortaa Regular", 10))
day5_desc.place(x=10, y=135)

# sixth cell
sixth_frame = Frame(root, width=100, height=160, bg=coloryWhite)
sixth_frame.place(x=635, y=281)

day6 = Label(sixth_frame, font=("Comfortaa Bold", 10), bg=coloryWhite, fg="black")
day6.place(x=6, y=5)

sixth_image = Label(sixth_frame, bg=coloryWhite)
sixth_image.place(x=12, y=35)

day6_temp = Label(sixth_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 15))
day6_temp.place(x=10, y=70)

day6_temp = Label(sixth_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 18))
day6_temp.place(x=20, y=95)

day6_desc = Label(sixth_frame, bg=coloryWhite, fg="black", font=("Comfortaa Regular", 10))
day6_desc.place(x=10, y=135)

# seventh cell
seventh_frame = Frame(root, width=100, height=160, bg=coloryWhite)
seventh_frame.place(x=757, y=281)

day7 = Label(seventh_frame, font=("Comfortaa Bold", 10), bg=coloryWhite, fg="black")
day7.place(x=6, y=5)

seventh_image = Label(seventh_frame, bg=coloryWhite)
seventh_image.place(x=12, y=35)

day7_temp = Label(seventh_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 15))
day7_temp.place(x=10, y=70)

day7_temp = Label(seventh_frame, bg=coloryWhite, fg="black", font=("Comfortaa Bold", 18))
day7_temp.place(x=20, y=95)

day7_desc = Label(seventh_frame, bg=coloryWhite, fg="black", font=("Comfortaa Regular", 10))
day7_desc.place(x=10, y=135)

root.mainloop()
