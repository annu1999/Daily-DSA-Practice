Given a set of N jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job
  
Example -> 
Input:
N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
Output:
2 127
Explanation:
2 jobs can be done with
maximum profit of 127 (100+27).

Solution -> Time Complexity is O(N*logN) + O(N*M) (For Sorting + checking the empty position for job to perform)
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        Jobs.sort(reverse = True,key = lambda i:i.profit) #Sorting the Jobs based on maximum profit O(N*logN)
        
        maxDead = 0 #Finding the Maximum Deadline in Job Sequencing
        for i in range(n):
            if maxDead < Jobs[i].deadline:
                maxDead = Jobs[i].deadline
        check = [-1]*(maxDead+1) #Creating an array upto the maximum deadline
        
        countJobs,jobProfit = 0,0
        
        for i in range(n):     #O(N*M)
            for j in range(Jobs[i].deadline,0,-1):
                if check[j] == -1:
                    check[j] = i
                    countJobs += 1
                    jobProfit += Jobs[i].profit
                    break
        return [countJobs,jobProfit]

