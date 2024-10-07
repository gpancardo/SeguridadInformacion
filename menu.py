import redireccion
print("""
-----------------------------------------------------------------
    ██████████                
  ████      ████             Seguridad de la Información 
  ██          ██              
  ██          ██             Pancardo Ortega Germán Heberto   
██████████████████           
██████████████████           
████████▒▒████████           --o Iniciar Sesión (I)
████████  ████████           --o Registrar Cuenta (R)
████████░░████████           --o Salir (S)
  ██████████████   
-----------------------------------------------------------------
""")

opcion=input("--o ")
opcion=opcion.upper()

if (opcion=="I"):
    redireccion.redireccion("inicioSesion")
elif (opcion=="R"):
    redireccion.redireccion("registro")
else:
    print("Regresa pronto!")
    redireccion.redireccion("salir")