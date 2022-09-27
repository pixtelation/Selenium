package Selenium;

import org.openqa.selenium.*;
import java.time.Duration;
import org.openqa.selenium.chrome.ChromeDriver;
import io.github.bonigarcia.wdm.WebDriverManager;

public class SeleniumClass {
	
	

	public static void main(String[] args)
	{
		//System.setProperty("webdriver.chrome.driver", "C:\\selenium-java-4.1.0\\chromedriver.exe");
		WebDriverManager.chromedriver().setup();
		WebDriver driver = new ChromeDriver();
		   
		
//		driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F");
//
//		driver.findElement(By.id("email--1")).sendKeys("Aniketshaw31@gmail.com");
//		driver.findElement(By.id("id_password")).sendKeys("papamummy@09");
	
		
		    driver.get("https://web.skype.com/");
		    
		   
		    
		    
//		    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(20));
//		    
	    driver.findElement(By.id("i0116")).click();
		driver.findElement(By.id("i0116")).sendKeys("abhishekmehta50@gmail.com");	  
		driver.findElement(By.xpath("//input[@type='submit']")).click();
//			
//			
//		if 	(driver.findElement(By.name("passwd")).isDisplayed());
//		{
//			try 
//			{
//			driver.findElement(By.id("i0118")).sendKeys("9681abhi");
//		 	}
//			catch (Exception e)
//			{
//				System.out.println(e);
//			}
//			
//		}
//		
//		
//		WebElement button = driver.findElement(By.id("idSIButton9"));
//	
//		if (button.isDisplayed())
//		{
//			System.out.println("Button found");
//		}
//		
	   
		
	}

	
	
}
