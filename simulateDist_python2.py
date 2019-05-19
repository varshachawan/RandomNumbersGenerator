##########################################################################
# Name: Varsha Rani Chawan
# UTA ID # 1001553524
# Homework # 5
##########################################################################
import random as rand
import math
import sys

def binomial(sample, N, prob):
    samples = []
    for i in range(sample):
        x = 0
        for n in range(N):
            if (rand.random() < prob):
                x += 1
        samples.append(x)
    return samples


def bernoulli(sample, prob):
    samples = []
    for i in range(sample):
        samples.append(int(rand.random() < prob))
    return samples


def geometric(sample, prob):
    samples = []
    for i in range(sample):
        x = 1
        while (rand.random() > prob):
            x += 1
        samples.append(x)
    return samples


def negative_binomial(sample, K, prob):
    samples = []
    for i in range(sample):
        for j in range(K):
            x = 1
            while (rand.random() > prob):
                x += 1
            x += x
        samples.append(x)
    return samples


def gamma(sample, alpha, lamda):
    samples = []
    for i in range(sample):
        x = 0
        for j in range(int(alpha)):
            u = rand.random()
            x += ((-1 / lamda) * (math.log(u)))
        samples.append(x)
    return samples

def factorial(n):
    factorial = 1
    if n < 0:
        print("Factorial does not exist for negative numbers")
    elif n == 0:
        factorial = 1
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
    return factorial

def poisson(sample, lamda):
    samples = []
    for i in range(sample):
        U = rand.random()
        i = 0
        F = math.exp(-lamda)
        while (U >= F):
            W = (math.pow(lamda, i) / factorial(i))
            F = F + ((math.exp(-lamda)) * W)
            i = i + 1
        x = i
        samples.append(x)
    return samples


def normal_dist(sample, mean, variance):
    samples = []
    if sample % 2 == 1:
        S = int((sample + 1)/ 2 )
    elif sample % 2 == 0:
        S = int(sample / 2)
    for i in range(S):
        U1 = rand.random()
        U2 = rand.random()
        Z1 = (math.sqrt(-2 * math.log(U1))) * (math.cos(2 * math.pi * U2))
        Z2 = (math.sqrt(-2 * math.log(U1))) * (math.sin(2 * math.pi * U2))
        N1 = mean + (variance * Z1)
        N2 = mean + (variance * Z2)
        samples.append(N1)
        samples.append(N2)
    return samples[0:sample]


def exponential(sample, lamda):
    samples = []
    for i in range(sample):
        x = ((-1 / lamda) * math.log(1 - (rand.random())))
        samples.append(x)
    return samples


def uniform(sample, a, b):
    samples = []
    for i in range(sample):
        x = a + ((b - a) * (rand.random()))
        samples.append(x)
    return samples


def arb_discrete(sample, args):
    samples = []
    lenOrig = len(args)
    totalcntOrig = len(args)-3

    for i in range(sample):
        totalcnt = totalcntOrig
        X = 0
        a = 0
        b = float(args[3])
        U = rand.random()
        while (a < U and U >= b):
            a = b
            b = b + float(args[-(totalcnt - 1)])
            totalcnt -= 1
            X += 1
        samples.append(X)
    return samples


class Error(Exception):
   """Base class for other exceptions"""
   pass

class IllegalValue(Error):
   """Raised when the P value is not in range [0-1]"""
   pass

class IncorrectProbabilities(Error):
   """Raised when the sum of P is not equal to 1"""
   pass

class NegativeValue(Error):
    """Raised when the argument value is negative"""

try:

    total_samples = int(sys.argv[1])
    distribution = sys.argv[2]
    argslen =len(sys.argv)

