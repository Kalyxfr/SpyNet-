using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task VerifierEntetesSecurite(string url)
    {
        using (var client = new HttpClient())
        {
            try
            {
                var response = await client.GetAsync(url);
                var headers = response.Headers;
                Console.WriteLine($"En-têtes de sécurité pour {url}:\n");

                List<string> entetesSecurite = new List<string>
                {
                    "Content-Security-Policy", "Strict-Transport-Security", "X-Content-Type-Options",
                    "X-Frame-Options", "X-XSS-Protection"
                };

                foreach (var entete in entetesSecurite)
                {
                    if (headers.Contains(entete))
                    {
                        Console.WriteLine($"{entete}: {string.Join(", ", headers.GetValues(entete))}");
                    }
                    else
                    {
                        Console.WriteLine($"{entete} est manquant!");
                    }
                }
            }
            catch (HttpRequestException e)
            {
                Console.WriteLine($"Erreur lors de la vérification de {url}: {e.Message}");
            }
        }
    }

    static void Main(string[] args)
    {
        Console.Write("Entrez l'URL du site à vérifier: ");
        string url = Console.ReadLine();
        VerifierEntetesSecurite(url).Wait();
    }
}