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


// GUI
// Create a new `Visualforce Page` for GUI code
// Click `preview` to view it
<apex:page controller="CalculatorController">
    <apex:form >
        <apex:pageBlock >
            <apex:pageBlockSection columns="1">
                <apex:inputText label="Input 1" value="{!input1}"/>
                <apex:inputText label="Input 2" value="{!input2}"/>
            </apex:pageBlockSection>
            <apex:pageBlockButtons >
                <apex:commandButton action="{!add}" value="+" />
                <apex:commandButton action="{!subtract}" value="-" />
                <apex:commandButton action="{!multiply}" value="*" />
                <apex:commandButton action="{!divide}" value="/" />
            </apex:pageBlockButtons>
            <apex:outputText value="{!result}" />
        </apex:pageBlock>
    </apex:form>
</apex:page>


// Logic
// Create a new `Apex Class`
public class CalculatorController {
    public Integer input1 { get; set; }
    public Integer input2 { get; set; }
    public Integer result { get; set; }
    
    public void add() {
        result = input1 + input2;
    }
    
    public void subtract() {
        result = input1 - input2;
    }
    
    public void multiply() {
        result = input1 * input2;
    }
    
    public void divide() {
        result = input1 / input2;
    }
}
