"""
Ali, çatı katında bir satranç takımı bulur. Ancak bu takımda sadece beyaz taşlar bulunduğu farketti. Göreviniz takımdaki eksik taşların

durumunu tespit etmektir. Şöyle ki; normalde beyaz takımda sırasıyla 1 Şah, 1 Vezir, 2 At, 2 Kale, 2 Fil ve 8 Piyon bulunmalıdır.

Tek satırda bulduğunuz bu setteki taşların girişini yapacaksınız. Çıkış olarak ise eksik ya da fazla taşların durumu verilecektir.

Örnek
0 1 2 2 2 7 >>> 1 Şah eksik, 1 Piyon eksik
veya

2 1 2 1 2 1 >>> 1 Şah fazla, 1 Kale eksik, 7 Piyon eksik

"""

def create_int_list(coming_list): # Gelen veriyi ayırarak int şekilde listeler

    temp_list = list()

    for i in  coming_list:
        temp_list.append(int(i))

    return temp_list


def check_elements(value):

    default_dict = {"Şah":1, "Vezir":1, "At":2, "Kale":2, "Fil": 2, "Piyon":8}
    input_list = create_int_list(value)
    result = ""
    counter = 0
    default_values = list(default_dict.values())
    default_keys = list(default_dict.keys())

    if len(input_list) != 6:
        return "Lütfen doğru sayıda eleman giriniz(6) "

    else:

        while counter < len(default_values):

            if input_list[counter] - default_values[counter] > 0:
                result += str(abs(input_list[counter] - default_values[counter])) + " " + default_keys[counter] +" fazla "

            elif input_list[counter] - default_values[counter] < 0:
                result += str(abs(input_list[counter] - default_values[counter])) + " " + default_keys[counter] + " eksik "

            counter += 1

    return result





while True:

    input_list = input("Lütfen değerleri giriniz: ")
    print(check_elements(input_list))


