
# Ejecución
Esto no es un api, es un programa python básico
Para ejecutar, ejecutar el archivo main.py desde vscode o con:

`python main.py`

# Estructura de carpetas
La estructura de carpetas es la siguiente:

├── model
│   ├── uber
│   │   └── dto.py
│   └── otro
│       └── dto.py
├── function
│   ├── uber
│   │   └── get_data.py
│   └── otro
│       └── get_data.py
├── json_examples
│   ├── uber
│   │   ├── user.json
│   │   ├── vehicle.json
│   │   └── ... .json
│   └── otro
│       ├── example1.json
│       ├── example2.json
│       └── ....json
└── main.py

### Descripción de archivos
La aplicación se divide en 3 carpetas y un main.py:

* model: definición del modelo, vale decir, las clases de la aplicación
* function: la parte funcional de la aplicación, ejecución de código y lógica
* json_examples: sencillamente ejemplos .json del modelo
* main.py: punto de inicio de la aplicación, llama a todas las otras carpetas y archivos

Cada subcarpeta se divide ademas en subcarpetas donde cada una representa un "dominio", valer decir, en la carpeta "uber" de la carpeta model están todas las clases de uber, si agrego datos de una aplicación tipo instagram, al lado de la carpeta uber habría una carpeta instagram.
