import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600


def Adesanya(mofe):
    try:
        name = mofe['name']
        description = mofe['weather'][0]['description']
        temp = mofe['main']['temp']

        final_string = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, description, temp)
    except():
        final_string = "There was a problem retrieving that information"
    return final_string


def get_weather(city):
    weather_key = '7f83af070e20d6b846eea23452910538'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': "imperial"}
    response = requests.get(url, params=params)
    mofe = response.json()

    Label["text"] = Adesanya(mofe)


# Everything in GUI starts here
# 7f83af070e20d6b846eea23452910538
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid=


root = tk.Tk()

Canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
Canvas.pack()

Background_image = tk.PhotoImage(file="./landscape.png")
Background_label = tk.Label(Canvas, image=Background_image)
Background_label.place(relwidth=1, relheight=1)

Frame = tk.Frame(Canvas, bg='cyan', bd=5)
Frame.place(relheight=0.1, relwidth=0.75, relx=0.5, anchor='n', rely=0.1)

Entry = tk.Entry(Frame, font=40)
Entry.place(relwidth=0.65, relheight=1)

Button = tk.Button(Frame, text="Please input your location: ", fg="yellow", command=lambda: get_weather(Entry.get()))
Button.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)

Lower_frame = tk.Frame(Canvas, bg='cyan', bd=10)
Lower_frame.place(relheight=0.6, relwidth=0.75, relx=0.5, anchor='n', rely=0.25)

Label = tk.Label(Lower_frame, bg='white', font=("Modern", 20))
Label.place(relheight=1, relwidth=1)

root.mainloop()
# Everything runnable on GUI ends here
