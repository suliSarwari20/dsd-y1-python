def get_vital_signs():
    try:
        heart_rate = int(input("Enter heart rate (bpm): "))
        temperature = float(input("Enter body temperature (°C): "))
        oxygen_level = int(input("Enter oxygen saturation (%): "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None
    return heart_rate, temperature, oxygen_level

def check_vitals(hr, temp, oxy):
    messages = []

    
    if temp > 37.5:
        messages.append("Warning: High temperature (fever).")

    
    if oxy < 92:
        messages.append("Warning: Low oxygen saturation.")

  
    if 60 <= hr <= 100:
        messages.append("Heart rate is normal.")
    else:
        messages.append("Warning: Heart rate is outside the normal range.")

    return messages

def main():
    vitals = get_vital_signs()
    if vitals:
        hr, temp, oxy = vitals
        print("\nVital Signs Monitor Report:")
        print(f"Heart Rate: {hr} bpm")
        print(f"Temperature: {temp} °C")
        print(f"Oxygen Saturation: {oxy} %\n")

        results = check_vitals(hr, temp, oxy)
        for msg in results:
            print(msg)

if __name__ == "__main__":
    main()
