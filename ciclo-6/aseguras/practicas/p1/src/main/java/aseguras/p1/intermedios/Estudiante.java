package aseguras.p1.intermedios;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Setter
@Getter
@AllArgsConstructor
@NoArgsConstructor
public class Estudiante {
    
    private Long id;
    private String cedula;
    private String nombres;
    private String direccion;
    private String correo;
    private String telefono;
    private int edad;
}
