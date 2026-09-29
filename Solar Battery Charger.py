# Solar Battery Charger - Easy Python

solar_voltage = float(input("Enter solar panel voltage (V): "))
battery_voltage = float(input("Enter battery voltage (V): "))

print("\n--- SOLAR BATTERY CHARGER ---")
print("Solar Voltage  :", solar_voltage, "V")
print("Battery Voltage:", battery_voltage, "V")

# Charging control
if solar_voltage > battery_voltage and battery_voltage < 14.4:
    print("Charging: ON")
    print("Solar panel is charging the battery.")

elif battery_voltage >= 14.4:
    print("Charging: OFF")
    print("Battery is fully charged.")

else:
    print("Charging: OFF")
    print("Not enough solar voltage.")
