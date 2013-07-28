//
//  main.cpp
//  min_cuts
//
//  Created by Mohammad Rashid on 28/07/2013.
//  Copyright (c) 2013 Mohammad Rashid. All rights reserved.
//

#include <iostream>
#include <fstream>


int main(int argc, const char * argv[])
{
    std::ifstream input("//Users//Rashid//Documents//Dev//python//algorithms//min_cuts//test.txt");
    std::string line;
    
    while( std::getline( input, line ) ) {
        std::cout<<line<<'\n';
    }
    
    return 0;
}