except Exception , exception:
    # Output unexpected Exceptions.
    print("==========================================================================================")
    print("Wrong Input arguments, pls follow below guide line for respective distribution calculation")
    print("==========================================================================================")
    print("python simulateDist.py <#ofSamples::int> bernoulli <P::float>")
    print("python simulateDist.py <#ofSamples::int> binomial <N::int> <P::float>")
    print("python simulateDist.py <#ofSamples::int> geometric <P::flot>")
    print("python simulateDist.py <#ofSamples::int> neg-binomial <K::int> <P::float>")
    print("python simulateDist.py <#ofSamples::int> poisson <lambda::float|int>")
    print("python simulateDist.py <#ofSamples::int> arb-discrete <p1, p2... pn::float>")
    print("python simulateDist.py <#ofSamples::int> uniform <a::float|int> <b::float|int>")
    print("python simulateDist.py <#ofSamples::int> exponential <lambda::float|int>")
    print("python simulateDist.py <#ofSamples::int> gamma <alpha::float|int> <lambda::float|int>")
    print("python simulateDist.py <#ofSamples::int> normal <mean::float|int> <sigma::float|int>")
    print("==========================================================================================\n")
    sys.exit(-1)


if distribution == "bernoulli":
    try:
        if argslen != 4 :
            raise IndexError
        if float(sys.argv[3]) > 1.0 or float(sys.argv[3]) < 0.0:
            raise IllegalValue
        print(bernoulli(total_samples, float(sys.argv[3])))
    except IndexError , error:
        # Output expected IndexErrors.
        print("Wrong number of  Input arguments For Bernoulli, please give in following format")
        print("python simulateDist.py <#ofSamples> bernoulli <P>")
    except TypeError , error:
        print("Wrong Input arguments Type For Binomial, please give in following type")
        print("python simulateDist.py <#ofSamples::int> bernoulli::string <P::float>")
    except ValueError , error:
        print("Wrong Input arguments Type For Binomial, please give in following type")
        print("python simulateDist.py <#ofSamples::int> bernoulli::string <P::float>")
    except IllegalValue:
        print("P value cannot be less than 0.0 or greater than 1.0 . Please provide proper P value.")
    except Exception , exception:
        print(exception, False)


elif distribution == "binomial":
    try:
        if argslen != 5:
            raise IndexError
        if float(sys.argv[4]) > 1.0 or float(sys.argv[4]) < 0.0:
            raise IllegalValue
        if int(sys.argv[3]) < 0:
            raise NegativeValue
        print(binomial(total_samples, int(sys.argv[3]), float(sys.argv[4])))
    except IndexError , error:
      # Output expected IndexErrors.
        print("Wrong number of Input arguments For Binomial, please give in following format")
        print("python simulateDist.py <#ofSamples> binomial <N> <P>")
    except TypeError , error:
      # Output expected IndexErrors.
        print("Wrong Input arguments Type For Binomial, please give in following type")
        print("python simulateDist.py <#ofSamples::int> binomial::string <N::int> <P::float>")
    except ValueError , error:
        print("Wrong Input arguments Type For Binomial, please give in following type")
        print("python simulateDist.py <#ofSamples::int> binomial::string <N::int> <P::float>")
    except IllegalValue:
        print("P value cannot be less than 0.0 or greater than 1.0 . Please provide proper P value.")
    except NegativeValue:
        print("N value must be greater than or equal to 0")
    except Exception , exception:
      # Output unexpected Exceptions.
        print(exception, False)


elif distribution == "geometric":
    try:
        if argslen != 4:
            raise IndexError
        if float(sys.argv[3]) > 1.0 or float(sys.argv[3]) < 0.0:
            raise IllegalValue
        print(geometric(total_samples, float(sys.argv[3])))
    except IndexError , error:
      # Output expected IndexErrors.
        print("Wrong number of Input arguments For geometric, pls give in following format")
        print("python simulateDist.py <#ofSamples> geometric <P>")
    except TypeError , error:
      # Output expected IndexErrors.
        print("Wrong Input arguments Type For geometric, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> geometric::string <P::float>")
    except ValueError , error:
        print("Wrong Input arguments Type For geometric, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> geometric::string <P::float>")
    except IllegalValue:
        print("P value cannot be less than 0.0 or greater than 1.0 . Please provide proper P value.")
    except Exception , exception:
      # Output unexpected Exceptions.
        print(exception, False)


