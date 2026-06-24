public class Animal {
    public void speak() { System.out.println("..."); }
}

public class Dog extends Animal {   // 'extends' = Python's class Dog(Animal)
    @Override
    public void speak() { System.out.println("Woof!"); }
}