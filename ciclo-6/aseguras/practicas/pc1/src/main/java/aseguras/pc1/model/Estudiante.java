package aseguras.pc1.model;

import jakarta.persistence.Basic;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.persistence.UniqueConstraint;


@Entity
@Table(uniqueConstraints = {@UniqueConstraint(columnNames = {"cedula"})})
public class Estudiante {
    
    @Id
    @GeneratedValue
    private Integer id;
    
    @Basic
    @Column(nullable = false)
    private String cedula;
    
    private String direccion;
    private String nombres;
    private int edad;

    public Estudiante(Integer id, String cedula, String direccion, String nombres, int edad) {
        this.id = id;
        this.cedula = cedula;
        this.direccion = direccion;
        this.nombres = nombres;
        this.edad = edad;
    }

    
    public Estudiante(String cedula, String direccion, String nombres, int edad) {
        this.cedula = cedula;
        this.direccion = direccion;
        this.nombres = nombres;
        this.edad = edad;
    }

    
    public Estudiante() {
    }

    public void setId(Integer id) {
        this.id = id;
    }
   

    public void setCedula(String cedula) {
        this.cedula = cedula;
    }
    

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    

    public void setNombres(String nombres) {
        this.nombres = nombres;
    }
    

    public void setEdad(int edad) {
        this.edad = edad;
    }
    

    public Integer getId() {
        return id;
    }
    

    public String getCedula() {
        return cedula;
    }
    

    public String getDireccion() {
        return direccion;
    }

    
    public String getNombres() {
        return nombres;
    }

    
    public int getEdad() {
        return edad;
    }
}
