# 
# word count 
# mimic the Linux wc command. 
# Demonstrates file reading. 
# 

def main():
    
   file_name = input( "Enter the file name: ")

   inp = open( file_name, "r")
   lines = 0
   chars = 0
   words = 0 

   line = inp.readline()
   while line != "":
        lines = lines + 1
        chars = chars + len( line)
        a  = line.split()
        # print( a) 
        words = words + len( a) 
        line = inp.readline()
    
   inp.close()
   print( "File: ", file_name, "Lines: ", lines, "Chars: ", chars, "Words: ", words) 

main() 
