package aseguras.p1.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/basicos")
public class EjBasicosController {
    
    @GetMapping("/ej1/{cadena}")
    public String ej1SoloNumeros(@PathVariable String cadena){
         String patron = "^[0-9]+$";
         return "["+cadena+"] corresponde a un patrón de solo números?: "+(cadena.matches(patron));
    }
    
    
    @GetMapping("/ej2/{cadena}")
    public String ej2SoloMinusculas(@PathVariable String cadena){
        String patron = "^[a-z]+$";
        return "["+cadena+"] corresponde a un patrón de solo letras minúsculas?: "+(cadena.matches(patron));
    }
    
    
    @GetMapping("/ej3/{cadena}")
    public String ej3SoloMayusculas(@PathVariable String cadena){
        String patron = "^[A-Z]+$";
        return "["+cadena+"] corresponde a un patrón de solo letras mayúsculas?: "+(cadena.matches(patron));
    }
    
    
    @GetMapping("/ej4/{cadena}")
    public String ej4LetrasONumeros(@PathVariable String cadena){
        String patron = "^[a-zA-Z]+$";
        String patron2 = "^[0-9]+$";
        return "["+cadena+"] corresponde a un patrón de solo números o solo letras?: "+(cadena.matches(patron) || cadena.matches(patron2));
    }
    
    
    @GetMapping("/ej5/{cadena}")
    public String ej5LetrasYNumeros(@PathVariable String cadena){
        String patron = "^(?=.*[a-zA-Z])(?=.*[0-9]).+$";
        return "["+cadena+"] corresponde a un patrón que contiene por lo menos un número y una letra?: "+(cadena.matches(patron));
    }
}
