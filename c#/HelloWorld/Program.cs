using System;

namespace HelloWorld
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string filePath = "output.txt";
            string content = "Hello World!";
            File.WriteAllText(filePath, content);
        }
    }
}
