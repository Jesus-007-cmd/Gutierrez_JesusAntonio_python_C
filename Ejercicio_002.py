import datetime
def formulario():
    print("1.	¿Cuál es tu nombre(s)?")
    nombre=input()
    print("2.	¿Cuál es tu primer apellido?")
    primerapellido=input()
    print("3.	¿Cuál es tu segundo apellido?")
    segundoapellido=input()
    print("4.	¿En qué año naciste?")
    año=input()
    print('5.	¿En qué mes y día naciste? (en el siguiente formato "mm-dd"')
    mesdia=input()
    nombrecompleto=nombre+" "+primerapellido+" "+segundoapellido
    print("A.	Este es tu nombre completo en mayúsculas:",nombrecompleto.upper())
    print("B.	Este es tu nombre completo en minúsculas :",nombrecompleto.lower())
    dia=mesdia[0:2]
    mes=mesdia[3:6]
    año_s=str(año)
    print("C.	Esta es tu fecha de nacimiento “dd-mm-aaaa”.", dia+"-"+mes+"-"+ año_s)
    hoy = datetime.date.today();
    añoactual=hoy.year
    mesactual=hoy.month
    diaactual=hoy.day
    edad=añoactual-año
    if int(mes)>mesactual:
        edad=edad-1
    if int(mes)==mesactual:
        if int(dia)>diaactual:
            edad=edad-1
    print("D.	Esta es tu edad.  ",edad)
    contador=0
    arreglonom=list(nombrecompleto)
    for i in arreglonom:
          if i in "aeiou":
              contador += 1
    print("E.	Tu nombre completo tiene", contador,"vocales")
    print("F.	Tu nombre completo tiene", len(nombrecompleto.replace(" ","")), "letras")
    print("G.	¿Tu edad es un carácter de tipo número?", isinstance(edad, int))
    print("H.	¿Tu nombre completo es un carácter de tipo alfanumérico?", isinstance(nombrecompleto,str))
    print("I.	Tu edad en 10 años será", edad+10)
    print("J.	La media de tu edad actual y tu edad en 20 años es", (edad+edad+20)/2)



