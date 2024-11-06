package aseguras.p1.util;

public class Response<T> {
    
    private T respuesta;
    private String mensaje;

    public Response(T respuesta, String mensaje) {
        this.respuesta = respuesta;
        this.mensaje = mensaje;
    }

    public void setRespuesta(T respuesta) {
        this.respuesta = respuesta;
    }

    public void setMensaje(String mensaje) {
        this.mensaje = mensaje;
    }

    
    public T getRespuesta() {
        return respuesta;
    }

    public String getMensaje() {
        return mensaje;
    }
    
    
}
