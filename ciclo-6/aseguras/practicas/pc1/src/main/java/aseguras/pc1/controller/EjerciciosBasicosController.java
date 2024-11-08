package aseguras.pc1.controller;


import aseguras.pc1.util.Response;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/ejbasicos")
public class EjerciciosBasicosController {
    
    
    /**
    * Verifica si una cadena de texto contiene solo números. La verificación se realiza utilizando una expresión regular 
    * que compara la cadena con el patrón "\\d+", que coincide con una secuencia de dígitos.
    *
    * @param cadena La cadena de texto que se va a verificar si contiene solo números.
    * @return Un objeto `Response<Boolean>` que indica si la cadena contiene solo números (`true`) o no (`false`).
    */
    @GetMapping(value = "ej1")
    public Response<Boolean> esSoloNumeros(@RequestParam String cadena){
        boolean resultado = cadena.matches("\\d+");
        return new Response<>("|"+cadena+"| = solo números?", resultado);
    }
    
    
    /**
    * Verifica si una cadena de texto contiene solo letras minúsculas. La verificación se realiza utilizando una expresión 
    * regular que compara la  cadena con el patrón "[a-z]+", que coincide con una secuencia de caracteres que son solo 
    * letras minúsculas.
    *
    * @param cadena La cadena de texto que se va a verificar si contiene solo letras minúsculas.
    * @return Un objeto `Response<Boolean>` que indica si la cadena contiene solo letras minúsculas (`true`) o no (`false`).
    */
    @GetMapping(value = "ej2")
    public Response<Boolean> esSoloLetrasMinusculas(@RequestParam String cadena){
        boolean resultado = cadena.matches("[a-z]+");
        return new Response<>("|"+cadena+"| = solo letras minúsculas?", resultado);
    }
    
    
    /**
    * Verifica si una cadena de texto contiene solo letras mayúsculas. La verificación se realiza utilizando una expresión 
    * regular que compara la cadena con el patrón "[A-Z]+", que coincide con una secuencia de caracteres que son solo letras
    * mayúsculas.
    * 
    * @param cadena La cadena de texto que se va a verificar si contiene solo letras mayúsculas.
    * @return Un objeto `Response<Boolean>` que indica si la cadena contiene solo letras mayúsculas (`true`) o no (`false`).
    */
    @GetMapping(value = "ej3")
     public Response<Boolean> esSoloLetrasMayusculas(@RequestParam String cadena) {
        boolean resultado = cadena.matches("[A-Z]+");
        return new Response<>("|"+cadena+"| = solo letras mayúsculas?", resultado);
     }
    
    
     
    /**
    * Verifica si una cadena de texto contiene solo letras o solo números. La verificación se realiza utilizando dos 
    * expresiones regulares:
    * - `"[a-zA-Z]+"` para comprobar si la cadena contiene solo letras.
    * - `"\\d+"` para comprobar si la cadena contiene solo dígitos numéricos.
    * 
    * @param cadena La cadena de texto que se va a verificar si contiene solo letras o solo números.
    * @return Un objeto `Response<Boolean>` que indica si la cadena contiene solo letras o solo números (`true`), 
    *         o si contiene una combinación de caracteres no permitidos (`false`).
    */
    @GetMapping(value = "ej4")
    public Response<Boolean> esSoloLetrasONumeros(@RequestParam String cadena) {
        boolean resultado = cadena.matches("[a-zA-Z]+") || cadena.matches("\\d+");
        return new Response<>("|"+cadena+"| = solo letras o solo números?", resultado);
    }
    
     
    /**
    * Verifica si una cadena de texto contiene al menos una letra y al menos un número. La verificación se realiza 
    * utilizando dos expresiones regulares:
    * - `".*[a-zA-Z].*"` para comprobar que la cadena contiene al menos una letra.
    * - `".*\\d.*"` para comprobar que la cadena contiene al menos un dígito numérico.
    * 
    * @param cadena La cadena de texto que se va a verificar si contiene al menos una letra y al menos un número.
    * @return Un objeto `Response<Boolean>` que indica si la cadena contiene al menos una letra y un número (`true`), 
    *         o si no cumple con estas condiciones (`false`).
    */
    @GetMapping(value = "ej5")
    public Response<Boolean> tieneLetrasYNumeros(@RequestParam String cadena){
        boolean resultado = cadena.matches(".*[a-zA-Z].*") && cadena.matches(".*\\d.*");
        return new Response<>("|"+cadena+"| = Al menos un número y una letra?", resultado);
    }     
}
