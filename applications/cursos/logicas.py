#Esto genera un Choices desde 2000 hasta la fecha actual
def generate_years(current_año):
    años = []
    for i in range(2000 , current_año+1):
        año = tuple((str(i),str(i)))
        años.append(año) 
    años = tuple(años)
    return años