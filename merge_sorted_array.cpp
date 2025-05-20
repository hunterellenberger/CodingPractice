#include <iostream>
#include <vector>
#include <cstdlib>

void merge_sorted_array(std::vector<int> &arr1, int count1, std::vector<int> &arr2, int count2);
void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n);

int main(int argc, char *argv[]){

	//char *arrayOne = argv[1];
	//int countOne = atoi(argv[2]);
	//char *arrayTwo = argv[3];
	//int conutTwo = atoi(argv[4]);

	std::vector<int> nums1 = {2, 0};
	int size1 = 1;
	std::vector<int> nums2 = {1};
	int size2 = 1;

	merge_sorted_array(nums1, size1, nums2, size2);
	//merge(nums1, size1, nums2, size2);

	for(int num : nums1){
		std::cout << num << std::endl;
	}

	return 0;
}

void merge_sorted_array(std::vector<int>& arr1, int count1, std::vector<int>& arr2, int count2){
	if(count1 == 0) 
		arr1 = arr2;
	else if(count2 != 0){
		std::vector<int> tmpArr;

		for(int i = 0, j = 0; i < count1 || j < count2;){
			if(arr1[i] < arr2[j]){
				tmpArr.push_back(arr1[i]);
				i++;
			}else{
				tmpArr.push_back(arr2[j]);
				j++;
			}
		}

		arr1 = tmpArr;
	}


}

void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
	if(m == 0) 
		nums1 = nums2;
	else if(n != 0){
		std::vector<int> tmpArr;

		for(int i = 0, j = 0; i < m && j < n;){
			if(nums1[i] < nums2[j]){
				tmpArr.push_back(nums1[i]);
				i++;
			}else{
				tmpArr.push_back(nums2[j]);
				j++;
			}
		}

		nums1 = tmpArr;
	}
}