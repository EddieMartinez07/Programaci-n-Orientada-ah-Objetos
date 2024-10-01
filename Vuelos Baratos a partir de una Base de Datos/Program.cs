using System;
using System.Collections.Generic;
using System.Linq;

class Flight
{
    public string Origin { get; set; }
    public string Destination { get; set; }
    public decimal Price { get; set; }
    public DateTime Date { get; set; }
}

class Program
{
    static void Main()
    {
        var flights = new List<Flight>
        {
            new Flight { Origin = "Quito", Destination = "Guayaquil", Price = 150, Date = DateTime.Today },
            new Flight { Origin = "Quito", Destination = "Guayaquil", Price = 100, Date = DateTime.Today.AddDays(1) },
            new Flight { Origin = "Quito", Destination = "Guayaquil", Price = 120, Date = DateTime.Today.AddDays(2) }
        };

        var cheapestFlight = flights
            .Where(f => f.Origin == "Quito" && f.Destination == "Guayaquil")
            .OrderBy(f => f.Price)
            .FirstOrDefault();

        if (cheapestFlight != null)
        {
            Console.WriteLine($"Vuelo más barato de Quito a Guayaquil: Precio {cheapestFlight.Price}");
        }
    }
}
