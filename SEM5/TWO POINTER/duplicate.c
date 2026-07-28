int findDuplicate(int* nums, int N){
    int low=1,high=N-1;
    while(low<high){
        int mid=low+(high-low)/2;
        int cnt=0;
        for(int i=0;i<N;i++){
            if(nums[i]<=mid) cnt++;
        }
        if(cnt>mid) high=mid;
            else low=mid+1;
        }
        return low;
}
