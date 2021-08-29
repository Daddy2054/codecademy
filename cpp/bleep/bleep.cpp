#include <iostream> 
#include <string>
#include <cstring>

char word[] = "broccoli";
char text[] = "My favorite things are broccoli, and I love to eat a few broccoli at lunch. In my kitchen garden there are always plenty of broccoli";
char bleep[]= "********";
int bleep_size = sizeof(bleep)-1;

 int main (){
  char * ptr;
  std::cout << text << '\n';
  do {
    ptr = strstr(  text,  word);  
    if (ptr) {
      strncpy ( ptr, bleep, bleep_size );
    }
  } while (ptr != NULL);
  std::cout << text << '\n';
  return 0;
}
