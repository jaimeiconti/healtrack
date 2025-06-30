from flask import Flask, render_template, request

app = Flask(__name__)

class Usuario:
    def __init__(self, nombre: str, peso: float):
        self.nombre = nombre
        self.peso = peso

    def get_nombre(self):
        return self.nombre
    
    def get_peso(self):
        return self.peso
    
    def actualizar_peso(self, nuevo_peso: float):
        self.peso = nuevo_peso

    def mostrar_informacion(self) -> str:
        return f"Usuario: {self.nombre}, Peso Actual: {self.peso} kg"


@app.route("/", methods=["GET", "POST"])
def formulario():
    mensaje = ""
    if request.method == "POST":
        nombre = request.form["nombre"]
        peso = float(request.form["peso"])  # Sin validación
        usuario = Usuario(nombre, peso)
        usuario.actualizar_peso(peso)
        mensaje = usuario.mostrar_informacion()
    return render_template("formulario.html", resultado=mensaje)

if __name__ == "__main__":
    app.run(debug=True)