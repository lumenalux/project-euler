"""
The points P (x1, y1) and Q (x2, y2) are plotted at integer coordinates and are
joined to the origin, O(0,0), to form ΔOPQ.

          .                                                                   
         %@=                                                                  
        *%@#=                                                                 
          *                                                                   
          *                                     
          *                                       
          *                                 
          *                       P                                            
          *                                                                   
          *                      ==                                           
          *                     ====                                          
          *                    =+  -*                                         
          *                   ==    +=-                                       
          *                  ==      =+                                       
          *                  =.        +:                                     
          *                -+.          ==                                    
          *               -+.            ++                                   
          *               +*              ==                                  
          *              ++                ==                                 
          *             *=                  ++                                
          *            *-                    .+                               
          *           ++                       +=                             
          *          -*                         +: Q                 
          *         =*                       +=++                  
          *        ==                     -++=                 
          *       +=-                   +=+               
          *      :+-                =++.                                      
          *     .+-              =+=+                                         
          *     =+            -+=                                             
          *    =+         =+=*-                                               
          *   ==        ++=                                                   
          *  *-      =+=                                                      
          * ++   =++=                                                         
          *++  +++                                                            
          *+++.                                                      -%#%     
    +*****#***********************************************************@@%*    
       O  *                                                           *       
          *                                                                   
          =                                                                   

  
There are exactly fourteen triangles containing a right angle that can be formed
when each co-ordinate lies between 0 and 2 inclusive;
that is, 0 ≤ x1, y1, x2, y2 ≤ 2.

Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
"""
from math import gcd
from itertools import product


def solution(N: int) -> int:
    return 3 * N**2 + 2 * sum(min(gcd(x, y) * x // y, gcd(x, y) * (N-y) // x)
                              for x, y in product(range(1, N + 1), repeat=2))


# Test
if __name__ == "__main__":
    print(solution(50))  # 14234

