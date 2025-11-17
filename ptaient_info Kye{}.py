ptaient_info = {}

patient_info['name'] = input("Enter patient name: ")

pateint_info['age'] = int(input("Enter patient name"))

patient_info['details'] = input("Enter patient details (e.g., symptoms, history): ")

print("\n--- Patient record ---")   
for key, value in patient_info.items():        
    print(f"{key.replace('_', ' ').title()}: {value}")     
                          