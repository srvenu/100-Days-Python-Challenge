def cel_far(cel):
    return ((9/5)*cel)+32

def m_km(km):
    return km*1000

def usd_inr(usd):
    return usd*83.57

cel=int(input("Enter celcius : "))
print(f"{cel} celcius = {cel_far(cel)} fahrenheit ")
km=int(input("Enter Kilo-meter : "))
print(f"{km} km = {m_km(km)} mtr")
usd=int(input("Enter USD : "))
print(f"{usd} usd = {usd_inr(usd)} inr ")