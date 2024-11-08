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
    
    
    /**
    * Realiza el proceso de autenticación de un usuario y genera un token JWT.
    *
    * Esta función autentica al usuario utilizando el nombre de usuario y la contraseña
    * proporcionados en el objeto `LoginRegisterRequest`. Si la autenticación es exitosa,
    * se recupera el detalle del usuario desde el repositorio y se genera un token JWT
    * para el usuario autenticado.
    *
    * @param request El objeto `LoginRegisterRequest` que contiene el nombre de usuario y la contraseña
    *                del usuario que intenta iniciar sesión.
    * @return Un token JWT generado para el usuario autenticado.
    */
    public String login(LoginRegisterRequest request) {
        authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(
                request.getUsername(), request.getPassword()));
        UserDetails user = userRepository.findByUsername(request.getUsername()).orElseThrow();
        return jwtService.getToken(user);

    }

    
    /**
    * Registra un nuevo usuario en el sistema y genera un token JWT.
    *
    * Esta función crea un nuevo objeto `Usuario` con el nombre de usuario y la contraseña
    * proporcionados en el objeto `LoginRegisterRequest`. La contraseña se codifica antes
    * de almacenarla en la base de datos. Después de guardar el usuario en el repositorio,
    * se genera un token JWT para el nuevo usuario registrado.
    *
    * @param request El objeto `LoginRegisterRequest` que contiene el nombre de usuario y la contraseña
    *                del usuario que se desea registrar.
    * @return Un token JWT generado para el usuario recién registrado.
    */
    public String register(LoginRegisterRequest request) {
        Usuario user = new Usuario(request.getUsername(), passwordEncoder.encode( request.getPassword()),Rol.USER);

        userRepository.save(user);

        return jwtService.getToken(user);
        
    }

}
