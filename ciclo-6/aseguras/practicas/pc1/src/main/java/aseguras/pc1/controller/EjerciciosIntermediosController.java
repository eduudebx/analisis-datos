package aseguras.pc1.controller;

import aseguras.pc1.model.Estudiante;
import aseguras.pc1.service.EjerciciosIntermediosService;
import aseguras.pc1.util.Response;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/ejintermedios")
public class EjerciciosIntermediosController {
    
    private final EjerciciosIntermediosService ejerciciosIntermediosService;

    public EjerciciosIntermediosController(EjerciciosIntermediosService ejerciciosIntermediosService) {
        this.ejerciciosIntermediosService = ejerciciosIntermediosService;
    }
    
    
    /**
    * Realiza la autenticación de un usuario utilizando un archivo de texto plano. El resultado de la autenticación 
    * se devuelve como una cadena de texto que indica si la autenticación fue exitosa o fallida, dependiendo de las 
    * credenciales proporcionadas.
    *
    * @param username El nombre de usuario que se va a autenticar.
    * @param password La contraseña del usuario para la autenticación.
    * @return Un objeto `Response<String>` que contiene el resultado de la autenticación.
    */
    @GetMapping(value = "ej1")
    public Response<String> autenticacionArchivoTextoPlano(
            @RequestParam String username, @RequestParam String password){
        String resultado = ejerciciosIntermediosService
                .autenticacionArchivoTextoPlano(username, password);
        return new Response<>("Autenticación archivo texto plano.", resultado);
    }
    
    
    /**
    * Realiza una consulta a la base de datos utilizando un `PreparedStatement` para obtener los datos de un estudiante.
    * El servicio utiliza un `PreparedStatement` para consultar la base de datos en busca de un estudiante con la cédula 
    * proporcionada.
    * 
    * @param cedula La cédula del estudiante que se va a consultar en la base de datos.
    * @return Un objeto `Response<Estudiante>` que contiene un mensaje de estado y el objeto `Estudiante` con los datos 
    *           del estudiante o `null` si no se encuentra.
    */
    @GetMapping(value = "ej2")
    public Response<Estudiante> consultaPreparedStatement(@RequestParam String cedula){
        Estudiante estudiante = ejerciciosIntermediosService
                .consultaPreparedStatement(cedula);
        String mensaje = "Conexión BD Ok!";
        if(estudiante == null){mensaje = "Credenciales incorrectas!";}
        return new Response<>(mensaje, estudiante);
    }
}
