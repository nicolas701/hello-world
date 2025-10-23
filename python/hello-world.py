import cowsay
import sys

def format_greeting(name="World"):
    """Prepara un saludo."""
    return f"Hello, {name}!"

def main():
    """Función principal que imprime el saludo."""
    # Revisa si se pasó un argumento al correr el script
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    
    greeting = format_greeting(name)
    cowsay.cow(greeting)

if __name__ == "__main__":
    main()