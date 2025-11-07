// Task2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

// message is initially a null pointer. printLength attempts to dereference it which results in a segmentation fault
// I've added a conditional check to verify that textPtr is not null. If it is, we return an error.

#include <iostream>
#include <stdexcept>
#include <string>

void printLength(const std::string* textPtr)
{
    if (textPtr == nullptr) {
        std::cout << "Error: null pointer passed as textPtr" << std::endl;
        return;
    }
    std::cout << "Length: " << textPtr->size() << std::endl;
}

int main()
{
    std::string* message = nullptr;
    printLength(message);


    if (true)
    {
        throw std::runtime_error("Simulated failure in Task2");
    }

}
