class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    def get_celsius(self) -> float:
        """Getter for the temperature in Celsius."""
        return self._celsius

    def set_celsius(self, value: float):
        """Setter for the temperature in Celsius with basic validation."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    def get_fahrenheit(self) -> float:
        """Getter for the temperature in Fahrenheit."""
        return self._celsius * 9 / 5 + 32

    def set_fahrenheit(self, value: float):
        """Setter for the temperature in Fahrenheit, converting to Celsius."""
        self._celsius = (value - 32) * 5 / 9

if __name__ == "__main__":
    temp = Temperature(25) 
    print(f"Temperature is {temp.get_celsius()}C, or {temp.get_fahrenheit()}F")

    temp.set_fahrenheit(68)
    print(f"Temperature is now {temp.get_celsius()}C, or {temp.get_fahrenheit()}F")

    try:
        temp.set_celsius(-300)
    except ValueError as e:
        print("Error:", e)