elif distribution == "neg-binomial":
    try:
        if argslen != 5:
            raise IndexError
        if float(sys.argv[4]) > 1.0 or float(sys.argv[4]) < 0.0:
            raise IllegalValue
        if int(sys.argv[3]) <= 0 :
            raise NegativeValue
        print(negative_binomial(total_samples, int(sys.argv[3]), float(sys.argv[4])))
    except IndexError , error:
      # Output expected IndexErrors.
        print("Wrong number of Input arguments For neg-binomial, pls give in following format")
        print("python simulateDist.py <#ofSamples> neg-binomial <K> <P>")
    except TypeError , error:
      # Output expected IndexErrors.
        print("Wrong Input arguments Type For neg-binomial, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> neg-binomial::string <K::int> <P::float>")
    except ValueError , error:
        print("Wrong Input arguments Type For neg-binomial, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> neg-binomial::string <K::int> <P::float>")
    except IllegalValue:
        print("P value cannot be less than 0.0 or greater than 1.0 . Please provide proper P value.")
    except NegativeValue :
        print("K value must be greater than 0 ")
    except Exception , exception:
      # Output unexpected Exceptions.
        print(exception, False)


elif distribution == "poisson":
    try:
        if argslen != 4:
            raise IndexError
        if float(sys.argv[3]) < 0 :
            raise NegativeValue
        print(poisson(total_samples, float(sys.argv[3])))
    except IndexError , error:
      # Output expected IndexErrors.
        print("Wrong number of Input arguments For poisson, pls give in following format")
        print("python simulateDist.py <#ofSamples> poisson <lambda>")
    except TypeError , error:
      # Output expected IndexErrors.
        print("Wrong Input arguments Type For poisson, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> poisson::string <lambda::float/Int>")
    except ValueError , error:
        print("Wrong Input arguments Type For poisson, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> poisson::string <lambda::float/Int>")
    except NegativeValue:
        print("lambda value must be greater than or equal to 0")
    except Exception , exception:
      # Output unexpected Exceptions.
        print(exception, False)

elif distribution == "arb-discrete":
    try:
        if argslen < 4:
            raise IndexError
        summ = sum(float(i) for i in sys.argv[3:])
        if summ != 1.0:
            raise IncorrectProbabilities
        print(arb_discrete(total_samples, sys.argv))
    except IndexError , error:
        # Output expected IndexErrors.
        print("Wrong number of Input arguments For arb-discrete, pls give in following format")
        print("python simulateDist.py <#ofSamples> arb-discrete <p1, p2... pn>")
    except TypeError , error:
        # Output expected IndexErrors.
        print("Wrong Input arguments Type For arb-discrete, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> arb-discrete::string <p1, p2... pn ::float>")
    except ValueError , error:
        print("Wrong Input arguments Type For arb-discrete, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> arb-discrete::string <p1, p2... pn ::float>")
    except IncorrectProbabilities , error:
        print("The sum of the probabilities must be 1. Please provide proper P values")
    except Exception , exception:
        # Output unexpected Exceptions.
        print(exception, False)

elif distribution == "uniform":
    try:
        if argslen != 5:
            raise IndexError
        print(uniform(total_samples, float(sys.argv[3]), float(sys.argv[4])))
    except IndexError , error:
      # Output expected IndexErrors.
        print("Wrong number of Input arguments For uniform, pls give in following format")
        print("python simulateDist.py <#ofSamples> uniform <a> <b>")
    except TypeError , error:
      # Output expected IndexErrors.
        print("Wrong Input arguments Type For uniform, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> uniform::string <a::float/int> <b::float/int>")
    except ValueError , error:
        print("Wrong Input arguments Type For uniform, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> uniform::string <a::float/int> <b::float/int>")
    except Exception , exception:
      # Output unexpected Exceptions.
        print(exception, False)

