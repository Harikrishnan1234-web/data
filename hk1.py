3
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



1

import javax.crypto.*;
import java.util.Base64;

public class Main {
    public static void main(String[] args) throws Exception {
        SecretKey key = KeyGenerator.getInstance("AES").generateKey();
        Cipher cipher = Cipher.getInstance("AES");

        String msg = "Hello, world!";
        cipher.init(Cipher.ENCRYPT_MODE, key);
        String enc = Base64.getEncoder().encodeToString(cipher.doFinal(msg.getBytes()));

        cipher.init(Cipher.DECRYPT_MODE, key);
        String dec = new String(cipher.doFinal(Base64.getDecoder().decode(enc)));

        System.out.println("Original: " + msg);
        System.out.println("Encrypted: " + enc);
        System.out.println("Decrypted: " + dec);
    }





10

import os
def start_vpn():
 # Replace 'client.ovpn' with the actual path to your OpenVPN client configuration file
 print("Starting VPN connection...")
 os.system("sudo openvpn --config /path/to/client.ovpn")
if __name__ == "__main__":
 start_vpn()import os
def start_vpn():
 # Replace 'client.ovpn' with the actual path to your OpenVPN client configuration file
 print("Starting VPN connection...")
 os.system("sudo openvpn --config /path/to/client.ovpn")
if __name__ == "__main__":
 start_vpn()