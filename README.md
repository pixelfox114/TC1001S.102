Calculador de Geometria
Este es un proyecto sencillo de Python para calcular el area y el perimetro/circunferencia de triangulos,
rectángulos y circulos a partir de un archivo CSV.
El archivo CSV, debe llamarse: "figuras.csv", debe tener el siguiente formato: la primera columna contiene el tipo de forma: 
c para circulo, t para triangulo o r para rectangulo. 
La segunda columna contiene la base para rectangulos y triangulos, o el radio para circulos. *Importante notar que el programa asume que todos
los triangulos son rectangulos. 
La tercera columna contiene la altura para rectangulos y triangulos; esta se ignora para circulos.
El proyecto esta listo para ejecutarse y no requiere compilacion. Requiere Python 3 y las bibliotecas math (integrada)
y pandas. Si se ejecuta en Ubuntu, recomendable usar un entorno virtual para evitar conflictos de pip en todo el sistema. (Utilizando venv)
Si no sabes utilizar venv, buscalo en google.
Para usar el proyecto, coloque el archivo CSV en la carpeta del proyecto y ejecute el script principal con "python3 leer.py". 
El programa imprimira el nombre, area y el perimetro/circunferencia de cada forma de la tabla.
Permisos: Se permite el uso comercial, la distribución, la modificación y el uso privado.
Aviso legal: No me hago responsable de ningun problema causado por este proyecto. El proyecto se proporciona tal cual, sin garantía.
