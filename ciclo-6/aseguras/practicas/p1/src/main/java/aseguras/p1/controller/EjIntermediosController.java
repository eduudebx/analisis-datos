package aseguras.p1.controller;

import aseguras.p1.service.EjIntermediosService;
import aseguras.p1.model.Estudiante;
import aseguras.p1.util.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/intermedios")
public class EjIntermediosController {
    
    @Autowired
    private EjIntermediosService intermediosService;
    
    
    @GetMapping("/ej1/{nombreUsuario}/{contrasena}")
    public String ej1AutenticarEnArchivoTextoPlano(
            @PathVariable String nombreUsuario, @PathVariable String contrasena){
        boolean acceso = intermediosService.autenticarEnArchivoTextoPlano(nombreUsuario, contrasena);
        return "Usuario: "+nombreUsuario+" | Acceso: "+acceso;
    }
    
    
    @GetMapping("/ej2/{cedula}")
    public Response<Estudiante> ej2ConsultaPreparedStatement(@PathVariable String cedula){
        Estudiante estudiante = intermediosService.buscarEstudiantePorCedula(cedula);
        String mensaje = "Ok.";
        
        if(estudiante == null){
            mensaje = "Recurso no encontrado.";
        }
        return new Response(estudiante, mensaje);
    }
}
