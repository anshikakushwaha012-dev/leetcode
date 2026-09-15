/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize) {
    int* a = malloc(numsSize * sizeof(int));
    int current_sum=0;
    for(int i=0;i< numsSize;i++){
        current_sum+=nums[i];
        a[i]=current_sum;
    }
    *returnSize=numsSize;
    return a;
}