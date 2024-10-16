from django.shortcuts import render

# Create your views here.
     from django.shortcuts import render
     from django.http import HttpResponse
     from .data_processing import load_data, train_model, save_model
     from joblib import load

     # Загрузка данных и обучение модели при старте приложения
     pos_reviews, neg_reviews = load_data()
     model = train_model(pos_reviews, neg_reviews)
     save_model(model)

     def index(request):
         return render(request, 'index.html')

     def result(request):
         if request.method == 'POST':
             review = request.POST['review']
             model = load('movie_review_model.joblib')
             prediction = model.predict([review])
             result_text = "Положительный" if prediction[0] == 1 else "Отрицательный"
             return HttpResponse(f'Результат: {result_text}')
         return HttpResponse('Ошибка: неверный метод запроса.')
     