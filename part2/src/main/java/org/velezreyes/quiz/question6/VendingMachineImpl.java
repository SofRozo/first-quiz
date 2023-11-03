package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {
  /**Part 2 is a single question that must be implemented in Java. 
  The problem provides an interface for a VendingMachine. Your job is to create a class that implements
  the interface and behaves the way that the test suite in `Question6Test.java` expects. */

  private int balanceInCents;

  
  public static VendingMachine getInstance() {
    // Fix me!
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {
    balanceInCents += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
      if (name.equals("ScottCola")) {
          if (balanceInCents >= 75) {
              balanceInCents -= 75;
              return new DrinkImp("ScottCola", true); // Crear una instancia de DrinkImpl
          } else {
              throw new NotEnoughMoneyException();
          }
      } else if (name.equals("KarenTea")) {
          if (balanceInCents >= 100) {
              balanceInCents -= 100;
              return new DrinkImp("KarenTea", false); // Crear una instancia de DrinkImpl
          } else {
              throw new NotEnoughMoneyException();
          }
      } else {
          throw new UnknownDrinkException();
      }
  }
}