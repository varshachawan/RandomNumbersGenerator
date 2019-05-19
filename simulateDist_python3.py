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
        for j in range(alpha):
            u = rand.random()
            x += ((-1 / lamda) * (math.log(u)))
        samples.append(x)
    return samples


def poisson(sample, lamda):
    samples = []
    for i in range(sample):
        U = rand.random()
        i = 0
        F = math.exp(-lamda)
        while (U >= F):
            F = F + ((math.exp(-lamda)) * (math.pow(lamda, i) / math.gamma(i + 1)))
            i = i + 1
        x = i
        samples.append(x)
    return samples


def normal_dist(sample, mean, variance):
    samplesN1 = []
    samplesN2 = []
    for i in range(sample):
        U1 = rand.random()
        U2 = rand.random()
        Z1 = (math.sqrt(-2 * math.log(U1))) * (math.cos(2 * math.pi * U2))
        Z2 = (math.sqrt(-2 * math.log(U1))) * (math.sin(2 * math.pi * U2))
        N1 = mean + (variance * Z1)
        N2 = mean + (variance * Z2)
        samplesN1.append(N1)
        samplesN2.append(N2)
    return samplesN1, samplesN2


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
   """Raised when the input value is too small"""
   pass

class IncorrectProbabilities(Error):
   """Raised when the input value is too large"""
   pass

try:

    total_samples = int(sys.argv[1])
    distribution = sys.argv[2]
    argslen =len(sys.argv)

except Exception as exception:
    # Output unexpected Exceptions.
    print("==========================================================================================")
    print("Wrong Input arguments, pls follow below guide line for respective distribution calculation")
    print("==========================================================================================")
    print("python simulateDist.py <#ofSamples> bernouli <N> <P>")
    print("python simulateDist.py <#ofSamples> bernouli <N> <P>")
    print("python simulateDist.py <#ofSamples> bernouli <N> <P>")
    print("python simulateDist.py <#ofSamples> bernouli <N> <P>")
    print("python simulateDist.py <#ofSamplestotal_samples = int(sys.argv[1])")
    print("python simulateDist.py <#ofSamples> bernouli <N> <P>")
    print("python simulateDist.py <#ofSamples> bernouli <N> <P>")
    print("python simulateDist.py <#ofSamples> bernouli <N> <P>")
    print("python simulateDist.py <#ofSamples> bernouli <N> <P>")
    print("python simulateDist.py <#ofSamples> bernouli <N> <P>")
    print("python simulateDist.py <#ofSamples> bernouli <N> <P>")
    print("==========================================================================================\n")
    exit(-1)


if distribution == "bernoulli":
    try:
        if argslen != 4 :
            raise IndexError
        if float(sys.argv[3]) > 1.0 or float(sys.argv[3]) < 0.0:
            raise IllegalValue
        print(bernoulli(total_samples, float(sys.argv[3])))

    except IndexError as error:
        # Output expected IndexErrors.
        print("Wrong number of  Input arguments For Bernoulli, pls give in following format")
        print("python simulateDist.py <#ofSamples> bernoulli <P>")
    except TypeError as error:
        print("Wrong Input arguments Type For Binomial, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> bernoulli::string <P::float>")
    except ValueError as error:
        print("Wrong Input arguments Type For Binomial, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> bernoulli::string <P::float>")
    except IllegalValue:
        print("P value cannot be less than 0.0 or greater than 1.0 . Please provide proper P value.")
    except Exception as exception:
        print(exception, False)


if distribution == "binomial":
    try:
        if argslen != 5:
            raise IndexError
        if float(sys.argv[4]) > 1.0 or float(sys.argv[4]) < 0.0:
            raise IllegalValue
        print(binomial(total_samples, int(sys.argv[3]), float(sys.argv[4])))
    except IndexError as error:
      # Output expected IndexErrors.
        print("Wrong number of Input arguments For Binomial, pls give in following format")
        print("python simulateDist.py <#ofSamples> binomial <N> <P>")
    except TypeError as error:
      # Output expected IndexErrors.
        print("Wrong Input arguments Type For Binomial, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> binomial::string <N::int> <P::float>")
    except ValueError as error:
        print("Wrong Input arguments Type For Binomial, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> binomial::string <N::int> <P::float>")
    except IllegalValue:
        print("P value cannot be less than 0.0 or greater than 1.0 . Please provide proper P value.")
    except Exception as exception:
      # Output unexpected Exceptions.
        print(exception, False)


if distribution == "geometric":
    try:
        if argslen != 4:
            raise IndexError
        if float(sys.argv[3]) > 1.0 or float(sys.argv[3]) < 0.0:
            raise IllegalValue
        print(geometric(total_samples, float(sys.argv[3])))
    except IndexError as error:
      # Output expected IndexErrors.
        print("Wrong number of Input arguments For geometric, pls give in following format")
        print("python simulateDist.py <#ofSamples> geometric <P>")
    except TypeError as error:
      # Output expected IndexErrors.
        print("Wrong Input arguments Type For geometric, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> geometric::string <P::float>")
    except ValueError as error:
        print("Wrong Input arguments Type For geometric, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> geometric::string <P::float>")
    except IllegalValue:
        print("P value cannot be less than 0.0 or greater than 1.0 . Please provide proper P value.")
    except Exception as exception:
      # Output unexpected Exceptions.
        print(exception, False)


