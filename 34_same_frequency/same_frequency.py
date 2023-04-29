def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_dict = {num : str(num1).count(str(num)) for num in range(0,10) if str(num1).count(str(num)) > 0}
    num2_dict = {num : str(num2).count(str(num)) for num in range(0,10) if str(num2).count(str(num)) > 0}
    return num1_dict==num2_dict