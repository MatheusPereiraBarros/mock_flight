import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Configurações iniciais
fake = Faker()
Faker.seed(42)
random.seed(42)
np.random.seed(42)

# Parâmetros
num_flights_per_year = 4000
num_days = 365
start_date = datetime(2023, 1, 1)
airlines = ['AirNSR', 'SkyWave', 'JetFly', 'GlobeAir', 'PacificWings']
destinations = ['JFK', 'LAX', 'ORD', 'ATL', 'CDG', 'LHR', 'HND', 'DXB', 'SYD', 'GRU']

# Geração de dados de voos
flights = []
for i in range(num_flights_per_year):
    flight_number = f"{random.choice(airlines)}{random.randint(1000, 9999)}"
    airline = random.choice(airlines)
    departure_time = start_date + timedelta(days=i//(num_flights_per_year//num_days), hours=random.randint(6, 22), minutes=random.randint(0, 59))
    arrival_time = departure_time + timedelta(hours=random.randint(1, 5))
    delay = max(0, np.random.normal(30, 45))  # Média de 30 minutos, desvio padrão de 45 minutos para simular problemas operacionais
    cancellation = random.random() < 0.05  # 5% de cancelamentos
    destination = random.choice(destinations)
    
    flights.append([flight_number, airline, departure_time, arrival_time, int(delay), cancellation, destination])

flight_df = pd.DataFrame(flights, columns=['FlightNumber', 'Airline', 'DepartureTime', 'ArrivalTime', 'Delay', 'Cancellation', 'Destination'])

# Geração de dados de passageiros
passengers = []
for flight in flight_df['FlightNumber']:
    passenger_count = random.randint(50, 150)  
    complaints = max(0, np.random.poisson(2))  
    satisfaction_score = max(1, min(5, np.random.normal(3, 1.5)))  
    
    passengers.append([flight, passenger_count, complaints, round(satisfaction_score, 1)])

passenger_df = pd.DataFrame(passengers, columns=['FlightNumber', 'PassengerCount', 'Complaints', 'SatisfactionScore'])

# Geração de dados operacionais
operations = []
for flight in flight_df['FlightNumber']:
    turnaround_time = max(20, np.random.normal(60, 15))  # Média de 60 minutos, desvio padrão de 15 minutos, tempo maior devido a problemas
    taxi_time = max(5, np.random.normal(15, 5))  # Média de 15 minutos, desvio padrão de 5 minutos
    gate_utilization = random.randint(50, 90)  # Utilização do portão entre 50% e 90%
    
    operations.append([flight, int(turnaround_time), int(taxi_time), gate_utilization])

operational_df = pd.DataFrame(operations, columns=['FlightNumber', 'TurnaroundTime', 'TaxiTime', 'GateUtilization'])

# Geração de dados climáticos
weather_conditions = ['Clear', 'Rain', 'Fog', 'Storm']
weather = []
for day in range(num_days):
    date = start_date + timedelta(days=day)
    condition = random.choice(weather_conditions)
    temperature = round(np.random.normal(20, 10), 1)  # Média de 20°C, desvio padrão de 10°C
    wind_speed = max(0, np.random.normal(15, 10))  # Média de 15 km/h, desvio padrão de 10 km/h
    visibility = max(1, np.random.normal(8, 5))  # Média de 8 km, desvio padrão de 5 km
    
    weather.append([date, condition, temperature, int(wind_speed), int(visibility)])

weather_df = pd.DataFrame(weather, columns=['Date', 'WeatherCondition', 'Temperature', 'WindSpeed', 'Visibility'])

# Salvando os dados em CSVs
flight_df.to_csv('flights_small_airport.csv', index=False)
passenger_df.to_csv('passengers_small_airport.csv', index=False)
operational_df.to_csv('operations_small_airport.csv', index=False)
weather_df.to_csv('weather_small_airport.csv', index=False)

print("Dados mockados e salvos em seus respectivos CSVs.")
