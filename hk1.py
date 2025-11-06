import java.security.*;
import java.util.*;

public class CreatingDigitalSignatures {
    public static void main(String[] args) throws Exception {
        String msg = new Scanner(System.in).nextLine();
        KeyPair pair = KeyPairGenerator.getInstance("DSA").generateKeyPair();
        Signature sign = Signature.getInstance("SHA256withDSA");
        sign.initSign(pair.getPrivate());
        sign.update(msg.getBytes());
        System.out.println(new String(sign.sign()));
    }
}