package aseguras.pc1.jwt;


public class LoginRegisterRequest {
    
    private String username;
    private String password;

    public LoginRegisterRequest(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public LoginRegisterRequest() {
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
