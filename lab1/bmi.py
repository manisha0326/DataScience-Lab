def height_to_meters_feet(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 0.0254

def height_to_meters_cm(cm):
    return cm / 100

def weight_to_kg_pounds(pounds):
    return pounds * 0.453592

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

