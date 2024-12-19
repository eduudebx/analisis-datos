package aseguras.pc1.util;


public class Response<T> {
    
    
    private String message;
    private T data;
    

    public Response() {
        this.message = "";
        this.data = null;
    }
    

    public Response(String message, T data) {
        this.message = message;
        this.data = data;
    }
    

    public String getMessage() {
        return message;
    }
    

    public void setMessage(String message) {
        this.message = message;
    }
    

    public T getData() {
        return data;
    }
    

    public void setData(T data) {
        this.data = data;
    }
    

    @Override
    public String toString() {
        return "Message: " + message + ", Data: " + data;
    }
}

