public class Calculator {
    public Integer result=0;

    public void Addition(Integer x, Integer y)
    {
        result=x+y;
        System.debug('Sum = '+result);
    }
    public void Subtraction(Integer x, Integer y)
    {
        result=x-y;
        System.debug('Difference = '+result);
    }
    public void Multiplication(Integer x, Integer y)
    {
        result=x*y;
        System.debug('Product = '+result);
    }
    public void Division(Integer x, Integer y)
    {
        result=x/y;
        System.debug('Quotient = '+result);
    }
}


Calculator c=new Calculator();
c.Addition(20,10);
c.Subtraction(20,10);
c.Multiplication(20,10);
c.Division(20,10);
