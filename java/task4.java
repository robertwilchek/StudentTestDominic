import java.util.*;

public class task4 {
    // Embedded model class so no external file is needed
    static class Person {
        final String first;
        final String last;
        final int age;
        Person(String first, String last, int age) {
            this.first = first; this.last = last; this.age = age;
        }
        @Override public String toString() {
            return last + ", " + first + " (" + age + ")";
        }
    }

    public static void main(String[] args) {
        Person[] people = new Person[] {
            new Person("Ben", "Adams", 30),
            new Person("Ana", "Zhang", 22),
            new Person("Cara", "Lopez", 27),
            new Person("Ben", "Adams", 35)
        };

        
        Arrays.sort(people, Comparator
            .comparing((Person p) -> p.last)
            .thenComparing(Comparator.comparingInt((Person p) -> p.age).reversed())
            .thenComparing(p -> p.first));

        for (Person p : people) System.out.println(p);
    }
}
