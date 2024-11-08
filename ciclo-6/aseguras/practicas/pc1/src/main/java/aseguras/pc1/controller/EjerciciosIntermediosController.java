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
    
    
    @GetMapping(value = "ej1")
    public Response<String> autenticacionArchivoTextoPlano(
            @RequestParam String username, @RequestParam String password){
        String resultado = ejerciciosIntermediosService
                .autenticacionArchivoTextoPlano(username, password);
        return new Response<>("Autenticación archivo texto plano.", resultado);
    }
    
    
    @GetMapping(value = "ej2")
    public Response<Estudiante> consultaPreparedStatement(@RequestParam String cedula){
        Estudiante estudiante = ejerciciosIntermediosService
                .consultaPreparedStatement(cedula);
        String mensaje = "Conexión BD Ok!";
        if(estudiante == null){mensaje = "Credenciales incorrectas!";}
        return new Response<>(mensaje, estudiante);
    }
}
