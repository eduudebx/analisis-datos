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
    
    
    @PostMapping(value = "login")
    public Response<String> login(@RequestBody LoginRegisterRequest request){
        return new Response<>("JWT Token", authService.login(request));
    }
    

    @PostMapping(value = "register")
    public Response<String> register(@RequestBody LoginRegisterRequest request){
        return new Response<>("JWT Token", authService.register(request));
    }
}
