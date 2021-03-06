# DataStructure

排序方法 | 时间复杂度（平均）   | 时间复杂度（最好）  | 时间复杂度（最坏）  | 空间复杂度）  | 稳定性 
-|-|-|-|-|-
插入排序 | $O(n^2)$ | $O(n^2)$ | $O(n)$ |$O(1)$|稳定
希尔排序 | $O(n^{1.3})$ |$O(n^2)$|$O(n)$|$O(1)$| 不稳定
选择排序 | $O(n^2)$ |$O(n^2)$| $O(n^2)$|$O(1)$|不稳定
堆排序  |  $O(nlog_2n)$ |$O(nlog_2n)$ |$O(nlog_2n)$ |$O(1)$|不稳定
冒泡排序 | $O(n^2)$ |$O(n^2)$|$O(n)$|$O(1)$|稳定
快速排序 | $O(nlog_2n)$ |$O(n^2)$ |$O(nlog_2n)$ |$O(nlog_2n)$|不稳定
归并排序 | $O(nlog_2n)$ |$O(nlog_2n)$ |$O(nlog_2n)$ |$O(n^2)$|稳定
计数排序 |$O(n+k)$|$O(n+k)$|$O(n+k)$|$O(n+k)$|稳定
桶排序   |$O(n+k)$|$O(n^2)$|$O(n)$|$O(n+k)$|稳定
基数排序 |$O(nk)$|$O(nk)$|$O(nk)$|$O(n+k)$|稳定

# 插入排序

- 从第一个元素开始，该元素可以认为已经被排序；
- 取出下一个元素，在已经排序的元素序列中从后向前扫描；
- 如果该元素（已排序）大于新元素，将该元素移到下一位置；
- 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
- 将新元素插入到该位置后；
- 重复步骤2~5。


# 希尔排序

- 选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
- 按增量序列个数k，对序列进行k 趟排序；
- 每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

# 选择排序

- 初始状态：无序区为R[1..n]，有序区为空；
- 第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
- n-1趟结束，数组有序化了。


# 堆排序

- 将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
- 将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
- 由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。

# 冒泡排序
- 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
- 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
- 针对所有的元素重复以上的步骤，除了最后一个；
- 重复步骤1~3，直到排序完成。

# 快速排序

- 从数列中挑出一个元素，称为 “基准”（pivot）；
- 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
- 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

# 归并排序

- 把长度为n的输入序列分成两个长度为n/2的子序列；
- 对这两个子序列分别采用归并排序；
- 将两个排序好的子序列合并成一个最终的排序序列。

# 计数排序
- 找出待排序的数组中最大和最小的元素；
- 统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
- 对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
- 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。

# 桶排序
- 设置一个定量的数组当作空桶；
- 遍历输入数据，并且把数据一个一个放到对应的桶里去；
- 对每个不是空的桶进行排序；
- 从不是空的桶里把排好序的数据拼接起来。 


# 基数排序
- 取得数组中的最大数，并取得位数；
- arr为原始数组，从最低位开始取每个位组成radix数组；
- 对radix进行计数排序（利用计数排序适用于小范围数的特点）
