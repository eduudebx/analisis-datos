package aseguras.p1.security;

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;

@Service
public class JWTService {
    
   private static final String CLAVE = "ClaveSuperSecreta";
    
   
   public String getToken(UserDetails usuario){
       Map<String, Object> extraClaims = new HashMap<>();
       return Jwts. 
              builder(). 
              setClaims(extraClaims). 
              setSubject(usuario.getUsername()). 
              setIssuedAt(new Date(System.currentTimeMillis())). 
              setExpiration(new Date(System.currentTimeMillis() + 1000 * 60 * 24)). 
              signWith(Keys.hmacShaKeyFor(Decoders.BASE64.decode(CLAVE)), SignatureAlgorithm.HS256). 
              compact();
   }
}
