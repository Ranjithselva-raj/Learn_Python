#get a list and return list of factorial of each element in the list

def factorial_return_list(func):
    def wrapper(arg):
        """
        Wrapper function that takes an argument and performs certain operations based on the argument type. 
        If the argument is a list, it calculates the factorial of each element and returns the list of factorials. 
        If the argument is not a list, it prints 'Not a list'.
        
        Parameters:
        arg (any): The input argument to be processed.

        Returns:
        list or None: If the input is a list, returns a list of factorials of the elements. 
        If the input is not a list, returns None.
        """
        print('upside of wrapper')
        result = func(arg)
        #check the argument is list
        if isinstance(result, list):
            #stores the list after factorial
            
            total = []
            for i in result:
                def factorial(number):
                    if number == 0:
                        return 1
                    else:
                        return number * factorial(number - 1)
                #call and append the factorial
                total.append(factorial(i))
            return total
        else:
            print('Not a list')
            
    return wrapper




#get a list of numbers and return sum of factorial of each element in the list
def factorial_element_list(func):
    def wrapper(arg):
        """
        This function takes an argument and prints 'upside of wrapper'.
        It then calls func with the argument and checks if the result is a list.
        If it is a list, it calculates the factorial of each element and returns the total.
        If it's not a list, it prints 'Not a list'.
        """
        print('upside of wrapper')
        result = func(arg)

        if isinstance(result, list):
            total = 0
            for i in result:
                def factorial(number):
                    if number == 0:
                        return 1
                    else:
                        return number * factorial(number - 1)
                total += factorial(i)
            return total
        else:
            print('Not a list')
            
    return wrapper

#get a number and return the factorial of that number
def factorial_element(func):
    def wrapper(arg):
        """
        This function takes an argument and prints 'upside of wrapper', 
        then calls func with the argument and assigns the result to result. 
        It then defines a nested factorial function which calculates the 
        factorial of a number using recursion. After that, it prints 
        'downside of wrapper' and returns the factorial of the result.
        """
        print('upside of wrapper')
        result = func(arg)
        def factorial(number):
            if number == 0:
                return 1
            else:
                return number * factorial(number - 1)
        print('downside of wrapper')
        return factorial(result)
    return wrapper

@factorial_element
def get_factorial(element):
    return element