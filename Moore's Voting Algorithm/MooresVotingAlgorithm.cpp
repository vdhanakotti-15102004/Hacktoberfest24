#include <iostream>
#include <vector>
using namespace std;

int findMajorityCandidate(const vector<int>& nums) {
    int candidate = 0, count = 0;
    
    // Phase 1: Find a potential candidate
    for (int num : nums) {
        if (count == 0) {
            candidate = num;  // Set the current number as the candidate
        }
        if (num == candidate) {
            count++;
        } else {
            count--;
        }
    }
    
    return candidate;  // This is the potential candidate
}

bool isMajority(const vector<int>& nums, int candidate) {
    int count = 0;
    for (int num : nums) {
        if (num == candidate) {
            count++;
        }
    }
    return count > nums.size() / 2;
}

int majorityElement(const vector<int>& nums) {
    int candidate = findMajorityCandidate(nums);
    
    // Phase 2: Verify if the candidate is the majority element
    if (isMajority(nums, candidate)) {
        return candidate;
    } else {
        return -1;  // No majority element found
    }
}

int main() {
    int n;
    
    cout << "Enter the number of votes: ";
    cin >> n;
    
    if (n <= 0) {
        cout << "Invalid number of votes. Please enter a positive number." << endl;
        return 1;
    }

    vector<int> nums(n);
    cout << "Enter the votes (numbers separated by space): ";
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int result = majorityElement(nums);
    
    if (result != -1) {
        cout << "The Majority Element is: " << result << endl;
    } else {
        cout << "No Majority Element found." << endl;
    }

    return 0;
}

