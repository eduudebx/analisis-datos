package aseguras.pc1.controller;


import aseguras.pc1.jwt.AuthResponse;
import aseguras.pc1.jwt.LoginRegisterRequest;
import aseguras.pc1.service.EjercicioAvanzadoService;
import org.springframework.http.ResponseEntity;
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
    public ResponseEntity<AuthResponse> login(@RequestBody LoginRegisterRequest request){
        return ResponseEntity.ok(authService.login(request));
    }
    

    @PostMapping(value = "register")
    public ResponseEntity<AuthResponse> register(@RequestBody LoginRegisterRequest request){
        return ResponseEntity.ok(authService.register(request));
    }
}
