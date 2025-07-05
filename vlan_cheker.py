try:
    vlan = int(input("Ingrese el número de VLAN: "))
    if 1 <= vlan <= 1005:
        print("VLAN dentro del rango normal")
    elif 1006 <= vlan <= 4094:
        print("VLAN en el rango extendido")
    else:
        print("VLAN inválida")
except ValueError:
    print("Debe ingresar un número entero")
