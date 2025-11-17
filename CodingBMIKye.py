def calculate_bmi(request):
    if request.method == 'POST':
        weight = float(request.POST['weight'])
        height = float(request.POST['weight'])
        bmi = round(weight / (height ** 2))

        # Interpretaion of BMI 
        interpretation = get_bmi_interpretation(bmi)

        return render(request, 'result.html', {'bmi' : bmi,
'interpretation': interpretation})
    
    return render(request, 'index.html')

def get_bmi_interpretaion(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Healthy weight'
    else:
        return 'Overweight'

