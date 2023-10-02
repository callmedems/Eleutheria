from tkinter import *

#FUNCION PARA PANTALLA 2
def siguiente_1():

    #FUNCIÓN "VOLVER" A PANTALLA 1 DESDE PANTALLA 2
    def volver_1():
        v_02.iconify()
        v_01.deiconify()

    #funciones de botones rojo, amarillo y verde

    #función "Rojo"
        #aquí se hace la pantalla 3
    def rojo():
        def cancelar_1():
            v_03.iconify()
            v_02.deiconify()

        v_02.iconify()
        v_03 = Toplevel(v_02)
        v_03.title("Pantalla 3")
        v_03.geometry("270x480")
        v_03.resizable(0,0)
        v_03.config(bg="#EDBFBF")

        anuncio_msg = Message(v_03, text="POR FAVOR MANTÉN LA CALMA", font=("Candara Light", 20), fg="#AB1616", anchor=CENTER, justify=CENTER, bg="#EDBFBF")
        one_msg = Message(v_03, text="Se está marcando a emergencias", font=("Lucida Console", 10), fg="black", anchor=CENTER, justify=CENTER, bg="#C7ADAD", padx=10, pady=10)
        two_msg = Message(v_03, text="Se contactó a contactos de emergencia", font=("Lucida Console", 10), fg="black", padx=10, pady=10, bg="#C7ADAD", anchor=CENTER, justify=CENTER)
        three_msg = Message(v_03, text=" Buscando \nubicaciones\ncerca de ti", font=("Lucida Console", 10), fg="black", padx=10, pady=12, bg="#C7ADAD", anchor=CENTER, justify=CENTER)

        cancel_btn = Button(v_03, text="CANCELAR", font=("Candara Light", 10), bg="#EDBFBF", command=cancelar_1)

        #colocación de widgets
        anuncio_msg.place(x=55, y=10)
        one_msg.place(x=80, y=150)
        two_msg.place(x=80, y=210)
        three_msg.place(x=80, y=280)
        cancel_btn.place(x=100, y=440)
    
    #función "amarillo"
        #aquí se hace la pantalla 4
    def amarillo():
        def cancelar_2():
            v_04.iconify()
            v_02.deiconify()
            
        v_02.iconify()
        v_04 = Toplevel(v_02)
        v_04.title("Pantalla 4")
        v_04.geometry("270x480")
        v_04.resizable(0,0)
        v_04.config(bg="#EDBFBF")

        anuncio_msg_2 = Message(v_04, text="TU BIENESTAR ES IMPORTANTE", bg="#EDBFBF", fg="#AB1616", font=("Candara Light", 20), anchor=CENTER, justify=CENTER)

        one_msg_2 = Message(v_04, text="Se está contactando ayuda psicológica", font=("Lucida Console", 10), fg="black", padx=10, pady=10, bg="#C7ADAD", anchor=CENTER, justify=CENTER)
        two_msg_2 = Message(v_04, text="Se está\nbuscando\ncentros de\napoyo\ncerca de tu\nubicación", font=("Lucida Console", 10), fg="black", padx=10, pady=10, bg="#C7ADAD", anchor=CENTER, justify=CENTER)

        cancel_btn_2 = Button(v_04, text="CANCELAR", font=("Candara Light", 10), bg="#EDBFBF", command=cancelar_2)

        #colocación de widgets
        anuncio_msg_2.place(x=45, y=10)
        one_msg_2.place(x=80, y=180)
        two_msg_2.place(x=80, y=250)
        cancel_btn_2.place(x=100, y=440)
        

    #función "verde"
        #aquí se hace la pantalla 5
    def verde():
        def cerrarverde():
            v_05.iconify()
            v_02.deiconify()
            
        #pantalla 6
        def pantalla_6():
            def cancelar_3():
                v_06.iconify()
                v_05.deiconify()
                
            v_05.iconify()
            v_06 = Toplevel(v_05)
            v_06.title("Pantalla 6")
            v_06.geometry("270x480")
            v_06.resizable(0,0)
            v_06.config(bg="#EDBFBF")
            
            preguntaverde1 = Message(v_06, text = "¿Qué es la violencia de género?", justify=CENTER, anchor=CENTER, bg="#C97171", font=("Times New Roman", 18), fg="white")
            respuestaverde1 = Message(v_06, text = "La violencia de género se\nrefiere a los actos\ndañinos dirigidos contra\nuna persona o un\ngrupo de personas en razón\nde su género. Tiene su origen\nen la desigualdad de\ngénero, el abuso de poder\ny la existencia de\nnormas dañinas.\nEl término se utiliza\nprincipalmente para\nsubrayar el hecho de\nque las diferencias\nestructurales de poder\nbasadas en el género\ncolocan a las mujeres y\nniñas en situación de\nriesgo frente a\nmúltiples formas de\nviolencia.", bg="#5C3030", font=("Lucida Console", 10), fg="white", anchor=CENTER, justify=CENTER)
            boton_cancelarverde1 = Button (v_06, text = "CANCELAR", font=("Candara Light", 8), bg="#EDBFBF", command = cancelar_3)

            #colocación de widgets
            preguntaverde1.place (x=67, y = 15)
            respuestaverde1.place (x=15, y = 130)
            boton_cancelarverde1.place(x=110, y=430)
            
        def pantalla_7():
            def cancelar_4():
                v_07.iconify()
                v_05.deiconify()

            v_05.iconify()
            v_07 = Toplevel(v_05)
            v_07.title("Pantalla 7")
            v_07.geometry("270x480")
            v_07.resizable(0,0)
            v_07.config(bg="#EDBFBF")

            pregunta_lbl_1 = Label(v_07, text="¿Cómo identificar la\nviolencia de género?", font=("Times New Roman", 18), bg="#C97171", fg="white", justify=CENTER, anchor=CENTER)
            respuesta_msg_1 = Message(v_07, anchor=CENTER, bg="#5C3030", fg="white", font=("Lucida Console", 10), text="Es violencia si una persona:\n-Amenaza con hacerte daño a ti\no a tu familia.\n-Desprecia lo que sientes\na menudo.\n-Ridiculiza a las mujeres.\n-No deja que tengas un\ntrabajo y que ganes dinero\npara evitar que tengas\nindependencia económica.\n-Te humilla o insulta tanto\nen privado como delante de\nmás personas.\n-Te ha agredido físicamente.\n-Te aísla de tu familia o\nde tus amigos.\n-Te ha forzado a mantener\nrelaciones sexuales en contra\nde tu voluntad.\n-Mantiene el control sobre\ntu dinero.\n-Toma decisiones que te\nafectan.\n-Si le dices que quieres\nla separación o el divorcio\no romper la relación amenaza\ncon quedarse con tus hijos\ne hijas.")
            cancelbtn_4 = Button(v_07, text="CANCELAR", font=("Candara Light", 8), bg="#EDBFBF", command=cancelar_4)

            #colocación de widgets
            pregunta_lbl_1.place(x=35, y=10)
            respuesta_msg_1.place(x=10,y=75)
            cancelbtn_4.place(x=105, y=450)
            
            

        #Pantalla 8
        def pantalla_8():
            def cancelar_5():
                v_08.iconify()
                v_05.deiconify()

            v_05.iconify()
            v_08 = Toplevel(v_05)
            v_08.title("Pantalla 8")
            v_08.geometry("270x480")
            v_08.resizable(0,0)
            v_08.config(bg="#EDBFBF")

            pregunta_lbl_2 = Label(v_08, font=("Times New Roman", 18), bg="#C97171", fg="white", anchor=CENTER, justify=CENTER, text="¿A dónde puedo\nacudir por ayuda?")
            respuesta_msg_2 = Message(v_08, font=("Lucida Console", 10), bg="#5C3030", fg="white", anchor=CENTER, text="1.Centro de Terapia de\nApoyo a Víctimas de Delitos\nSexuales (CTA).\n\n2. Centro de Atención a\nla Violencia\nIntrafamiliar (CAVI).\n\n3. Centro de Atención a\nRiesgos Victimales y\nAdicciones (CARIVA).\n\n4.Centro de Investigación\nVictimológica y de Apoyo\nOperativo (CIVA).\n\n5. Centro de Justicia\npara las Mujeres.")
            cancelbtn_5=Button(v_08,text="CANCELAR", font=("Candara Light", 8), bg="#EDBFBF", command=cancelar_5)

            #colocación de widgets
            pregunta_lbl_2.place(x=48, y=15)
            respuesta_msg_2.place(x=23, y=115)
            cancelbtn_5.place(x=105,y=420)

            

        def pantalla_9():
            def cancelar_6():
                v_09.iconify()
                v_05.deiconify()
                
            v_05.iconify()
            v_09 = Toplevel(v_05)
            v_09.title("Pantalla 9")
            v_09.geometry("270x480")
            v_09.resizable(0,0)
            v_09.config(bg="#EDBFBF")
            
            preguntaverde4 = Message(v_09, anchor=CENTER, text = "¿Qué puedo hacer ante una situación de riesgo de violencia de género?", justify = CENTER, bg="#C97171", font=("Times New Roman", 18), fg="white")
            respuestaverde4 = Message(v_09, anchor=CENTER, bg="#5C3030", font=("Lucida Console", 10), fg="white", text = "Si hay violencia, o\ntienes miedo debido a la\nsituación en casa:\n\n-Acérquese a un lugar desde\ndonde pueda salir sin peligro.\n\n-No vaya a la cocina, donde\nhay objetos que puedan\nhacerle daño ni al baño o\nhabitaciones donde puede\nquedar encerrada.\n\n-Si el agresor ha perdido\nel control, salga de la casa.\n\n-Si no puede salir, trate\nde tranquilizar al agresor.")
            boton_cancelarverde4 = Button (v_09, text = "CANCELAR", font=("Candara Light", 8), bg="#EDBFBF", command = cancelar_6)

            #colocación de widgets
            preguntaverde4.place(x=27, y=10)
            respuestaverde4.place(x=10, y=150)
            boton_cancelarverde4.place(x=105, y=440)
            
        v_02.iconify()
        v_05 = Toplevel(v_02)
        v_05.title("Pantalla 5")
        v_05.geometry("270x480")
        v_05.resizable(0,0)
        v_05.config(bg="#EDBFBF")
        
        label_1v05 = Label (v_05, text = "INFÓRMATE", bg="#EDBFBF", fg="#AB1616", font=("Candara Light", 20), anchor=CENTER, justify=CENTER)
        boton1_v5 = Button (v_05, text = "¿QUÉ ES LA\nVIOLENCIA DE \n GÉNERO?", font=("Lucida Console", 10), bg="#C7ADAD", fg="black", padx=10, pady=10, anchor=CENTER, justify=CENTER, command=pantalla_6)
        boton2_v5 = Button (v_05, text = "¿CÓMO \nIDENTIFICAR\nLA VIOLENCIA \nDE GÉNERO?", font=("Lucida Console", 10), bg="#C7ADAD", fg="black", padx=10, pady=10, anchor=CENTER, justify=CENTER, command=pantalla_7)
        boton3_v5 = Button (v_05, text = "¿A DÓNDE \nPUEDO ACUDIR\nPOR AYUDA?", font=("Lucida Console", 10), bg="#C7ADAD", fg="black", padx=14, pady=10, anchor=CENTER, justify=CENTER, command=pantalla_8)
        boton4_v5 = Button (v_05, text = "¿QUÉ PUEDO\nHACER\nANTE UNA\nSITUACIÓN\n DE RIESGO DE\n VIOLENCIA DE\n GÉNERO?", font=("Lucida Console", 10), bg="#C7ADAD", fg="black", padx=10, pady=10, anchor=CENTER, justify=CENTER, command=pantalla_9)
        boton_cancelarv5 = Button (v_05, text = "CANCELAR", font=("Candara Light", 8), bg="#EDBFBF", command = cerrarverde)

       #colocación de widgets
        label_1v05.place (x = 60, y =10)
        boton1_v5.place (x=68, y=60)
        boton2_v5.place (x=68, y=130)
        boton3_v5.place (x=68, y=213)
        boton4_v5.place (x=68, y=283)
        boton_cancelarv5.place (x=105, y=430)


    v_01.iconify()
    v_02 = Toplevel(v_01)
    v_02.title("Pantalla 2")
    v_02.geometry("270x480")
    v_02.resizable(0,0)
    v_02.config(bg="#EDBFBF")


    question_msg = Message(v_02, text="¿Cómo definirías la gravedad o peligro de tu situación, siendo rojo lo más grave y verde lo menos grave?", bg="#EDBFBF", font=("Candara Light", 15), fg="#5C3030", justify = CENTER, anchor = CENTER)
    red_btn = Button(v_02, text="ROJO", bg="firebrick3", font=("Lucida Console", 20), fg="black", anchor =CENTER, justify = CENTER, command = rojo)
    yellow_btn = Button(v_02, text = "AMARILLO", bg="yellow", font=("Lucida Console", 20), fg="black", anchor = CENTER, justify = CENTER, command = amarillo)
    green_btn = Button(v_02, text = "VERDE", bg="green", font=("Lucida Console", 20), fg="black", anchor = CENTER, justify = CENTER, command = verde)


    sig_btn_2 = Button(v_02, text="VOLVER", bg="#EDBFBF",font=("Candara Light", 8), command=volver_1)
    
    
    #Colocación de widgets
    question_msg.place(x=38, y=10)
    red_btn.place(x=90, y=170)
    yellow_btn.place(x=60, y=230)
    green_btn.place(x=82, y=290)
    sig_btn_2.place(x=110, y=440)
    