if distribution == "neg-binomial":
    try:
        if argslen != 5:
            raise IndexError
        if float(sys.argv[4]) > 1.0 or float(sys.argv[4]) < 0.0:
            raise IllegalValue
        print(negative_binomial(total_samples, int(sys.argv[3]), float(sys.argv[4])))
    except IndexError as error:
      # Output expected IndexErrors.
        print("Wrong number of Input arguments For neg-binomial, pls give in following format")
        print("python simulateDist.py <#ofSamples> neg-binomial <K> <P>")
    except TypeError as error:
      # Output expected IndexErrors.
        print("Wrong Input arguments Type For neg-binomial, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> neg-binomial::string <K::int> <P::float>")
    except ValueError as error:
        print("Wrong Input arguments Type For neg-binomial, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> neg-binomial::string <K::int> <P::float>")
    except IllegalValue:
        print("P value cannot be less than 0.0 or greater than 1.0 . Please provide proper P value.")
    except Exception as exception:
      # Output unexpected Exceptions.
        print(exception, False)


if distribution == "poisson":
    try:
        if argslen != 4:
            raise IndexError
        print(poisson(total_samples, float(sys.argv[3])))
    except IndexError as error:
      # Output expected IndexErrors.
        print("Wrong number of Input arguments For poisson, pls give in following format")
        print("python simulateDist.py <#ofSamples> poisson <λ>")
    except TypeError as error:
      # Output expected IndexErrors.
        print("Wrong Input arguments Type For poisson, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> poisson::string <λ::float/Int>")
    except ValueError as error:
        print("Wrong Input arguments Type For poisson, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> poisson::string <λ::float/Int>")
    except Exception as exception:
      # Output unexpected Exceptions.
        print(exception, False)

if distribution == "arb-discrete":
  print(arb_discrete(total_samples, sys.argv))

if distribution == "uniform":
    try:
        if argslen != 5:
            raise IndexError
        print(uniform(total_samples, int(sys.argv[3]), int(sys.argv[4])))
    except IndexError as error:
      # Output expected IndexErrors.
        print("Wrong number of Input arguments For uniform, pls give in following format")
        print("python simulateDist.py <#ofSamples> uniform <a> <b>")
    except TypeError as error:
      # Output expected IndexErrors.
        print("Wrong Input arguments Type For uniform, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> uniform::string <a::float/int> <b::float/int>")
    except ValueError as error:
        print("Wrong Input arguments Type For uniform, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> uniform::string <a::float/int> <b::float/int>")
    except Exception as exception:
      # Output unexpected Exceptions.
        print(exception, False)

if distribution == "exponential":
    try:
        if argslen != 4:
            raise IndexError
        print(exponential(total_samples, float(sys.argv[3])))
    except IndexError as error:
      # Output expected IndexErrors.
        print("Wrong number of Input arguments For exponential, pls give in following format")
        print("python simulateDist.py <#ofSamples> exponential <λ>")
    except TypeError as error:
      # Output expected IndexErrors.
        print("Wrong Input arguments Type For exponential, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> exponential::string <λ::float/Int>")
    except ValueError as error:
        print("Wrong Input arguments Type For exponential, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> exponential::string <λ::float/Int>")
    except Exception as exception:
      # Output unexpected Exceptions.
        print(exception, False)

if distribution == "gamma":
    try:
        if argslen != 5:
            raise IndexError
        print(gamma(total_samples, int(sys.argv[3]), float(sys.argv[4])))
    except IndexError as error:
        # Output expected IndexErrors.
        print("Wrong number of Input arguments For gamma, pls give in following format")
        print("python simulateDist.py <#ofSamples> gamma <α> <λ>")
    except TypeError as error:
        # Output expected IndexErrors.
        print("Wrong Input arguments Type For gamma, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> gamma::string <α::int> <λ::float/int>")
    except ValueError as error:
        print("Wrong Input arguments Type For gamma, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> gamma::string <α::int> <λ::float/int>")
    except Exception as exception:
        # Output unexpected Exceptions.
        print(exception, False)

if distribution == "normal":
    try:
        if argslen != 5:
            raise IndexError
        print(normal_dist(total_samples, float(sys.argv[3]),float(sys.argv[4])))
    except IndexError as error:
        # Output expected IndexErrors.
        print("Wrong number of Input arguments For normal, pls give in following format")
        print("python simulateDist.py <#ofSamples> normal <μ> <σ>")
    except TypeError as error:
        # Output expected IndexErrors.
        print("Wrong Input arguments Type For normal, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> normal::string <μ::float/int> <σ::float/int>")
    except ValueError as error:
        print("Wrong Input arguments Type For normal, pls give in following type")
        print("python simulateDist.py <#ofSamples::int> normal::string <μ::float/int> <σ::float/int>")
    except Exception as exception:
        # Output unexpected Exceptions.
        print(exception, False)




