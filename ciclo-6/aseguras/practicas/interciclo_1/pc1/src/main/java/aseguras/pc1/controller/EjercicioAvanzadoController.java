package aseguras.pc1.controller;

import aseguras.pc1.jwt.LoginRegisterRequest;
import aseguras.pc1.service.EjercicioAvanzadoService;
import aseguras.pc1.util.Response;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/ejavanzado")
public class EjercicioAvanzadoController {
    
    
    private final EjercicioAvanzadoService authService;
    

    public EjercicioAvanzadoController(EjercicioAvanzadoService authService) {
        this.authService = authService;
    }
    
    
    /**
    * Maneja la solicitud de inicio de sesión y devuelve un token JWT.
    *
    * @param request Un objeto `LoginRegisterRequest` que contiene las credenciales de inicio de sesión del usuario (nombre de usuario y contraseña).
    * @return Un objeto `Response<String>` que contiene el token JWT como mensaje si el inicio de sesión es exitoso.
    */
    @PostMapping(value = "login")
    public Response<String> login(@RequestBody LoginRegisterRequest request){
        return new Response<>("JWT Token", authService.login(request));
    }
    

    /**
    * Maneja la solicitud de registro de un nuevo usuario y devuelve un token JWT.
    *
    * @param request Un objeto `LoginRegisterRequest` que contiene la información de registro del nuevo usuario (nombre de usuario y contraseña).
    * @return Un objeto `Response<String>` que contiene el token JWT generado para el nuevo usuario.
    */
    @PostMapping(value = "register")
    public Response<String> register(@RequestBody LoginRegisterRequest request){
        return new Response<>("JWT Token", authService.register(request));
    }
}