v_01 = Tk()
v_01.title("Pantalla 1")
v_01.geometry("270x480")
v_01.resizable(0,0)
v_01.config(bg="#EDBFBF")

#Imagen
logo = PhotoImage(file="logotipo eleutheria.png")
logo_lbl = Label(v_01, image=logo, bg="#EDBFBF")
#Título y slogan arriba de imagen
title_lbl = Label(v_01, text="Eleutheria", font=("Times New Roman", 28), fg="black", bg="#EDBFBF")
slogan_lbl = Label(v_01, text="NO ESTÁS SOLA", font=("Candara Light", 13), fg="black", bg="#EDBFBF")

#Etiqueta de "Bienvenida
welcome_lbl = Label(v_01, text="Bienvenida", font=("Lucida Console", 13), bg="#C7ADAD")
#Nombre, número y contacto que se le pide al usuario
name_lbl = Label(v_01, text="Nombre:", font=("Lucida Console", 8), bg="#EDBFBF")
number_lbl = Label(v_01, text="Número:", font=("Lucida Console", 8), bg="#EDBFBF")
contacts_msg = Message(v_01, text="Inserta un contacto de emergencia:", font=("Lucida Console", 8), bg="#EDBFBF")
#Widgets de entry
name_ent = Entry(v_01)
number_ent = Entry(v_01)
contacts_ent = Entry(v_01)

#Mensaje final
final_lbl = Label(v_01, text="Tus datos son necesarios para entender tu situación \n y poder ayudarte de la forma más rápida posible.", font=("Candara Light", 8), bg="#EDBFBF", justify = CENTER, anchor = CENTER, fg="black")

#Botón de siguiente
sig_btn = Button(v_01, text="SIGUIENTE", font=("Candara Light", 8), bg="#EDBFBF", command=siguiente_1)

#Colocación de widgets
title_lbl.place(x=60, y=10)
slogan_lbl.place(x=115, y=50)
logo_lbl.place(x=30, y=52)
welcome_lbl.place(x=82, y=210)
name_lbl.place(x=20, y=250)
number_lbl.place(x=20, y=290)
contacts_msg.place(x=20, y=330)
name_ent.place(x=115, y=250)
number_ent.place(x=115, y=290)
contacts_ent.place(x=115, y=350)
final_lbl.place(x=15, y=400)
sig_btn.place(x=110,y=440)


v_01.mainloop()
