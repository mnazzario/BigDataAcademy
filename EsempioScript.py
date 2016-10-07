#esempio di import di un'altra libreria
from Hello import hello_world, hello_world_ret #se voglio importare tutto usare l'asterisco

print "Hello world"

print "ESEGUO LA FUNZIONE DI SEGUITO"

hello_world()

print "ORA PROVO CON LA FUNZIONE CHE MI RITORNA UN VALORE"

print(hello_world_ret())
