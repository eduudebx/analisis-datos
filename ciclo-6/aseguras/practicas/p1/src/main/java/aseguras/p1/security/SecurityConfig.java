package aseguras.p1.security;

import org.springframework.beans.factory.annotation.Autowired;
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
    
    private final JWTAuthenticationFilter jwtAutenticationFilter;
    private final AuthenticationProvider authProvider;

    public SecurityConfig(JWTAuthenticationFilter jwtAutenticationFilter, AuthenticationProvider authProvider) {
        this.jwtAutenticationFilter = jwtAutenticationFilter;
        this.authProvider = authProvider;
    }
    
    
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception{
        return http.csrf(csrf -> csrf.disable()).
                authorizeHttpRequests(
                        authRequest -> authRequest.
                                requestMatchers("/avanzados/**").
                                permitAll().
                                anyRequest().
                                authenticated()
                ).
                sessionManagement(sessionManager -> sessionManager.sessionCreationPolicy(SessionCreationPolicy.STATELESS)). 
                authenticationProvider(authProvider).
                addFilterBefore(jwtAutenticationFilter, UsernamePasswordAuthenticationFilter.class).
                build();
    }
}
