from django.shortcuts import render
import joblib
from django.shortcuts import render
from django.http import JsonResponse

# Load the model
model = joblib.load('fraud_detection_model.pkl')

def predict(request):
    if request.method == 'POST':
        ratio_to_median_purchase_price = float(1.393858)
        repeat_retailer = float(0.891938)
        distance_from_home = float(22.429)
        distance_from_last_transaction = float(4.927520)
        used_chip = float(0.373070)
        used_pin_number = float(0.1121)
        online_order = float(0.614)
        

        prediction = model.predict([[ratio_to_median_purchase_price, repeat_retailer, distance_from_home, distance_from_last_transaction,used_chip,used_pin_number,online_order]])[0]
        print(prediction)
        result = 'Fraud' if prediction == 1 else 'Not Fraud'

        return JsonResponse({'result': result})

    return render(request, 'form.html')
