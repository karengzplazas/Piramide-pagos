import json

try:
    with open("empleados.json", "r") as archivo:
        empleados = json.load(archivo)
except (FileNotFoundError, json.JSONDecodeError):
    empleados = {}

print("Bienvenido al sistema de cálculo de pagos de la Pirámide de la Sabiduría\n")
while True:
    print("\nCalculadora de Pagos - Pirámide de la Sabiduría")
    nombre = input("\nIngrese el nombre del trabajador (o escriba 'salir' para terminar): ").strip()
    if nombre.lower() == "salir":
        print("Fin del programa.")
        break

    nombre = nombre.capitalize()
    print(f"Saludos, Señor(a) {nombre}. ¡Espero se encuentre bien!👌\n")

    try:
        horas = int(input("Ingrese las horas trabajadas: "))
        tarifa = int(input("Ingrese la tarifa por hora: "))
        tardanzas = int(input("Ingrese el número de veces que llegó tarde: "))
    except ValueError:
        print("Error: Ingrese solo números válidos.")
        continue

    extras = 0
    pago_total = horas * tarifa

    if horas > 40:
        extras = horas - 40
        pago_extras = extras * (tarifa * 1.2)
        sueldo_bruto = (40 * tarifa) + pago_extras
        print(f"\n💡 Señor (a) {nombre}, usted trabajó {extras} horas extras y recibirá un pago adicional de ${pago_extras:,.2f}.")
    else:
        sueldo_bruto = horas * tarifa
        print(f"\n🔹 {nombre}, usted no trabajó horas extras.")

    bonificacion = 0
    if sueldo_bruto > 600000:
        bonificacion = 50000
        print(f"¡Felicidades🥳 Señor(a) {nombre}! Recibirá un bono de ${bonificacion:,.2f} por su buen desempeño")

    descuento = 0
    if tardanzas >= 3:
        descuento = sueldo_bruto * 0.05
        print(f"⚠️ Descuento aplicado por tardanzas: ${descuento:,.2f}")

    sueldo_neto = sueldo_bruto + bonificacion - descuento

    print("\nResumen del Salario")
    print(f"Trabajador: {nombre}")
    print(f"Horas trabajadas: {horas}")
    print(f"Horas extras: {extras}")
    print(f"Sueldo bruto: ${sueldo_bruto:,.0f}")
    print(f"Bonificación: ${bonificacion:,.0f}")
    print(f"Descuento por tardanzas: ${descuento:,.0f}")
    print(f"Sueldo neto: ${sueldo_neto:,.0f}")
    print("------------------------------------------------------")
