package aseguras.pc1.jwt;


import java.io.IOException;

import org.springframework.http.HttpHeaders;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;
import org.springframework.util.StringUtils;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;


@Component
public class JwtAuthenticationFilter extends OncePerRequestFilter{
      
    
    private final JwtService jwtService;
    private final UserDetailsService userDetailsService;
    

    public JwtAuthenticationFilter(JwtService jwtService, UserDetailsService userDetailsService) {
        this.jwtService = jwtService;
        this.userDetailsService = userDetailsService;
    }
    
    
    /**
    * Filtro de seguridad que intercepta las peticiones HTTP para validar el token JWT y establecer la autenticación del usuario 
    * en el contexto de seguridad de Spring, si el token es válido.
    *
    * Este método es una implementación personalizada de un filtro en el que se extrae el token JWT del encabezado de la 
    * solicitud HTTP. Si el token es válido, se carga el usuario correspondiente, se verifica si el token es válido y si es 
    * así, se establece la autenticación del usuario en el contexto de seguridad de Spring para permitir el acceso a los recursos 
    * protegidos.
    *
    * @param request La solicitud HTTP entrante.
    * @param response La respuesta HTTP que se enviará al cliente.
    * @param filterChain La cadena de filtros que permite continuar el proceso de filtrado o el procesamiento de la solicitud.
    * @throws ServletException Si ocurre un error durante el procesamiento del filtro.
    * @throws IOException Si ocurre un error de entrada/salida al procesar la solicitud o respuesta.
    */
    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {
       
        final String token = getTokenFromRequest(request);
        final String username;

        if (token==null){
            filterChain.doFilter(request, response);
            return;
        }

        username=jwtService.getUsernameFromToken(token);

        if (username!=null && SecurityContextHolder.getContext().getAuthentication()==null){
            UserDetails userDetails=userDetailsService.loadUserByUsername(username);

            if (jwtService.isTokenValid(token, userDetails))
            {
                UsernamePasswordAuthenticationToken authToken= new UsernamePasswordAuthenticationToken(
                    userDetails,
                    null,
                    userDetails.getAuthorities());

                authToken.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));

                SecurityContextHolder.getContext().setAuthentication(authToken);
            }

        }
        
        filterChain.doFilter(request, response);
    }

    
    /**
    * Extrae el token JWT del encabezado de autorización de una solicitud HTTP.
    * 
    * Este método obtiene el encabezado de autorización de la solicitud HTTP, y si el encabezado contiene un token JWT 
    * (que comienza con el prefijo "Bearer "), extrae y devuelve dicho token. Si el encabezado no está presente o no 
    * contiene un token válido, devuelve `null`.
    *
    * @param request La solicitud HTTP desde la cual se extraerá el encabezado de autorización.
    * @return El token JWT extraído del encabezado de autorización, o `null` si no se encuentra un token válido.
    */
    private String getTokenFromRequest(HttpServletRequest request){
        final String authHeader=request.getHeader(HttpHeaders.AUTHORIZATION);

        if(StringUtils.hasText(authHeader) && authHeader.startsWith("Bearer "))
        {
            return authHeader.substring(7);
        }
        return null;
    }
}
