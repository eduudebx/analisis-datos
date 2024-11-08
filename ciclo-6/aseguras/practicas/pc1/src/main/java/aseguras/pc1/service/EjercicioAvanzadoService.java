package aseguras.pc1.service;

import aseguras.pc1.jwt.JwtService;
import aseguras.pc1.jwt.LoginRegisterRequest;
import aseguras.pc1.model.Rol;
import aseguras.pc1.model.Usuario;
import aseguras.pc1.repository.UsuarioRepository;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;


@Service
public class EjercicioAvanzadoService {
    
    
    private final UsuarioRepository userRepository;
    private final JwtService jwtService;
    private final PasswordEncoder passwordEncoder;
    private final AuthenticationManager authenticationManager;
    

    public EjercicioAvanzadoService(UsuarioRepository userRepository, JwtService jwtService, PasswordEncoder passwordEncoder, AuthenticationManager authenticationManager) {
        this.userRepository = userRepository;
        this.jwtService = jwtService;
        this.passwordEncoder = passwordEncoder;
        this.authenticationManager = authenticationManager;
    }
    
    
    public String login(LoginRegisterRequest request) {
        authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(
                request.getUsername(), request.getPassword()));
        UserDetails user = userRepository.findByUsername(request.getUsername()).orElseThrow();
        return jwtService.getToken(user);

    }

    public String register(LoginRegisterRequest request) {
        Usuario user = new Usuario(request.getUsername(), passwordEncoder.encode( request.getPassword()),Rol.USER);

        userRepository.save(user);

        return jwtService.getToken(user);
        
    }

}
