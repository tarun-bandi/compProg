class MedianFinder {
    priority_queue<int> smaller_half;  // max-heap for smaller elements
    priority_queue<int, vector<int>, greater<int>> larger_half; 

public:
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if (smaller_half.empty() || num < smaller_half.top()){
            smaller_half.push(num);
        }else{
            larger_half.push(num);
        }
        
        int total_elem_count = smaller_half.size() + larger_half.size();

        if (total_elem_count % 2 == 0){

            while (smaller_half.size() < larger_half.size()){
                smaller_half.push(larger_half.top());
                larger_half.pop();
            }

            while (smaller_half.size() > larger_half.size()){
                larger_half.push(smaller_half.top());
                smaller_half.pop();
            }
      
        } else {
            while (smaller_half.size() < larger_half.size() + 1){
                smaller_half.push(larger_half.top());
                larger_half.pop();
            }

            while (smaller_half.size() > larger_half.size() + 1){
                larger_half.push(smaller_half.top());
                smaller_half.pop();
            }

        }
        
    }
    
    double findMedian() {
        int total_elem_count = smaller_half.size() + larger_half.size();
        if (total_elem_count % 2 == 0){
            return ((double) smaller_half.top() + (double) larger_half.top()) / 2;
        }

        return smaller_half.top();
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */