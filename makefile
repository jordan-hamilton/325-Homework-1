# Source: http://web.engr.oregonstate.edu/~rookert/cs162/03.mp4

CXX = g++
CXXFLAGS = -std=c++0x
CXXFLAGS += -Wall
CXXFLAGS += -pedantic-errors
CXXFLAGS += -g

EXECS = mergesort insertsort
SRCS = mergesort.cpp insertsort.cpp

all: $(EXECS)

mergesort: mergesort.cpp
	$(CXX) $(CXXFLAGS) mergesort.cpp -o mergesort

insertsort: insertsort.cpp
	$(CXX) $(CXXFLAGS) insertsort.cpp -o insertsort

clean:
	rm mergesort insertsort
	rm -r *.dSYM
