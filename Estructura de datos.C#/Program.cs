using System;

public class Program
{
    public static void Main()
    {
        int n = 3; // Número de discos
        char source = 'A'; // Torre de origen
        char auxiliary = 'B'; // Torre auxiliar
        char destination = 'C'; // Torre destino

        SolveHanoi(n, source, auxiliary, destination);
    }

    public static void SolveHanoi(int n, char source, char auxiliary, char destination)
    {
        if (n == 1)
        {
            Console.WriteLine($"Mover disco 1 desde {source} hasta {destination}");
            return;
        }

        SolveHanoi(n - 1, source, destination, auxiliary);
        Console.WriteLine($"Mover disco {n} desde {source} hasta {destination}");
        SolveHanoi(n - 1, auxiliary, source, destination);
    }
}
