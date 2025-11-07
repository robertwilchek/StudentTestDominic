// Task 1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>

int main()
{
	std::cout << "Hello World!" << std::endl;

	std::ofstream outputFile("hello.txt");

	if (outputFile.is_open()) {
		outputFile << "Hello World!" << std::endl;
		outputFile.close();
	}
	else {
		std::cerr << "Error opening file" << std::endl;
	}
}

