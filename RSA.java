import java.math.*;
import java.util.*;


public class RSA {

    public static void main(String[] args)
    {
        HashMap<BigInteger, Integer> map = new HashMap<>();
        BigInteger n = new BigInteger("665491722871");
        BigInteger e = new BigInteger("710221");
        BigInteger c = new BigInteger("121259080226");

        for (int x = 1; x <= 3000000; x++)
        {
            try
            {
            BigInteger xMod = BigInteger.valueOf(x).modPow(e.negate(),n);
            BigInteger CxMod = (c.multiply(xMod)).mod(n);
            map.put(CxMod, x);
            }
            catch (ArithmeticException e1){
                System.out.println("cant do that");}
        }


        for (int index = 1; index <= 3000000; index++)
        {
            BigInteger y = BigInteger.valueOf(index).modPow(e,n);
            if (map.containsKey(y))
            {
                System.out.println("\nmatch found");
                BigInteger message = BigInteger.valueOf(index).multiply(BigInteger.valueOf(map.get(y)));
                System.out.println(message);

                String messageString = String.valueOf(message);
                String[] messageArray =messageString.split("(?<=\\G.{2})");
    
                String readableMessage = "";

                //hacky way to make this readable but it works.  I think the second letter should represent a P?
                if(messageArray[0].equals("19")){readableMessage+= "S";}
                if(messageArray[1].equals("17")){readableMessage+= "Q";}
                if(messageArray[2].equals("18")){readableMessage+= "R";}
                if(messageArray[3].equals("09")){readableMessage+= "I";}
                if(messageArray[4].equals("14")){readableMessage+= "N";}
                if(messageArray[5].equals("07")){readableMessage+= "G";}

                System.out.println("\nm = " +readableMessage);

                break;
            }


        }
        System.out.println("\nI think the answer should be SPRING but I can't reproduce a P for the second character");
    }
}
