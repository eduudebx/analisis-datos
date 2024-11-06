package aseguras.p1.service;

import aseguras.p1.model.Estudiante;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import org.springframework.stereotype.Service;

@Service
public class EjIntermediosService {
    
    public boolean autenticarEnArchivoTextoPlano(String usuario, String contrasena) {
        try (BufferedReader archivo = new BufferedReader(new InputStreamReader(getClass().getClassLoader().getResourceAsStream("usuarios.txt")))) {
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
    
    
    private Connection getConnection() throws SQLException {
        String url = "jdbc:mysql://localhost:3306/aseguras_p1"; 
        String usuario = "ista";
        String contrasena = "";

        return DriverManager.getConnection(url, usuario, contrasena);
    }
    
    
    public Estudiante buscarEstudiantePorCedula(String cedula) {
        Estudiante estudiante = null;
        String query = "SELECT * FROM estudiante WHERE cedula = ?";

        try (Connection conn = getConnection();
            PreparedStatement stmt = conn.prepareStatement(query)) {
            stmt.setString(1, cedula);
            ResultSet rs = stmt.executeQuery();
            
            if (rs.next()) {
                estudiante = new Estudiante(
                        rs.getLong("idestudiante"),
                        rs.getString("cedula"),
                        rs.getString("nombres"),
                        rs.getString("direccion"),
                        rs.getString("correo"),
                        rs.getString("telefono"),
                        rs.getInt("edad")
                );
            }
        } catch (SQLException e) {
            System.err.println("Error al conectarse a la BD: " + e.getMessage());
        }

        return estudiante;
    }
}
