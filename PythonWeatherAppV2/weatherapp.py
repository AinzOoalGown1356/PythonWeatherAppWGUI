from bs4 import BeautifulSoup
import requests, tkinter
from tkinter import *
from PIL import ImageTk, Image

#change url to anyarea on the weather.com website if you want
url = 'https://weather.com/weather/today/l/d6555e3553dc87739c3bee0d78dcd70d1cbfbbb237a66b97bb00664f98ad27aa'

Window = Tk()
Window.title('Weather App')
Window.config(bg="white")
Window.geometry("500x250")

ic1 = PhotoImage(file = 'icon.png')
Window.iconphoto(False, ic1)

img = Image.open("C:/Users/Gamin/OneDrive/Documents/PythonWeatherAppV2/weather_icon.png")
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    location = soup.find('h1', class_="CurrentConditions--location--1YWj_").text
    temperature = soup.find('span', class_="CurrentConditions--tempValue--MHmYY").text
    currentcondition = soup.find('div', class_="CurrentConditions--phraseValue--mZC_p").text
    LocationLabel.config(text=location)
    TemperatureLabel.config(text=temperature)
    weatherPrediciionLabel.config(text=currentcondition)

    # Updates labels every minute
    TemperatureLabel.after(60000, getWeather)
    weatherPrediciionLabel.after(60000, getWeather)
    Window.update()

LocationLabel = Label(Window, fg='black', font=("Caliri bold", 35), bg="white")
LocationLabel.grid(row=0, column=0, sticky="nsew", padx=100)

TemperatureLabel = Label(Window, fg='black', font=("Caliri bold", 50), bg="white")
TemperatureLabel.grid(row=1, column=0, sticky="s", padx=10, pady=10)

weatherPrediciionLabel = Label(Window, fg='black', font=("Caliri bold", 30), bg="white")
weatherPrediciionLabel.place(relx=0.36, rely=0.6)
getWeather()

ImageLabel = Label(Window, image=img, bg="white")
ImageLabel.place(relx=0.6,rely=0.29)

Window.mainloop()
