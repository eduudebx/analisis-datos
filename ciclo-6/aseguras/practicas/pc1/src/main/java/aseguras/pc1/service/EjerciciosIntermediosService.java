package aseguras.pc1.service;

import aseguras.pc1.model.Estudiante;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import org.springframework.stereotype.Service;


@Service
public class EjerciciosIntermediosService {
    
    
    /**
    * Autentica a un usuario leyendo las credenciales desde un archivo de texto plano.
    *
    * Esta función verifica si el nombre de usuario y la contraseña proporcionados
    * coinciden con los almacenados en un archivo llamado "usuarios.txt", el cual
    * se encuentra en el directorio de recursos del proyecto. El archivo de texto
    * debe tener el formato "usuario;contraseña" por cada línea.
    *
    * @param username El nombre de usuario a autenticar.
    * @param password La contraseña del usuario.
    * @return Un mensaje que indica el resultado de la autenticación. Si el
    *         usuario es encontrado y la contraseña es correcta, se devuelve
    *         "Autenticación exitosa!". Si la contraseña es incorrecta, se
    *         devuelve "Contraseña incorrecta!". Si el usuario no se encuentra
    *         en el archivo, se devuelve "Usuario no encontrado!". En caso de
    *         un error de lectura del archivo, se devuelve un mensaje de error
    *         con detalles del fallo.
    */
    public String autenticacionArchivoTextoPlano(String username, String password) {
        String archivo = "usuarios.txt";
        String resultado = "Usuario no encontrado!";

        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(getClass().getClassLoader().getResourceAsStream(archivo), StandardCharsets.UTF_8))) {

            if (reader == null) {
                throw new IOException("No se pudo encontrar el archivo " + archivo);
            }

            String linea;
            while ((linea = reader.readLine()) != null) {
                String[] credenciales = linea.split(";");

                if (credenciales.length == 2) {
                    String user = credenciales[0].trim();
                    String pass = credenciales[1].trim();

                    if (username.equals(user)) {
                        if (password.equals(pass)) {
                            return "Autenticación exitosa!";
                        } else {
                            return "Contraseña incorrecta!";
                        }
                    }
                }
            }

        } catch (IOException e) {
            resultado = "Error al leer el archivo de usuarios: " + e.getMessage();
        }

        return resultado;
    }
    

    /**
    * Realiza una consulta a la base de datos para obtener los datos de un estudiante
    * basados en su cédula utilizando un `PreparedStatement`.
    *
    * Esta función se conecta a una base de datos MySQL, ejecuta una consulta para
    * buscar los detalles de un estudiante con la cédula proporcionada y retorna un
    * objeto `Estudiante` con los datos recuperados de la base de datos.
    *
    * @param cedula La cédula del estudiante que se desea consultar en la base de datos.
    * @return Un objeto `Estudiante` con los datos recuperados de la base de datos, o `null`
    *         si no se encuentra ningún estudiante con la cédula proporcionada o si ocurre un error.
    */
    public Estudiante consultaPreparedStatement(String cedula) {
        String url = "jdbc:mysql://localhost:3306/aseguras_p1_test_1";
        String usuario = "ista";
        String contraseña = "";

        Estudiante estudiante = null;

        String query = "SELECT id, cedula, direccion, nombres, edad FROM estudiante WHERE cedula = ?";

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
