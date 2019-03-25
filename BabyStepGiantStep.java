import java.math.*;
import java.util.*;


public class BabyStepGiantStep {

    public static void main (String[]args)
    {
        BigInteger p = new BigInteger("595117");
        BigInteger alpha = new BigInteger("1002");
        BigInteger alphaX = new BigInteger("437083");
        BigInteger n = new BigInteger("772");
        int N = 772;
        ArrayList<BigInteger> list1 = new ArrayList<>();

        for (int j = 0; j <= N; j++)
        {
            long u = j;
            BigInteger bigJ = BigInteger.valueOf(u);
            BigInteger element = alpha.modPow(bigJ,p).mod(p);
            list1.add(element);
        }

        BigInteger beta = alphaX.mod(p);

        for(int k = 0; k <= N; k++)
        {
            long u = k;
            BigInteger bigK = BigInteger.valueOf(u);
            BigInteger betaAlphaExponents = beta.multiply(alpha.modPow((n.multiply(bigK)).negate(),p)).mod(p);

            if (list1.contains(betaAlphaExponents))
            {
                int x = list1.indexOf(betaAlphaExponents) + (N*k);
                System.out.println("x = "+ x);

                //ran code once and converted bytes to letters offline
                if(x==141901){
                    System.out.println("NSA");
                }
            }
        }

    }
}