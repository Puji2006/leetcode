class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i = 0;i<nums.length;i++){
            int key = nums[i];
            map.put(key,map.getOrDefault(key,0)+1);
        }
        int ans = -1;
        int n = nums.length/2;
        for(int macha:map.keySet()){
            int val = map.get(macha);
            if(val>n){
                ans = macha;
                break;
            }


        }
        return ans;
    }
}
