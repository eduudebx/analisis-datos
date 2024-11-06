package aseguras.p1.service;

import aseguras.p1.security.JWTService;
import aseguras.p1.model.Rol;
import aseguras.p1.model.Usuario;
import aseguras.p1.repository.UsuarioRepository;
import aseguras.p1.security.AuthResponse;
import aseguras.p1.security.LoginRegisterRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.security.crypto.password.PasswordEncoder;

@Service
public class EjAvanzadosService {
   
    private final UsuarioRepository usuarioRepository;
    private final JWTService jwtService;
    private final PasswordEncoder passwordEncoder;

    
    public EjAvanzadosService(UsuarioRepository usuarioRepository, JWTService jwtService, PasswordEncoder passwordEncoder) {
        this.usuarioRepository = usuarioRepository;
        this.jwtService = jwtService;
        this.passwordEncoder = passwordEncoder;
    }
    
    
    
    public AuthResponse login(LoginRegisterRequest request){
        return null;
    }
    
    
    public AuthResponse registro(LoginRegisterRequest request){
        Usuario usuario = new Usuario(request.getNombreUsuario(), request.getContrasena(), Rol.USER);
        usuarioRepository.save(usuario);
        
        return new AuthResponse(jwtService.getToken(usuario));
    }
}
