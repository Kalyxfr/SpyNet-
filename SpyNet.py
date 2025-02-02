import requests
from colorama import init, Fore, Back, Style

init(autoreset=True)

def verifier_entetes_securite(url):
    try:
        response = requests.get(url)
        headers = response.headers

        entetes_securite = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Referrer-Policy",
            "Permissions-Policy",
            "Feature-Policy",
            "Expect-CT",
            "Public-Key-Pins",
            "Server",
            "Set-Cookie",
            "Cache-Control",
            "Pragma",
            "Expires",
            "Access-Control-Allow-Origin",
            "Access-Control-Allow-Methods",
            "Access-Control-Allow-Headers",
            "Access-Control-Max-Age",
            "Access-Control-Expose-Headers",
            "Accept-Ranges",
            "Age",
            "Allow",
            "Alt-Svc",
            "Connection",
            "Content-Encoding",
            "Content-Language",
            "Content-Length",
            "Content-Location",
            "Content-MD5",
            "Content-Range",
            "Content-Type",
            "Date",
            "ETag",
            "Last-Modified",
            "Link",
            "Location",
            "Proxy-Authenticate",
            "Retry-After",
            "Server-Timing",
            "Trailer",
            "Transfer-Encoding",
            "Upgrade",
            "Vary",
            "Via",
            "Warning",
            "WWW-Authenticate",
            "X-DNS-Prefetch-Control",
            "X-Permitted-Cross-Domain-Policies",
            "X-Powered-By",
            "X-UA-Compatible",
            "Accept-Patch",
            "Accept-Push-Policy",
            "Accept-Signature",
            "Alt-Used",
            "Content-Security-Policy-Report-Only",
            "Digest",
            "Early-Data",
            "Expect",
            "Forwarded",
            "Host",
            "If-Match",
            "If-Modified-Since",
            "If-None-Match",
            "If-Range",
            "If-Unmodified-Since",
            "Max-Forwards",
            "Origin",
            "Pragma",
            "Prefer",
            "Range",
            "Save-Data",
            "Sec-WebSocket-Accept",
            "Server-Timing",
            "SourceMap",
            "Strict-Transport-Security",
            "TE",
            "Timing-Allow-Origin",
            "Tk",
            "Upgrade-Insecure-Requests",
            "User-Agent",
            "X-Content-Duration",
            "X-Content-Type-Options",
            "X-Download-Options",
            "X-Forwarded-For",
            "X-Forwarded-Host",
            "X-Forwarded-Proto",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Access-Control-Allow-Credentials",
            "Cross-Origin-Resource-Policy",
            "NEL",
            "Report-To",
            "Sec-Fetch-Dest",
            "Sec-Fetch-Mode",
            "Sec-Fetch-Site",
            "Sec-Fetch-User"
        ]

        print(f"{Fore.RED}{Style.BRIGHT}En-têtes de sécurité pour {url}:\n")

        for entete in entetes_securite:
            if entete in headers:
                print(f"{Fore.RED}{Style.BRIGHT}{entete}: {headers[entete]}")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}{entete} est manquant!")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}{Style.BRIGHT}Erreur lors de la vérification de {url}: {e}")

if __name__ == "__main__":
    url = input(f"{Fore.RED}{Style.BRIGHT}Entrez l'URL du site à vérifier: ")
    verifier_entetes_securite(url)