#include <iostream>
#include <string>

int absDifference(std::string s, std::string t);

int main(int argc, char *argv[]){
	std::string s(argv[1]);
	std::string t(argv[2]);

	std::cout << absDifference(s, t) << std::endl;

	return 0;
}

int absDifference(std::string s, std::string t){
	int difference = 0;

	for(int i = 0; i < static_cast<int>(s.length()); i++){
		for(int j = 0; j < static_cast<int>(s.length()); j++){
			if(s[i] == t[j]){
				if((i - j) < 0){
					difference += j - i;
				}else{
					difference += i - j;
				}
			}
		}
	}

	return difference;
}