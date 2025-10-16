#include <bits/stdc++.h>
using namespace std;
#define min(a, b) ((a) < (b) ? (a) : (b))

struct Process
{
    int pid;
    int arrival;
    int burst;
    int completion;
    int turnaround;
    int waiting;
    int remaining;
};
struct CompareBurst {
    bool operator()(const Process &a, const Process &b) {
        return a.burst > b.burst; 
    }
};

// Sort by AT
void sortByArrival(struct Process p[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (p[j].arrival > p[j + 1].arrival)
            {
                struct Process temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }
}

void sortByArrivalandBurst(struct Process p[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (p[j].arrival > p[j + 1].arrival)
            {
                struct Process temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
            else if (p[j].arrival == p[j + 1].arrival)
            {
                if (p[j].burst > p[j + 1].burst)
                {
                    struct Process temp = p[j];
                    p[j] = p[j + 1];
                    p[j + 1] = temp;
                }
            }
        }
    }
}

// FCFS
void fcfs(struct Process p[], int n)
{
    sortByArrival(p, n);
    int current = 0;
    float totalTAT = 0, totalWT = 0;

    for (int i = 0; i < n; i++)
    {
        if (current < p[i].arrival)
            current = p[i].arrival;
        p[i].completion = current + p[i].burst;
        p[i].turnaround = p[i].completion - p[i].arrival;
        p[i].waiting = p[i].turnaround - p[i].burst;
        current = p[i].completion;

        totalTAT += p[i].turnaround;
        totalWT += p[i].waiting;
    }

    printf("\n--- FCFS Scheduling ---\n");
    printf("PID\tAT\tBT\tCT\tTAT\tWT\n");
    for (int i = 0; i < n; i++)
        printf("%d\t%d\t%d\t%d\t%d\t%d\n",
               p[i].pid, p[i].arrival, p[i].burst, p[i].completion,
               p[i].turnaround, p[i].waiting);

    printf("\nAverage Turnaround Time: %.2f\n", totalTAT / n);
    printf("Average Waiting Time: %.2f\n", totalWT / n);
}

void sjf(struct Process p[], int n)
{
    sortByArrivalandBurst(p, n);
    int current = 0;
    float totalTAT = 0, totalWT = 0;

    for (int i = 0; i < n; i++)
    {
        if (current < p[i].arrival)
            current = p[i].arrival;
        p[i].completion = current + p[i].burst;
        p[i].turnaround = p[i].completion - p[i].arrival;
        p[i].waiting = p[i].turnaround - p[i].burst;
        current = p[i].completion;

        totalTAT += p[i].turnaround;
        totalWT += p[i].waiting;
    }

    printf("\n--- SJF Scheduling ---\n");
    printf("PID\tAT\tBT\tCT\tTAT\tWT\n");
    for (int i = 0; i < n; i++)
        printf("%d\t%d\t%d\t%d\t%d\t%d\n",
               p[i].pid, p[i].arrival, p[i].burst, p[i].completion,
               p[i].turnaround, p[i].waiting);

    printf("\nAverage Turnaround Time: %.2f\n", totalTAT / n);
    printf("Average Waiting Time: %.2f\n", totalWT / n);
}

void stcf(struct Process p[], int n)
{
    int currentTime = 0, completed = 0;
    for (int i = 0; i < n; i++) {
        p[i].remaining = p[i].burst;
    }
    while (completed < n) {
        int idx = -1;
        for (int i = 0; i < n; i++) {
            if (p[i].arrival <= currentTime && p[i].remaining > 0 && (idx == -1 || p[i].remaining < p[idx].remaining)) {
                idx = i;
            }
        }
        if (idx != -1) {
            p[idx].remaining--;
            currentTime++;
            if (p[idx].remaining == 0) {
                p[idx].completion = currentTime;
                p[idx].turnaround = currentTime - p[idx].arrival;
                p[idx].waiting = p[idx].turnaround - p[idx].burst;
                completed++;
            }
        } else {
            currentTime++;
        }
    }
    float totalTAT = 0, totalWT = 0;
    for (int i = 0; i < n; i++)
    {
        totalTAT += p[i].turnaround;
        totalWT += p[i].waiting;
    }
printf("\n--- FCFS Scheduling ---\n");
    printf("PID\tAT\tBT\tCT\tTAT\tWT\n");
    for (int i = 0; i < n; i++)
        printf("%d\t%d\t%d\t%d\t%d\t%d\n",
               p[i].pid, p[i].arrival, p[i].burst, p[i].completion,
               p[i].turnaround, p[i].waiting);

    printf("\nAverage Turnaround Time: %.2f\n", totalTAT / n);
    printf("Average Waiting Time: %.2f\n", totalWT / n);

}

int main()
{
    int n;
    printf("Enter number of processes: ");
    scanf("%d", &n);
    struct Process p[n];
    for (int i = 0; i < n; i++)
    {
        p[i].pid = i + 1;
        printf("Enter Arrival Time and Burst Time for P%d: ", i + 1);
        scanf("%d %d", &p[i].arrival, &p[i].burst);
    }
    stcf(p,n);
    return 0;
}