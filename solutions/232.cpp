// Title: Implement Queue using Stacks
// Category: Stack
// Difficulty: Easy

/*
    Design:
    Use 2 stacks 's1' and 's2', s1's purpose is to hold the entirety of the queue
    while s2 is used to hold the correct order of the queue.
    
    Methods:
    push: push(x) onto the s1 stack. Do not transfer items to s2 at this point.
    Example: push(1) -> s1 = [1], s2 = []
             push(2) -> s1 = [1, 2], s2 = []
             Keep s1 filled, only transfer to s2 when necessary.
    
    pop(): 
    s2.pop() removes the correct element.
    If s2 is empty, transfer all elements from s1 to s2 to maintain the correct order.
    
    peek():
    s2.top() returns the correct element at the front of the queue.
    If s2 is empty, transfer all elements from s1 to s2.
    
    empty():
    s2.empty() and s1.empty() returns whether the queue is empty.
*/
#include <stack> 

class MyQueue {
public:
    MyQueue() {}
    
    void push(int x) {
        s1.push(x); 
    }

    int pop() {
        if ( s2.empty() ) {
            while ( !s1.empty() ) {
                s2.push(s1.top()); 
                s1.pop();
            }
        }
        int popValue = s2.top(); 
        s2.pop(); 
        return popValue; 
    }

    int peek() {
        if ( s2.empty() ) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop(); 
            }
        }
        return s2.top(); 
    }

    bool empty() {
        return s2.empty() && s1.empty(); 
    }

private:
    std::stack<int> s1;
    std::stack<int> s2;  
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */