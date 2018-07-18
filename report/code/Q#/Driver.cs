using Microsoft.Quantum.Simulation.Core; // to use Q#
using Microsoft.Quantum.Simulation.Simulators; // to use Q#
using System; // to use several inbuilt classes
using System.Collections.Generic; // to allow the use of List


namespace Quantum.Shor{

    /**
     * Main class containing the factoring method and a small program using it.
     */
    class Shor {

        /**
         * Entry point of program
         */
        static void Main(string[] args){

            System.Console.WriteLine("Please enter an integer you would like to factor:");
            int toBeFactored = Int32.Parse(System.Console.ReadLine());

            try {
                int factorVal = Factor(toBeFactored);
                System.Console.WriteLine(String.Format
                    ("A factor of {0:d} is {1:d}.", toBeFactored, factorVal));
            } catch (System.FormatException sfExp) {
                System.Console.WriteLine("The value you input was not a valid integer.");
            } catch (QuantumAlgFailedException qExc) {
                System.Console.WriteLine(String.Format
                    ("Algorithm failed, because {0}", qExc.Message));
            }

            System.Console.WriteLine("Press any key to continue...");
            System.Console.ReadKey();
        }

        /**
        * Computes a factor of a given integer using Shor's algorithm.
        * Throws a QuantumAlgFailedException in case the quantum algorithm fails.
        */
        static int Factor(int N) {

            // Check if N is even
            if (N % 2 == 0) {
                return 2;
            }

            // Find random integer a such that 2<a<N
            Random rnd = new Random();
            int a = rnd.Next(2, N);

            // Check if a and N are coprime
            int b = GCD(a, N);
            if (b != 1) {
                return b;
            }

            // Quantum algorithm to find approximate periodicity
            int y;
            using (var sim = new QuantumSimulator()) {
                var outcome = ApproximatePeriodicity.Run(sim, N, a).Result;
                y = (int)outcome;
            }

            // Determine order r of a modulo N from quantum outcome with continued fractions
            
            // M is smallest power of 2 larger than N^2
            double Nsquared = Math.Pow((double)N, 2.0);
            int M = (int)Math.Pow(2.0, Math.Ceiling(Math.Log(Nsquared) / Math.Log(2.0)));

            // Find the convergents of the continued fractions expansion of y/M
            List<(int, int)> convergents = FindConvergents(y, M);

            int r;
            double z = (double)y/ (double)M;
            double maxDiff = 1 / (double)(2 * N ^ 2);
            foreach ((int num, int denom) in convergents){
                double fraction = (double)num / (double)denom;
                if (Math.Abs(fraction-z)<=maxDiff && denom < N) {
                    r = denom;

                    // Check if r is even
                    if (r % 2 != 0) {
                        continue;
                    }

                    // Find the greatest common divisor between a^(r/2)-1 and N
                    int s = GCD((int)Math.Pow(a,(r / 2)) - 1, N);

                    if (s == 1 || s == N) {
                        continue;
                    }

                    return s;
                }
            }

            throw new QuantumAlgFailedException
                ("no suitable order r could be found: either r was odd or s was 1");
        }

        /**
         * Computes greatest common divisor between x and y, assuming x and y are not 0.
         * Uses the Euclidean algorithm.
         */
        static int GCD(int x, int y) {
            
            // Ensure x > y
            if (x < y) {
                int swap = y;
                y = x;
                x = swap;
            }

            // Apply the Euclidean algorithm.
            int remainder;
            while (y != 1) {
                remainder = x % y;
                if (remainder == 0)
                    return y;

                x = y;
                y = remainder;
            }

            return y;
        }

        /**
         * Computes the convergents of the continued fraction expansion of a given fraction.
         */
        static List<(int, int)> FindConvergents(int num, int denom) {

            List<int> denominators = new List<int>();
            int wholeNumber;
            int remainder;

            // Find the denominator values for the continued fraction
            while (denom % num != 0) {
                wholeNumber = denom / num;
                remainder = denom % num;

                denom = num;
                num = remainder;

                denominators.Add(wholeNumber);
            }
            denominators.Add(denom / num);

            // Find the actual convergents: use the method a+b/c = (a*c+b)/c sequentially
            List<(int, int)> convergents = new List<(int,int)>();
            convergents.Add((1, denominators[0]));
            int swap;
            for (int i = 1; i < denominators.Count; i++) {
                denom = denominators[i];
                num = 1;

                for (int j = i; j>0; j--) {
                    wholeNumber = denominators[j - 1];
                    num = num + wholeNumber * denom;

                    swap = num;
                    num = denom;
                    denom = swap;
                }

                convergents.Add(SimplifyFraction(num, denom));
            }

            return convergents;
        }

        /**
         * Simplifies a given fraction. 
         * E.g. when given (3,9) it will return (1,3)
         */
        static (int,int) SimplifyFraction(int num, int denom) {

            int commonFactor = GCD(num, denom);
            return (num / commonFactor, denom / commonFactor);
        }


    }    
    
    /**
     * An Exception to handle failures in the algorithm.
     */
    public class QuantumAlgFailedException : Exception {

        public QuantumAlgFailedException(string message) : base(message) {
        }
    }
    
}