<div align="center">

# 🧾 Registro Básico de Ventas Diarias

**Herramienta de Punto de Venta (POS) y Facturación Diaria para RiwiTechStore en Python**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

</div>

---

## 📖 Descripción

**Registro Básico de Ventas Diarias** es una herramienta de terminal desarrollada en **Python 3** diseñada para registrar, validar y procesar ventas comerciales diarias en **RiwiTechStore**.

El sistema guía al vendedor paso a paso en el registro del cliente, validando de forma rigurosa precios unitarios y cantidades, aplicando beneficios comerciales como descuentos automáticos para clientes VIP y emitiendo un ticket resumen estructurado.

---

## 🚀 Características Principales

- **Validación Rigurosa de Entradas:**
  - Control de precio unitario positivo (`float`).
  - Control de cantidad de unidades positiva (`int`).
  - Prevención de caídas de ejecución ante datos alfanuméricos inválidos mediante `try / except ValueError`.
- **Detección y Descuento de Clientes VIP:**
  - Identificación interactiva de membresía VIP (`Si` / `No`).
  - Cálculo y aplicación automática de un **10% de descuento** sobre el subtotal de la compra.
- **Generación de Ticket Resumen:**
  - Detalle formateado que incluye: Nombre del Cliente, Precio Unitario, Cantidad, Subtotal acumulado, Descuento VIP aplicado y Total neto a pagar.

---

## 📂 Estructura del Proyecto

```text
RegistroBasicoDeVentasDiarias/
├── LICENSE                 # Licencia MIT
├── README.md               # Documentación del proyecto
└── registration.py         # Script principal de captura, cálculo y facturación
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**

---

## ⚙️ Puesta en Marcha

### 1. Clonar el repositorio
```bash
git clone https://github.com/Danilo-Doria/RegistroBasicoDeVentasDiarias.git
cd RegistroBasicoDeVentasDiarias
```

### 2. Ejecutar el script
```bash
python3 registration.py
```

### 3. Ejemplo de Salida
```text
Ingrese su nombre y apellido: Juan Pérez
Ingrese el precio unitario del producto: 50.0
Ingrese la cantidad de productos: 2
Es cliente VIP? (Si/No): si

############################

Resumen de la venta:

Cliente: Juan Pérez
Precio unitario: $50.0
Cantidad: 2
Subtotal: $100.0
Descuento VIP: $10.0
Total a pagar: $90.0

############################
```

---

## 👨💻 Author

- GitHub: **[Danilo-Doria](https://github.com/Danilo-Doria)**
- LinkedIn: **[Danilo Doria Diaz](https://www.linkedin.com/in/danilo-doria-diaz)**
- Mail: **danilodoria519@gmail.com**

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
