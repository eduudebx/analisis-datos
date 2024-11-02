package aseguras.p1.intermedios;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class EjIntermediosService {
    
    public boolean autenticarEnArchivoTextoPlano(String usuario, String contrasena) {
        try (BufferedReader archivo = new BufferedReader(new FileReader("usuarios.txt"))) {
            String registro;
            while ((registro = archivo.readLine()) != null) {
                String[] datos = registro.split(",");
                if (datos.length == 2) {
                    if (usuario.equals(datos[0]) && contrasena.equals(datos[1])) {
                        return true;
                    }
                }
            }
        } catch (IOException e) {
            System.err.println("Error al leer el archivo: " + e.getMessage());
        }
        return false;
    }
    
    
    
}
