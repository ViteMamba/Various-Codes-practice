#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct Process {
    int pid;
    int arrival;
    int burst;
    int completion;
    int turnaround;
    int waiting;
    int remaining;
};

// Comparator for min-heap based on burst time
struct CompareBurst {
    bool operator()(const Process &a, const Process &b) {
        return a.burst > b.burst; // smaller burst has higher priority
    }
};

int main() {
    // Min-heap of processes
    priority_queue<Process, vector<Process>, CompareBurst> pq;

    // Insert some processes
    pq.push({1, 0, 5, 0, 0, 0, 5});
    pq.push({2, 2, 3, 0, 0, 0, 3});
    pq.push({3, 1, 8, 0, 0, 0, 8});

    cout << "Processes in order of burst time:\n";
    while (!pq.empty()) {
        Process p = pq.top(); // get process with least burst time
        pq.pop();             // remove it
        cout << "PID: " << p.pid<<"Arrival: "<< p.arrival<< ", Burst: " << p.burst << endl;
    }

    return 0;
}
