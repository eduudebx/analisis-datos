package aseguras.pc1.repository;


import aseguras.pc1.model.Usuario;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;


public interface UsuarioRepository extends JpaRepository<Usuario,Integer>{
    
    Optional<Usuario> findByUsername(String username);
}
