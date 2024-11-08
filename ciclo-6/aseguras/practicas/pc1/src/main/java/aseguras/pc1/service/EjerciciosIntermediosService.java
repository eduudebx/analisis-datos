package aseguras.pc1.service;

import aseguras.pc1.model.Estudiante;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import org.springframework.stereotype.Service;


@Service
public class EjerciciosIntermediosService {
    
    
    public String autenticacionArchivoTextoPlano(String username, String password) {
        String archivo = "usuarios.txt";
        String resultado = "Usuario no encontrado!";

        try {
            List<String> lineas = Files.readAllLines(Paths.get(archivo));

            for (String linea : lineas) {
                String[] credenciales = linea.split(";");

                if (credenciales.length == 2) {
                    String user = credenciales[0].trim();
                    String pass = credenciales[1].trim();

                    if (username.equals(user)) {
                        if (password.equals(pass)) {
                            resultado = "Autenticación exitosa!";
                        } else {
                            resultado = "Contraseña incorrecta!";
                        }
                        break;
                    }
                }
            }
        } catch (IOException e) {
            System.out.println("\nError en autenticacionArchivoTextoPlano(String username, String password):\n" 
                    + e.getMessage());
        }
        return resultado;
    }
    

    public Estudiante consultaPreparedStatement(String cedula) {
        String url = "jdbc:mysql://localhost:3306/aseguras_p1_test_1";
        String usuario = "ista";
        String contraseña = "";

        Estudiante estudiante = null;

        String query = "SELECT id, cedula, direccion, nombres, edad FROM Estudiante WHERE cedula = ?";

        try (Connection conn = DriverManager.getConnection(url, usuario, contraseña);
             PreparedStatement pstmt = conn.prepareStatement(query)) {

            pstmt.setString(1, cedula);

            try (ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    estudiante = new Estudiante();
                    estudiante.setId(rs.getInt("id"));
                    estudiante.setCedula(rs.getString("cedula"));
                    estudiante.setDireccion(rs.getString("direccion"));
                    estudiante.setNombres(rs.getString("nombres"));
                    estudiante.setEdad(rs.getInt("edad"));
                }
            }
        } catch (SQLException e) {
            System.out.println("\nError en consultaPreparedStatement(String cedula):\n" + e.getMessage());
        }

        return estudiante;
    }

}
