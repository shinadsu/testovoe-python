
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Считываем Excel файл с адресами в DataFrame
df = pd.read_excel('addresses.xlsx')

# Инициализируем геокодер Nominatim
geolocator = Nominatim(user_agent="geo")

# Функция для получения координат по адресу
def get_coordinates(address):
    try:
        location = geolocator.geocode(address)
        return (location.latitude, location.longitude)
    except (AttributeError, GeocoderTimedOut):
        return None

# Создаем новый столбец для координат
df['coordinates'] = df['Адрес'].apply(get_coordinates)

# Убираем адреса, которые не удалось расшифровать
df.dropna(subset=['coordinates'], inplace=True)

# Записываем DataFrame с координатами в Excel файл
df.to_excel('addresses_with_coordinates.xlsx', index=False)