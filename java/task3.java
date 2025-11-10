/* There were no syntax issues that prevented the program from running.
 * But the program did assume that there would be at least one argument passed in
 * In the event that the program was run without arguments, it would crash
 * I've added a conditional check that checks if there is an argument before assigning it to the variable 'name'
 * If there is no argument, the name is left as a default 'John'
 */
public class task3 {
    
    public static void main(String[] args) {
        String name = "John"; 
        if(args.length > 0) {
            name = args[0]; 
        }
        System.out.println("Hello, " + name + "!");
    }
}