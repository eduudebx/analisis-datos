package aseguras.p1.basicos;


public class EjBasicosController {
    
    public boolean ej1SoloNumeros(String cadena){
         String patron = "^[0-9]+$";
         return cadena.matches(patron);
    }
    
    
    public boolean ej2SoloMinusculas(String cadena){
        String patron = "^[a-z]+$";
        return cadena.matches(patron);
    }
    
    
    public boolean ej3SoloMayusculas(String cadena){
        String patron = "^[A-Z]+$";
        return cadena.matches(patron);
    }
    
    
    public boolean ej4LetrasONumeros(String cadena){
        String patron = "^[a-zA-Z]+$";
        String patron2 = "^[0-9]+$";
        return cadena.matches(patron) || cadena.matches(patron2);
    }
    
    
    public boolean ej5LetrasYNumeros(String cadena){
        String patron = "^(?=.*[a-zA-Z])(?=.*[0-9]).+$";
        return cadena.matches(patron);
    }
}
