using System;

class Nodo
{
    public int valor;
    public Nodo izquierdo, derecho;

    public Nodo(int item)
    {
        valor = item;
        izquierdo = derecho = null;
    }
}

class ArbolBinario
{
    public Nodo raiz;

    public ArbolBinario()
    {
        raiz = null;
    }

    public void Insertar(int valor)
    {
        raiz = InsertarRecursivo(raiz, valor);
    }

    private Nodo InsertarRecursivo(Nodo raiz, int valor)
    {
        if (raiz == null)
        {
            raiz = new Nodo(valor);
            return raiz;
        }

        if (valor < raiz.valor)
            raiz.izquierdo = InsertarRecursivo(raiz.izquierdo, valor);
        else if (valor > raiz.valor)
            raiz.derecho = InsertarRecursivo(raiz.derecho, valor);

        return raiz;
    }

    public void RecorridoPreorden()
    {
        RecorridoPreordenRecursivo(raiz);
    }

    private void RecorridoPreordenRecursivo(Nodo raiz)
    {
        if (raiz != null)
        {
            Console.Write(raiz.valor + " ");
            RecorridoPreordenRecursivo(raiz.izquierdo);
            RecorridoPreordenRecursivo(raiz.derecho);
        }
    }

    public void RecorridoInorden()
    {
        RecorridoInordenRecursivo(raiz);
    }

    private void RecorridoInordenRecursivo(Nodo raiz)
    {
        if (raiz != null)
        {
            RecorridoInordenRecursivo(raiz.izquierdo);
            Console.Write(raiz.valor + " ");
            RecorridoInordenRecursivo(raiz.derecho);
        }
    }

    public void RecorridoPostorden()
    {
        RecorridoPostordenRecursivo(raiz);
    }

    private void RecorridoPostordenRecursivo(Nodo raiz)
    {
        if (raiz != null)
        {
            RecorridoPostordenRecursivo(raiz.izquierdo);
            RecorridoPostordenRecursivo(raiz.derecho);
            Console.Write(raiz.valor + " ");
        }
    }

    public bool Buscar(int valor)
    {
        return BuscarRecursivo(raiz, valor);
    }

    private bool BuscarRecursivo(Nodo raiz, int valor)
    {
        if (raiz == null)
            return false;

        if (valor == raiz.valor)
            return true;

        if (valor < raiz.valor)
            return BuscarRecursivo(raiz.izquierdo, valor);
        else
            return BuscarRecursivo(raiz.derecho, valor);
    }
}

class Programa
{
    static void Main(string[] args)
    {
        ArbolBinario arbol = new ArbolBinario();
        int opcion, valor;

        do
        {
            Console.WriteLine("\nÁrbol Binario de Búsqueda");
            Console.WriteLine("1. Insertar un nodo");
            Console.WriteLine("2. Buscar un nodo");
            Console.WriteLine("3. Mostrar recorrido Preorden");
            Console.WriteLine("4. Mostrar recorrido Inorden");
            Console.WriteLine("5. Mostrar recorrido Postorden");
            Console.WriteLine("6. Salir");
            Console.Write("Seleccione una opción: ");
            opcion = Convert.ToInt32(Console.ReadLine());

            switch (opcion)
            {
                case 1:
                    Console.Write("Ingrese un valor para insertar: ");
                    valor = Convert.ToInt32(Console.ReadLine());
                    arbol.Insertar(valor);
                    Console.WriteLine($"Valor {valor} insertado.");
                    break;

                case 2:
                    Console.Write("Ingrese el valor a buscar: ");
                    valor = Convert.ToInt32(Console.ReadLine());
                    if (arbol.Buscar(valor))
                        Console.WriteLine($"El valor {valor} fue encontrado.");
                    else
                        Console.WriteLine($"El valor {valor} no se encuentra en el árbol.");
                    break;

                case 3:
                    Console.WriteLine("Recorrido Preorden:");
                    arbol.RecorridoPreorden();
                    Console.WriteLine();
                    break;

                case 4:
                    Console.WriteLine("Recorrido Inorden:");
                    arbol.RecorridoInorden();
                    Console.WriteLine();
                    break;

                case 5:
                    Console.WriteLine("Recorrido Postorden:");
                    arbol.RecorridoPostorden();
                    Console.WriteLine();
                    break;

                case 6:
                    Console.WriteLine("Saliendo...");
                    break;

                default:
                    Console.WriteLine("Opción no válida.");
                    break;
            }
        } while (opcion != 6);
    }
}
