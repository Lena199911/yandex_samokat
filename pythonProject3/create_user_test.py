import sender_stand_request
import data

def positive_zakaz(order):
    # В переменную response сохраняется результат
    response = sender_stand_request.post_zakaz(order)
    #сохраняем в переменную трекер заказа
    track = response.json()["track"]
    #Переводим номер заказа в строку
    track_to_str = str(track)
    #заказ по номеру
    response_zakaz = sender_stand_request.post_zakaz_track(track_to_str)

    # Проверяется, что код ответа равен 200
    assert response_zakaz.json()["code"] == 200


def test_zakaz_response():
    positive_zakaz(data.new_zakaz)
