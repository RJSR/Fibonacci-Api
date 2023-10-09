# Programación Dinámica mediante la creación de una API
Aplicación realizada en `Python 3.11` que resuelve la serie de Fibonacci a través una API creada mediante la librería Flask.

## Librerías Usadas

### Flask
Librería usada para la creación de aplicaciones web, se instala con:
```
pip install flask
```

## Problema a Solucionar
Creación de un API que implemente el cálculo de la secuencia de Fibonacci utilizando programación dinámica. La API debe aceptar un número n como parámetro y devolver el n-ésimo término de la secuencia de Fibonacci.

## ¿Cómo Funciona?
Mediante el método `POST` del api creado en `app.py`, se envía el número ingresado en el campo de home.html al interactuar con el botón de enviar, luego se procede a hacer un request para obtener dicho número.
A continuación, se transforma el elemento a int, y procede a hacer las verificaciones para realizar Fibonacci de manera iterativa, en donde computa el siguiente número, recordando el anterior.
Finalmente se guarda el valor en una variable al momento de renderizar `resultado.html`, la cual es llamada dentro de ella para mostrar el resultado.

![Api-fibonacci](https://github.com/RJSR/Fibonacci-Api/assets/78589528/7f1bd340-8d07-46fd-895a-8782f2a6197c)

## Puntos a Mejorar
- Mostrar el término ingresado en home.html al momento de obtener la respuesta.
- Realizar el proceso en un solo template.html.
- Mensaje de validación al momento de dejar el campo en blanco.
- Eliminar límite de 4300 dígitos al momento de mostrar la respuesta del api en resultado.html para términos muy grandes de Fibonacci.
