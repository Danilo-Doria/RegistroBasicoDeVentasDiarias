name = str(input("Ingrese su nombre y apellido: "))
price = float(input("Ingrese el precio unitario del producto: "))
quantity = int(input("Ingrese la cantidad de productos: "))
vip = str(input("Es cliente VIP? (Si/No): "))

subtotal = price * quantity

if vip.lower() == "si":
    discount = subtotal * 0.1
else:    discount = 0

total = subtotal - discount