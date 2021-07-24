package src;
import java.util.*;
import java.io.File; // Import the file class
import java.io.IOException;  // Import the IOException class to handle errors
public class LinearRegression {
	public void use () {
		try {
		    File myObj = new File("filename.txt");
		    if (myObj.createNewFile()) {
		      System.out.println("File created: " + myObj.getName());
		    } else {
		      System.out.println("File already exists.");
		    }
		  } catch (IOException e) {
		    System.out.println("An error occurred.");
		    e.printStackTrace();
		  }
	}
}
