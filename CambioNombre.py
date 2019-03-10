# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    i = 300
      
    for filename in os.listdir("/data/estudiantes/aves/Tesis_Aves/AVES/Elanusleucurus/4Elanusleucurus/"): 
        dst ="00" + str(i) + ".jpg"
        src ='/data/estudiantes/aves/Tesis_Aves/AVES/Elanusleucurus/4Elanusleucurus/'+ filename 
        dst ='/data/estudiantes/aves/Tesis_Aves/AVES/Elanusleucurus/4Elanusleucurus/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 


