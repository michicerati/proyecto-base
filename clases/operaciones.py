class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0
        
    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1:"))
                break
            except Exception:
                print("Número inválido")
                continue
        while True:
            try:
                self.num2 = int(input("Número 2:"))
                break
            except Exception:
                print("Número inválido")
                continue    
    
    def sumar(self):
        self.resultado = f"La suma de {self.num1} + {self.num2} es igual a {self.num1 + self.num2}"
    
    def restar(self):
        self.resultado = f"La resta de {self.num1} - {self.num2} es igual a {self.num1 - self.num2}"

    def multiplicar(self):
        self.resultado = f"El producto de {self.num1} * {self.num2} es igual a {self.num1 * self.num2}"

    def dividir(self):
        try:
            self.resultado = f"La división de {self.num1} / {self.num2} es igual a {self.num1 / self.num2}"
        except ZeroDivisionError:
            self.resultado = "Error: No se puede dividir entre cero."

    def modulo(self):
        try:
            self.resultado = f"El módulo de {self.num1} % {self.num2} es igual a {self.num1 % self.num2}"
        except ZeroDivisionError:
            self.resultado = "Error: No se puede calcular el módulo con divisor cero."

    def mostrarResultado(self):
        print(self.resultado)

# Ejemplo de uso tipo calculadora:
if __name__ == "__main__":
    op = Operaciones()
    op.leerNumeros()
    print("Elige operación: 1) Sumar 2) Restar 3) Multiplicar 4) Dividir 5) Módulo")
    opcion = input("Opción: ")
    if opcion == "1":
        op.sumar()
    elif opcion == "2":
        op.restar()
    elif opcion == "3":
        op.multiplicar()
    elif opcion == "4":
        op.dividir()
    elif opcion == "5":
        op.modulo()
    else:
        print("Opción inválida")
        exit()
    op.mostrarResultado()