elif distribution == "exponential":
    try:
        if argslen != 4:
            raise IndexError
        print(exponential(total_samples, float(sys.argv[3])))
    except IndexError , error:
      # Output expected IndexErrors.
        print("Wrong number of Input arguments For exponential, pls give in following format")
        print("python simulateDist.py <#ofSamples> exponential <lambda>")
    except TypeError , error:
      # Output expected IndexErrors.
        print("Wrong Input arguments Type For exponential, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> exponential::string <lambda::float/Int>")
    except ValueError , error:
        print("Wrong Input arguments Type For exponential, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> exponential::string <lambda::float/Int>")
    except Exception , exception:
      # Output unexpected Exceptions.
        print(exception, False)

elif distribution == "gamma":
    try:
        if argslen != 5:
            raise IndexError
        if float(sys.argv[3]) <= 0 or float(sys.argv[4]) <= 0 :
            raise NegativeValue
        print(gamma(total_samples, float(sys.argv[3]), float(sys.argv[4])))
    except IndexError , error:
        # Output expected IndexErrors.
        print("Wrong number of Input arguments For gamma, pls give in following format")
        print("python simulateDist.py <#ofSamples> gamma <alpha> <lambda>")
    except TypeError , error:
        # Output expected IndexErrors.
        print("Wrong Input arguments Type For gamma, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> gamma::string <alpha::float/int> <lambda::float/int>")
    except ValueError , error:
        print("Wrong Input arguments Type For gamma, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> gamma::string <alpha::float/int> <lambda::float/int>")
    except NegativeValue:
        print("alpha and lambda value must be greater than 0 ")
    except Exception , exception:
        # Output unexpected Exceptions.
        print(exception, False)

elif distribution == "normal":
    try:
        if argslen != 5:
            raise IndexError
        print(normal_dist(total_samples, float(sys.argv[3]),float(sys.argv[4])))
    except IndexError , error:
        # Output expected IndexErrors.
        print("Wrong number of Input arguments For normal, pls give in following format")
        print("python simulateDist.py <#ofSamples> normal <mean> <sigma>")
    except TypeError , error:
        # Output expected IndexErrors.
        print("Wrong Input arguments Type For normal, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> normal::string <mean::float/int> <sigma::float/int>")
    except ValueError , error:
        print("Wrong Input arguments Type For normal, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> normal::string <mean::float/int> <sigma::float/int>")
    except Exception , exception:
        # Output unexpected Exceptions.
        print(exception, False)

else:
    print("==========================================================================================")
    print("Wrong Input arguments, pls follow below guide line for respective distribution calculation")
    print("==========================================================================================")
    print("python simulateDist.py <#ofSamples::int> bernoulli <P::float>")
    print("python simulateDist.py <#ofSamples::int> binomial <N::int> <P::float>")
    print("python simulateDist.py <#ofSamples::int> geometric <P::float>")
    print("python simulateDist.py <#ofSamples::int> neg-binomial <K::int> <P::float>")
    print("python simulateDist.py <#ofSamples::int> poisson <lambda::float|int>")
    print("python simulateDist.py <#ofSamples::int> arb-discrete <p1, p2... pn::float>")
    print("python simulateDist.py <#ofSamples::int> uniform <a::float|int> <b::float|int>")
    print("python simulateDist.py <#ofSamples::int> exponential <lambda::float|int>")
    print("python simulateDist.py <#ofSamples::int> gamma <alpha::float|int> <lambda::float|int>")
    print("python simulateDist.py <#ofSamples::int> normal <mean::float|int> <sigma::float|int>")
    print("==========================================================================================\n")
    sys.exit(-1)

