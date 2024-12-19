package aseguras.pc1.jwt;


import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;


@Configuration
@EnableWebSecurity
public class SecurityConfig {
    
    private final JwtAuthenticationFilter jwtAuthenticationFilter;
    private final AuthenticationProvider authProvider;
    

    public SecurityConfig(JwtAuthenticationFilter jwtAuthenticationFilter, AuthenticationProvider authProvider) {
        this.jwtAuthenticationFilter = jwtAuthenticationFilter;
        this.authProvider = authProvider;
    }
    
    
    /**
    * Configura la cadena de filtros de seguridad para la aplicación.
    * 
    * Este método configura el filtro de seguridad de la aplicación utilizando `HttpSecurity` para definir las políticas 
    * de seguridad, como la protección CSRF, las reglas de autorización, la gestión de sesiones y el proveedor de autenticación.
    * También agrega un filtro personalizado para la autenticación basada en JWT antes del filtro de autenticación estándar de Spring.
    * 
    * La configuración realiza las siguientes acciones:
    * 1. Deshabilita la protección CSRF (Cross-Site Request Forgery).
    * 2. Permite el acceso público a las rutas que coinciden con "/ejavanzado/**".
    * 3. Requiere autenticación para cualquier otra solicitud.
    * 4. Configura la gestión de sesiones para que no se utilicen sesiones de estado (sin estado).
    * 5. Establece un proveedor de autenticación personalizado.
    * 6. Añade un filtro de autenticación JWT antes del filtro de autenticación estándar de Spring (`UsernamePasswordAuthenticationFilter`).
    * 
    * @param http La configuración de seguridad HTTP de la aplicación.
    * @return El objeto `SecurityFilterChain` que define la cadena de filtros de seguridad.
    * @throws Exception Si ocurre un error durante la configuración de seguridad.
    */
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception{
        return http
            .csrf(csrf -> 
                csrf
                .disable())
            .authorizeHttpRequests(authRequest ->
              authRequest
                .requestMatchers("/ejavanzado/**").permitAll()
                .anyRequest().authenticated()
                )
            .sessionManagement(sessionManager->
                sessionManager 
                  .sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .authenticationProvider(authProvider)
            .addFilterBefore(jwtAuthenticationFilter, UsernamePasswordAuthenticationFilter.class)
            .build();     
    }
}
