package aseguras.pc1.controller;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/ejbasicos")
public class EjerciciosBasicosController {
    
    
    @GetMapping(value = "ej1")
    public String welcome()
    {
        return "Welcome from secure endpoint";
    }
}
