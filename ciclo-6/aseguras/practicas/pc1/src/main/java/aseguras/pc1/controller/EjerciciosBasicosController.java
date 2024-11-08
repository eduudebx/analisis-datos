package aseguras.pc1.controller;


import aseguras.pc1.util.Response;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/ejbasicos")
public class EjerciciosBasicosController {
    
    
    @GetMapping(value = "ej1")
    public Response<Boolean> esSoloNumeros(@RequestParam String cadena){
        boolean resultado = cadena.matches("\\d+");
        return new Response<>("|"+cadena+"| = solo números?", resultado);
    }
    
    
    @GetMapping(value = "ej2")
    public Response<Boolean> esSoloLetrasMinusculas(@RequestParam String cadena){
        boolean resultado = cadena.matches("[a-z]+");
        return new Response<>("|"+cadena+"| = solo letras minúsculas?", resultado);
    }
    
    
    @GetMapping(value = "ej3")
     public Response<Boolean> esSoloLetrasMayusculas(@RequestParam String cadena) {
        boolean resultado = cadena.matches("[A-Z]+");
        return new Response<>("|"+cadena+"| = solo letras mayúsculas?", resultado);
     }
    
    
    @GetMapping(value = "ej4")
    public Response<Boolean> esSoloLetrasONumeros(@RequestParam String cadena) {
        boolean resultado = cadena.matches("[a-zA-Z]+") || cadena.matches("\\d+");
        return new Response<>("|"+cadena+"| = solo letras o solo números?", resultado);
    }
    
    
    @GetMapping(value = "ej5")
    public Response<Boolean> tieneLetrasYNumeros(@RequestParam String cadena){
        boolean resultado = cadena.matches(".*[a-zA-Z].*") && cadena.matches(".*\\d.*");
        return new Response<>("|"+cadena+"| = solo letras minúsculas?", resultado);
    }     
}
