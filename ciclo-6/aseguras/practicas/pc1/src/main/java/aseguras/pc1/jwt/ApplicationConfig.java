package aseguras.pc1.jwt;


import aseguras.pc1.repository.UsuarioRepository;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;


@Configuration
public class ApplicationConfig {
    
    
    private final UsuarioRepository userRepository;
    

    public ApplicationConfig(UsuarioRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    

    /**
    * Configura y devuelve un `AuthenticationManager` para la autenticación de usuarios.
    *
    * Este método crea un `AuthenticationManager` utilizando la configuración proporcionada
    * en el parámetro `AuthenticationConfiguration`, que se utiliza para gestionar el
    * proceso de autenticación en el sistema.
    *
    * @param config La configuración de autenticación que se utiliza para obtener el `AuthenticationManager`.
    * @return El `AuthenticationManager` configurado para gestionar la autenticación de usuarios.
    */
    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration config) throws Exception{
        return config.getAuthenticationManager();
    }

    
    /**
    * Crea y configura un `AuthenticationProvider` para la autenticación de usuarios.
    *
    * Este método configura un `DaoAuthenticationProvider`, que se encarga de autenticar a los usuarios
    * utilizando un `UserDetailsService` personalizado para cargar los detalles del usuario y un 
    * `PasswordEncoder` para verificar la contraseña de manera segura.
    *
    * @return Un `AuthenticationProvider` configurado que utiliza el `UserDetailsService` y el `PasswordEncoder` definidos.
    */
    @Bean
    public AuthenticationProvider authenticationProvider(){
        DaoAuthenticationProvider authenticationProvider= new DaoAuthenticationProvider();
        authenticationProvider.setUserDetailsService(userDetailService());
        authenticationProvider.setPasswordEncoder(passwordEncoder());
        return authenticationProvider;
    }

    
    /**
    * Crea un `PasswordEncoder` utilizando el algoritmo BCrypt.
    *
    * Este método configura un `BCryptPasswordEncoder` para ser utilizado en la codificación
    * y verificación de contraseñas de manera segura. BCrypt es un algoritmo de hash de contraseñas
    * que incorpora un factor de coste adaptable, lo que hace que sea resistente a ataques de fuerza bruta.
    *
    * @return Un `PasswordEncoder` basado en el algoritmo BCrypt, que se utilizará para codificar y verificar contraseñas.
    */
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    
    /**
    * Crea un `UserDetailsService` para cargar los detalles del usuario a partir de la base de datos.
    *
    * Este método configura un `UserDetailsService` que utiliza el repositorio de usuarios
    * para buscar un usuario por su nombre de usuario. Si el usuario no se encuentra en la base de datos,
    * se lanza una excepción `UsernameNotFoundException`.
    *
    * @return Un `UserDetailsService` que carga los detalles del usuario desde la base de datos utilizando
    *         el `userRepository`.
    */
    @Bean
    public UserDetailsService userDetailService() {
        return username -> userRepository.findByUsername(username)
        .orElseThrow(()-> new UsernameNotFoundException("User not fournd"));
    }
}
