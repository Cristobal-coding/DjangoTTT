cursos_base = [['1erobasico','Primero básico',1.0], ['2dobasico','Segundo básico',2.0],['3robasico','Tercero básico',3.0],
            ['4tobasico', 'Cuarto básico',4.0],['5tobasico','Quinto básico',5.0],['6tobasico', 'Sexto básico',6.0],
            ['7tobasico', 'Septimo básico',7.0],['8vobasico', 'Octavo básico',8.0],['1eromedio','Primero medio',9.0],['2domedio','Segundo medio',10.0],
            ['3romedioCON','Tercero medio Construccion', 11.0, 'CON'],
            ['3romedioEL','Tercero medio Electricidad', 11.1, 'EL'],
            ['3romedioMET','Tercero medio Construccion Metalicas', 11.2, 'MET'],
            ['4tomedioCON','Cuarto medio Construccion',12.0, 'CON'] ,
            ['4tomedioEL','Cuarto medio Electricidad',12.1, 'EL'] ,
            ['4tomedioMET','Cuarto medio Construccion Metalicas',12.2, 'MET'] ,
            ]

#Esto genera un Choices desde 2000 hasta la fecha actual
def generate_years(current_año):
    años = []
    for i in range(2000 , current_año+1):
        año = tuple((str(i),str(i)))
        años.append(año) 
    años = tuple(años)
    return años

def curso_anterior(numero):
    for i in range(0, len(cursos_base)):
        if i > 0  :
            if numero < 11.0:
                if cursos_base[i][2] == numero:
                    return cursos_base[i-1][1]
            elif  numero in [11.0,11.1,11.2] and i>=10 and i<13:
                if cursos_base[i][2] == numero:
                    return cursos_base[9][1]
            elif  numero in [12.0,12.1,12.2] and i>=13 :
                if cursos_base[i][2] == numero:
                    number = i-3
                    return cursos_base[i-3][1]
def get_curso_anterior_pk(numero):
    for i in range(0, len(cursos_base)):
        if i > 0  :
            if numero < 11.0:
                if cursos_base[i][2] == numero:
                    return cursos_base[i-1][0]
            elif  numero in [11.0,11.1,11.2] and i>=10 and i<13:
                if cursos_base[i][2] == numero:
                    return cursos_base[9][0]
            elif  numero in [12.0,12.1,12.2] and i>=13 :
                if cursos_base[i][2] == numero:
                    number = i-3
                    return cursos_base[i-3][0]