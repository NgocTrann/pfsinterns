from tkinter import *
import requests
api_key = "30d4741c779ba94c470ca1f63045390a"

class WeatherGui:
    def __init__(self):
        self.PassedCity = NotImplemented
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Weather Forecast App")

        self.myLabel = Label(self.root, text="Weather Forcecast App", font=("Arial", 18))
        self.myLabel.pack(pady=20)

        self.textbox = Text(self.root, height=3, font=("Arial", 16))
        self.textbox.pack(padx=20)

        self.TextButton = Button(self.root, text="Click Me!", font=("Arial", 16), command=self.OnButtonClick)
        self.TextButton.pack(pady=10, padx=10)

        self.buttonFrame = Frame(self.root)
        self.buttonFrame.columnconfigure(0)

        # Weather
        self.Weather = Label(self.buttonFrame, text="Weather: ", font=("Arial", 18))
        self.Weather.grid(row = 0, column = 0)

        self.WeatherText = Label(self.buttonFrame, text="nil", font=("Arial", 18))
        self.WeatherText.grid(row = 0, column = 1)

        # Temp
        self.Temp = Label(self.buttonFrame, text="Temp: ", font=("Arial", 18))
        self.Temp.grid(row = 1, column = 0)

        self.TempText = Label(self.buttonFrame, text="nil", font=("Arial", 18))
        self.TempText.grid(row = 1, column = 1)

        # Humidity
        self.Humidity = Label(self.buttonFrame, text="Humidity: ", font=("Arial", 18))
        self.Humidity.grid(row = 2, column = 0)

        self.HumidityText = Label(self.buttonFrame, text="nil", font=("Arial", 18))
        self.HumidityText.grid(row = 2, column = 1)


        # WindSpeed
        self.WindSpeed = Label(self.buttonFrame, text="WindSpeed: ", font=("Arial", 18))
        self.WindSpeed.grid(row = 3, column = 0)

        self.WindSpeedText = Label(self.buttonFrame, text="nil", font=("Arial", 18))
        self.WindSpeedText.grid(row = 3, column = 1)

        self.buttonFrame.pack(fill = "x", padx=20, pady=20)

        #  
        self.ErrorText = Label(self.root, text="", font=("Arial", 16))
        self.ErrorText.pack(padx=20, pady=50)

        #
        self.root.mainloop()

    def OnButtonClick(self):
        weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.textbox.get("1.0", "end-1c")}&units=imperial&APPID={api_key}")
        if weatherData.status_code == 200:
            self.WeatherText.config(text= weatherData.json()["weather"][0]["main"])
            self.HumidityText.config(text=f"{weatherData.json()["main"]["humidity"]}")
            self.WindSpeedText.config(text= f"{weatherData.json()["wind"]["speed"]} m/s")
            self.TempText.config(text=f"{weatherData.json()["main"]["temp"]}°F")
            self.ErrorText.config(text="")
        else:
            self.ErrorText.config(text="Error")
            self.WeatherText.config(text="nil")
            self.HumidityText.config(text="nil")
            self.WindSpeedText.config(text="nil")
            self.TempText.config(text="City Not Found")


        


if __name__ == "__main__":
    app = WeatherGui()


