class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int>mpp;
        int n = nums.size();
        vector<int>ans;
        for(int i = 0;i<n;i++){
            mpp[nums[i]]++;
        }
        priority_queue<pair<int,int>>pq;
        for(auto i :mpp){
            pq.push({i.second,i.first});

        }
        while(k--){
            auto t = pq.top();
            ans.push_back(t.second);
            pq.pop();
        }
        return ans;

    }
};