package aseguras.p1.controller;

import aseguras.p1.security.AuthResponse;
import aseguras.p1.security.LoginRegisterRequest;
import aseguras.p1.service.EjAvanzadosService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/avanzados")
public class EjAvanzadosController {
    
    @Autowired
    private EjAvanzadosService ejAvanzadosService;
    
    
    @PostMapping("/login")
    public ResponseEntity<AuthResponse> login(@RequestBody LoginRegisterRequest request){
        return ResponseEntity.ok(ejAvanzadosService.login(request));
    }
    
    
    @PostMapping("/registro")
    public ResponseEntity<AuthResponse> registro(@RequestBody LoginRegisterRequest request){
        return ResponseEntity.ok(ejAvanzadosService.registro(request));
    }
}
