using System;

class Nodo
{
    public string Titulo { get; set; } // Título de la revista
    public Nodo Izquierdo { get; set; } // Nodo  izquierdo
    public Nodo Derecho { get; set; }   // Nodo  derecho

    public Nodo(string titulo)
    {
        Titulo = titulo;
        Izquierdo = null;
        Derecho = null;
    }
}

class ArbolBinarioBusqueda
{
    private Nodo raiz;

    public ArbolBinarioBusqueda()
    {
        raiz = null;
    }

    // Método para insertar un título en el árbol binario
    public void Insertar(string titulo)
    {
        raiz = InsertarRecursivo(raiz, titulo);
    }

    private Nodo InsertarRecursivo(Nodo nodo, string titulo)
    {
        if (nodo == null)
        {
            return new Nodo(titulo);
        }

        // Comparar los títulos y colocar en el lado correspondiente
        if (string.Compare(titulo, nodo.Titulo, StringComparison.OrdinalIgnoreCase) < 0)
        {
            nodo.Izquierdo = InsertarRecursivo(nodo.Izquierdo, titulo);
        }
        else if (string.Compare(titulo, nodo.Titulo, StringComparison.OrdinalIgnoreCase) > 0)
        {
            nodo.Derecho = InsertarRecursivo(nodo.Derecho, titulo);
        }

        return nodo;
    }

    // Búsqueda iterativa 
    public bool BuscarIterativo(string titulo)
    {
        Nodo actual = raiz;

        while (actual != null)
        {
            if (actual.Titulo.Equals(titulo, StringComparison.OrdinalIgnoreCase))
            {
                return true;
            }

            if (string.Compare(titulo, actual.Titulo, StringComparison.OrdinalIgnoreCase) < 0)
            {
                actual = actual.Izquierdo;
            }
            else
            {
                actual = actual.Derecho;
            }
        }

        return false;
    }

    // Búsqueda recursiva 
    public bool BuscarRecursivo(Nodo nodo, string titulo)
    {
        if (nodo == null)
        {
            return false;
        }

        if (nodo.Titulo.Equals(titulo, StringComparison.OrdinalIgnoreCase))
        {
            return true;
        }

        if (string.Compare(titulo, nodo.Titulo, StringComparison.OrdinalIgnoreCase) < 0)
        {
            return BuscarRecursivo(nodo.Izquierdo, titulo);
        }
        else
        {
            return BuscarRecursivo(nodo.Derecho, titulo);
        }
    }

    // Obtener la raíz del árbol para la búsqueda recursiva
    public Nodo ObtenerRaiz()
    {
        return raiz;
    }

    // Menú principal
    public static void Main(string[] args)
    {
        ArbolBinarioBusqueda catalogo = new ArbolBinarioBusqueda();

        // Insertar 10 títulos 
        catalogo.Insertar("Ciencia Hoy");
        catalogo.Insertar("Ingeniería y Sociedad");
        catalogo.Insertar("Tecnología Moderna");
        catalogo.Insertar("Revista Informática");
        catalogo.Insertar("Electrónica Aplicada");
        catalogo.Insertar("Física Avanzada");
        catalogo.Insertar("Biología Moderna");
        catalogo.Insertar("Matemáticas Aplicadas");
        catalogo.Insertar("Revista Química");
        catalogo.Insertar("Arquitectura y Diseño");

        bool salir = false;

        while (!salir)
        {
            Console.WriteLine("Menú de búsqueda en el catálogo de revistas (Árbol Binario):");
            Console.WriteLine("1. Buscar título (iterativa)");
            Console.WriteLine("2. Buscar título (recursiva)");
            Console.WriteLine("3. Salir");
            Console.Write("Seleccione una opción: ");
            int opcion = int.Parse(Console.ReadLine());

            switch (opcion)
            {
                case 1:
                    Console.Write("Ingrese el título de la revista a buscar (iterativa): ");
                    string tituloIterativa = Console.ReadLine();
                    if (catalogo.BuscarIterativo(tituloIterativa))
                        Console.WriteLine("Encontrado");
                    else
                        Console.WriteLine("No encontrado");
                    break;

                case 2:
                    Console.Write("Ingrese el título de la revista a buscar (recursiva): ");
                    string tituloRecursiva = Console.ReadLine();
                    if (catalogo.BuscarRecursivo(catalogo.ObtenerRaiz(), tituloRecursiva))
                        Console.WriteLine("Encontrado");
                    else
                        Console.WriteLine("No encontrado");
                    break;

                case 3:
                    salir = true;
                    break;

                default:
                    Console.WriteLine("Opción no válida. Intente de nuevo.");
                    break;
            }
        }
    }
}
