package aseguras.pc1.model;


import java.util.Collection;
import java.util.List;

import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import jakarta.persistence.Basic;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.persistence.UniqueConstraint;


@Entity
@Table(uniqueConstraints = {@UniqueConstraint(columnNames = {"username"})})
public class Usuario implements UserDetails{
    
    
    @Id
    @GeneratedValue
    Integer id;
    
    @Basic
    @Column(nullable = false)          
    String username;
    
    @Column(nullable = false)
    String password;
    
    @Enumerated(EnumType.STRING) 
    Rol role;
    

    public Usuario(Integer id, String username, String password, Rol role) {
        this.id = id;
        this.username = username;
        this.password = password;
        this.role = role;
    }
    

    public Usuario(String username, String password, Rol role) {
        this.username = username;
        this.password = password;
        this.role = role;
    }

    
    public Usuario() {
    }
    

    public void setUsername(String username) {
        this.username = username;
    }
    

    public void setPassword(String password) {
        this.password = password;
    }
    

    public void setRole(Rol role) {
        this.role = role;
    }
    

    public Integer getId() {
        return id;
    }

    
    @Override
    public String getUsername() {
        return username;
    }

    
    @Override
    public String getPassword() {
        return password;
    }

    
    public Rol getRole() {
        return role;
    }
    

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
      return List.of(new SimpleGrantedAuthority((role.name())));
    }
    
    
    @Override
    public boolean isAccountNonExpired() {
       return true;
    }
    
    
    @Override
    public boolean isAccountNonLocked() {
       return true;
    }
    
    
    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }
    
    
    @Override
    public boolean isEnabled() {
        return true;
    }
}
