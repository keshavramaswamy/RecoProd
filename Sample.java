import java.io.*;
import com.rapidminer.*;
import com.rapidminer.operator.*;
import com.rapidminer.tools.XMLException;
import java.lang.Object;
import com.rapidminer.RepositoryProcessLocation;
import com.rapidminer.repository.*;
    
public class Sample extends Thread {

public static void main(String[] args) throws IOException,InterruptedException {
  // set up the command and parameter
  String[] cmd0 = new String[2];
  cmd0[0] = "C:\\Python27\\python.exe";
  cmd0[1] = "IR_Component_module1.py";
  Runtime rt0 = Runtime.getRuntime();
  java.lang.Process pr0 = rt0.exec(cmd0);
  
  Thread.sleep(120000);
  String pythonScriptPath = "mod2.py";
  String pythonScriptPath2 = "rating.py";
  String pythonScriptPath3 = "module3_int.py";
  String pythonScriptPath4 = "plotmod3inp.py";
  
  String pythonScriptPath5 = "mod4.py";
  String pythonScriptPath6 = "new_gui.py";
  
  String[] cmd = new String[2];
  cmd[0] = "C:\\Python27\\python.exe";
  cmd[1] = pythonScriptPath;


 
   // create runtime to execute external command
  Runtime rt = Runtime.getRuntime();
  java.lang.Process pr = rt.exec(cmd);
 
  // retrieve output from python script
   BufferedReader bfr = new BufferedReader(new InputStreamReader(pr.getInputStream()));
   String line = "";
   while((line = bfr.readLine()) != null)
   {
         // display each output line form python script
            System.out.println(line);

   }
   
  //RM
  try {
         
          RapidMiner.setExecutionMode(RapidMiner.ExecutionMode.COMMAND_LINE);
          System.setProperty("rapidminer.home", "C:\\Program Files\\Rapid-I\\RapidMiner5");
          RapidMiner.init();
          Repository repo = RepositoryManager.getInstance(null).getRepository("Local Repository");
          RepositoryProcessLocation processLocation = new RepositoryProcessLocation(new RepositoryLocation(repo.getLocation(), "linsvmtest"));
          com.rapidminer.Process process = processLocation.load(null);
          process.run();
          
        }
      catch (IOException e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
      }
      catch (XMLException e)
      {
        // TODO Auto-generated catch block
        e.printStackTrace();
      }
      catch (OperatorException e)
      {
         // TODO Auto-generated catch block
        e.printStackTrace();
      } 
      catch (RepositoryException e)
      {
        // TODO Auto-generated catch block
        e.printStackTrace();
       }
      //end of rm
      String[] cmd2 = new String[2];
      cmd2[0] = "C:\\Python27\\python.exe";
      cmd2[1] = pythonScriptPath2;
      // create runtime to execute external command
      Runtime rt2 = Runtime.getRuntime();
      java.lang.Process pr2 = rt2.exec(cmd2);
      //Thread.sleep(1000);
      
      String[] cmd3 = new String[2];
      cmd3[0] = "C:\\Python27\\python.exe";
      cmd3[1] = pythonScriptPath3;
      // create runtime to execute external command
      Runtime rt3 = Runtime.getRuntime();
      java.lang.Process pr3 = rt3.exec(cmd3);
      
      try {
         
          RapidMiner.setExecutionMode(RapidMiner.ExecutionMode.COMMAND_LINE);
          System.setProperty("rapidminer.home", "C:\\Program Files\\Rapid-I\\RapidMiner5");
          RapidMiner.init();
          Repository repo = RepositoryManager.getInstance(null).getRepository("Local Repository");
          RepositoryProcessLocation processLocation = new RepositoryProcessLocation(new RepositoryLocation(repo.getLocation(), "mod3"));
          com.rapidminer.Process process = processLocation.load(null);
          process.run();
          
        }
      catch (IOException e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
      }
      catch (XMLException e)
      {
        // TODO Auto-generated catch block
        e.printStackTrace();
      }
      catch (OperatorException e)
      {
         // TODO Auto-generated catch block
        e.printStackTrace();
      } 
      catch (RepositoryException e)
      {
        // TODO Auto-generated catch block
        e.printStackTrace();
       }
      //end of rm
  
      String[] cmd4 = new String[2];
      cmd4[0] = "C:\\Python27\\python.exe";
      cmd4[1] = pythonScriptPath4;
      // create runtime to execute external command
      Runtime rt4 = Runtime.getRuntime();
      java.lang.Process pr4 = rt4.exec(cmd4);
      
      String[] cmd5 = new String[2];
      //cmd4[0] = "C:\\Users\\Goutham\\AppData\\Local\\Enthought\\Canopy\\User\\Scripts\\python.exe";
      cmd5[0] = "C:\\Python27\\python.exe";
      cmd5[1] = pythonScriptPath5;
      // create runtime to execute external command
      Runtime rt5 = Runtime.getRuntime();
      java.lang.Process pr5 = rt5.exec(cmd5);
      
      String[] cmd6 = new String[2];
      cmd6[0] = "C:\\Python27\\python.exe";
      cmd6[1] = pythonScriptPath6;
      // create runtime to execute external command
      Runtime rt6 = Runtime.getRuntime();
      java.lang.Process pr6 = rt6.exec(cmd6);
      
      System.out.println("asd");
  }
  
   
}
