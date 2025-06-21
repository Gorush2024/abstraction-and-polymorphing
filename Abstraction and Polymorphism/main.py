class India:
    def capital(self):
        print("New Delhi is the capital of india")
    def language(self):
        print("Hindi is the most spoken language is india")
    def type(self):
        print("India is a developing country\n\n")
    
class Usa:
    def capital(self):
        print("Washington, Dc is the capital of Usa")
    def language(self):
        print("English is the most widely spoken language is Usa")
    def type(self):
        print("India is a developed country")

obj_ind = India()
obj_us = Usa()

for country in(obj_ind,obj_us):
    country.capital()
    country.language()
    country.type()