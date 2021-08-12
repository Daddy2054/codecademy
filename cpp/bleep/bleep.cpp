#include <iostream>
#include <string>

std::string word = "broccoli";
std::string text = "My favorite things are broccoli, and I love to eat a few boccoli at lunch. In my kitchen garden there are always plenty of broccoli";
void bleep (std::string word, std::string &text);

int main (){
    std::cout << text << "\n";
  bleep (word, text);
  std::cout << text << "\n";
  return 0;
}

void bleep (std::string word, std::string &text){

  std::cout << text << "\n";
  text = "ha ha ha";
  std::cout << text << "\n";

}
