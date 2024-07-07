using System;

public class Node
{
    public int Data;
    public Node Next;

    public Node(int data)
    {
        Data = data;
        Next = null;
    }
}

public class LinkedList
{
    private Node head;

    public LinkedList()
    {
        head = null;
    }

    public void Append(int data)
    {
        Node newNode = new Node(data);
        if (head == null)
        {
            head = newNode;
            return;
        }
        Node last = head;
        while (last.Next != null)
        {
            last = last.Next;
        }
        last.Next = newNode;
    }

    public void PrintList()
    {
        Node current = head;
        while (current != null)
        {
            Console.Write(current.Data + " ");
            current = current.Next;
        }
        Console.WriteLine();
    }

    public void Invertir()
    {
        Node prev = null;
        Node current = head;
        Node next = null;
        while (current != null)
        {
            next = current.Next;
            current.Next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }

    public int Search(int data)
    {
        Node current = head;
        int count = 0;

        while (current != null)
        {
            if (current.Data == data)
            {
                count++;
            }
            current = current.Next;
        }

        if (count == 0)
        {
            Console.WriteLine("El dato no fue encontrado");
        }

        return count;
    }
}

class Program
{
    static void Main()
    {
        LinkedList llist = new LinkedList();

        // Crear una lista enlazada y agregar elementos
        int[] values = { 1, 2, 3, 4, 5, 3, 3 };
        foreach (int value in values)
        {
            llist.Append(value);
        }

        Console.WriteLine("Lista original:");
        llist.PrintList();

        // Invertir la lista
        llist.Invertir();
        Console.WriteLine("Lista invertida:");
        llist.PrintList();

        // Buscar un elemento en la lista
        int datoABuscar = 3;
        int resultado = llist.Search(datoABuscar);
        if (resultado > 0)
        {
            Console.WriteLine($"El dato {datoABuscar} se encuentra {resultado} veces en la lista.");
        }
    }
}
