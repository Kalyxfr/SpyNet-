import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.List;
import java.util.Map;

public class VerifierEntetesSecurite {
    public static void verifierEntetesSecurite(String url) throws IOException {
        HttpURLConnection connection = (HttpURLConnection) new URL(url).openConnection();
        connection.setRequestMethod("GET");

        System.out.println("En-têtes de sécurité pour " + url + ":\n");

        Map<String, List<String>> headers = connection.getHeaderFields();
        String[] entetesSecurite = {
            "Content-Security-Policy", "Strict-Transport-Security", "X-Content-Type-Options",
            "X-Frame-Options", "X-XSS-Protection"
        };

        for (String entete : entetesSecurite) {
            if (headers.containsKey(entete)) {
                System.out.println(entete + ": " + headers.get(entete));
            } else {
                System.out.println(entete + " est manquant!");
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.out.print("Entrez l'URL du site à vérifier: ");
        String url = new java.util.Scanner(System.in).nextLine();
        verifierEntetesSecurite(url);
    }
}
