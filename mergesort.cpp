#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::string;
using std::vector;

int main() {

  ifstream inputFile;
  ofstream outputFile;
  string inFileName, outFileName;

  do {
    std::cout << "Please enter the name of a file to read: " << endl;
    getline(cin, inFileName);
    inputFile.open(inFileName);
  } while (!inputFile);

  inputFile.close();

}
