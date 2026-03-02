name = input("Ingrese su nombre y apellido: ").strip()

while True:
    try:
        price = float(input("Ingrese el precio unitario del producto: "))

        if price < 0:
            print(
                "El precio no puede ser negativo. Por favor, ingrese un valor válido."
            )
            continue
        break

    except ValueError:
        print("Por favor, ingrese un número válido para el precio.")

while True:
    try:
        quantity = int(input("Ingrese la cantidad de productos: "))

        if quantity < 0:
            print(
                "La cantidad no puede ser negativa. Por favor, ingrese un valor válido."
            )
            continue
        break
    except ValueError:
        print("Por favor, ingrese un número válido para la cantidad.")

while True:
    vip = input("Es cliente VIP? (Si/No): ").lower().strip()

    if vip != "si" and vip != "no":
        print("Por favor, ingrese 'Si' o 'No' para indicar si es cliente VIP.")
        continue
    break

subtotal = price * quantity

if vip == "si":
    discount = subtotal * 0.1
else:
    discount = 0

total = subtotal - discount

# Resumen de la venta

print("\n############################\n")
print("Resumen de la venta:\n")
print(f"Cliente: {name}\n")
print(f"Precio unitario: ${price}\n")
print(f"Cantidad: {quantity}\n")
print(f"Subtotal: ${subtotal}\n")
print(f"Descuento VIP: ${discount}\n")
print(f"Total a pagar: ${total}")
print("\n############################\n")
