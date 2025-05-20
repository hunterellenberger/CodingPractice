#include <iostream>
#include <string>

int main(int argc, char *argv[]){
  std::string userName;
  std::cout << "Enter your name: ";
  std::cin >> userName;
  std::cout << "Hello " << userName << "!" << std::endl;

  return(0);
}
