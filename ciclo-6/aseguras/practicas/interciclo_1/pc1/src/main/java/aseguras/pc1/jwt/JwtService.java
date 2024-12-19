package aseguras.pc1.jwt;


import java.security.Key;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;

import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;


@Service
public class JwtService {
    
    
    private static final String SECRET_KEY="586E3272357538782F413F4428472B4B6250655368566B597033733676397924";
    

    public String getToken(UserDetails user) {
        return getToken(new HashMap<>(), user);
    }
    

    /**
    * Genera un token JWT basado en los reclamos adicionales y los detalles del usuario proporcionados.
    *
    * Este método construye un token JWT utilizando la biblioteca JJWT, configurando los reclamos adicionales, el nombre de 
    * usuario como sujeto, la fecha de emisión, la fecha de expiración y una clave secreta para la firma. El token generado 
    * es válido por 24 horas desde su emisión.
    *
    * @param extraClaims Un mapa de reclamos adicionales que se incluirán en el token (por ejemplo, roles o atributos personalizados).
    * @param user Los detalles del usuario para el cual se genera el token, incluyendo su nombre de usuario.
    * @return El token JWT generado como una cadena de texto.
    */
    private String getToken(Map<String,Object> extraClaims, UserDetails user) {
        return Jwts
            .builder()
            .setClaims(extraClaims)
            .setSubject(user.getUsername())
            .setIssuedAt(new Date(System.currentTimeMillis()))
            .setExpiration(new Date(System.currentTimeMillis()+1000*60*24))
            .signWith(getKey(), SignatureAlgorithm.HS256)
            .compact();
    }
    
    
    /**
    * Obtiene la clave secreta utilizada para firmar y verificar tokens JWT.
    * 
    * Este método decodifica una cadena de texto base64 (almacenada en la constante `SECRET_KEY`) y la utiliza para generar 
    * una clave HMAC (Hash-based Message Authentication Code) que será empleada para firmar y verificar tokens JWT 
    * con el algoritmo HS256.
    *
    * @return La clave secreta HMAC generada a partir de la clave base64 decodificada.
    */
    private Key getKey() {
       byte[] keyBytes=Decoders.BASE64.decode(SECRET_KEY);
       return Keys.hmacShaKeyFor(keyBytes);
    }

    
    /**
    * Extrae el nombre de usuario (sujeto) desde un token JWT.
    * 
    * Este método decodifica el token JWT y extrae el nombre de usuario del sujeto (subject) del token, 
    * que generalmente corresponde al nombre de usuario del usuario autenticado. Utiliza el método `getClaim` 
    * para obtener el valor de este reclamo específico del token.
    *
    * @param token El token JWT del cual se extraerá el nombre de usuario.
    * @return El nombre de usuario extraído del token, o `null` si no se puede obtener.
    */
    public String getUsernameFromToken(String token) {
        return getClaim(token, Claims::getSubject);
    }
    

    /**
    * Verifica si un token JWT es válido en función del nombre de usuario y su fecha de expiración.
    * 
    * Este método valida un token JWT comprobando dos condiciones:
    * 1. Si el nombre de usuario extraído del token coincide con el nombre de usuario del objeto `UserDetails`.
    * 2. Si el token no ha expirado.
    * 
    * Si ambas condiciones son verdaderas, el token es considerado válido.
    *
    * @param token El token JWT que se va a validar.
    * @param userDetails El objeto `UserDetails` que contiene los detalles del usuario para comparar el nombre de usuario.
    * @return `true` si el token es válido, es decir, si el nombre de usuario coincide y el token no ha expirado; `false` en caso contrario.
    */
    public boolean isTokenValid(String token, UserDetails userDetails) {
        final String username=getUsernameFromToken(token);
        return (username.equals(userDetails.getUsername())&& !isTokenExpired(token));
    }
    

    /**
    * Extrae todos los reclamos del token JWT.
    * 
    * Este método decodifica el token JWT y extrae todos sus reclamos. Utiliza la clave de firma para validar el token 
    * y luego obtiene el cuerpo del JWT, que contiene los reclamos, como un objeto `Claims`. 
    * El método utiliza la biblioteca JJWT para analizar el token y verificar su integridad.
    *
    * @param token El token JWT del cual se extraerán los reclamos.
    * @return Un objeto `Claims` que contiene todos los reclamos del token JWT, como el nombre de usuario, la fecha de expiración, etc.
    * @throws JwtException Si el token no es válido o no puede ser decodificado correctamente.
    */
    private Claims getAllClaims(String token){
        return Jwts
            .parserBuilder()
            .setSigningKey(getKey())
            .build()
            .parseClaimsJws(token)
            .getBody();
    }

    
    /**
    * Extrae un reclamo específico del token JWT utilizando un resolver de reclamos.
    * 
    * Este método obtiene todos los reclamos del token JWT y luego aplica un `Function<Claims, T>` para extraer el 
    * valor de un reclamo específico del objeto `Claims`. El tipo de valor extraído depende del tipo de reclamo que 
    * se desea obtener (por ejemplo, el nombre de usuario, la fecha de expiración, etc.).
    *
    * @param <T> El tipo de valor que se espera del reclamo (por ejemplo, `String` para el nombre de usuario).
    * @param token El token JWT del cual se extraerán los reclamos.
    * @param claimsResolver Una función que toma un objeto `Claims` y devuelve el valor del reclamo deseado.
    * @return El valor del reclamo extraído del token JWT, según lo definido por el `claimsResolver`.
    */
    public <T> T getClaim(String token, Function<Claims,T> claimsResolver){
        final Claims claims=getAllClaims(token);
        return claimsResolver.apply(claims);
    }

    
    /**
    * Extrae la fecha de expiración de un token JWT.
    * 
    * Este método utiliza la función `getClaim` para obtener el reclamo de expiración del token JWT. 
    * El reclamo de expiración (exp) es una fecha que indica cuándo el token deja de ser válido.
    * 
    * @param token El token JWT del cual se extraerá la fecha de expiración.
    * @return La fecha de expiración del token JWT.
    */
    private Date getExpiration(String token){
        return getClaim(token, Claims::getExpiration);
    }

    
    /**
    * Verifica si un token JWT ha expirado.
    * 
    * Este método comprueba si la fecha de expiración del token JWT es anterior a la fecha y hora actuales. 
    * Si el token ha expirado, el método retorna `true`; de lo contrario, retorna `false`.
    * 
    * @param token El token JWT que se va a verificar.
    * @return `true` si el token ha expirado (su fecha de expiración es anterior al momento actual), 
    *         `false` si el token aún es válido.
    */
    private boolean isTokenExpired(String token){
        return getExpiration(token).before(new Date());
    }
}
