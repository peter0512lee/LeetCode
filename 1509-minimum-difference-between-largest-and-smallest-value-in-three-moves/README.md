<h2><a href="https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves">1509. Minimum Difference Between Largest and Smallest Value in Three Moves</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>In one move, you can choose one element of <code>nums</code> and change it to <strong>any value</strong>.</p>

<p>Return <em>the minimum difference between the largest and smallest value of <code>nums</code> <strong>after performing at most three moves</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,3,2,4]
<strong>Output:</strong> 0
<strong>Explanation:</strong> We can make at most 3 moves.
In the first move, change 2 to 3. nums becomes [5,3,3,4].
In the second move, change 4 to 3. nums becomes [5,3,3,3].
In the third move, change 5 to 3. nums becomes [3,3,3,3].
After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,0,10,14]
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can make at most 3 moves.
In the first move, change 5 to 0. nums becomes [1,0,0,10,14].
In the second move, change 10 to 0. nums becomes [1,0,0,0,14].
In the third move, change 14 to 1. nums becomes [1,0,0,0,1].
After performing 3 moves, the difference between the minimum and maximum is 1 - 0 = 1.
It can be shown that there is no way to make the difference 0 in 3 moves.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,100,20]
<strong>Output:</strong> 0
<strong>Explanation:</strong> We can make at most 3 moves.
In the first move, change 100 to 7. nums becomes [3,7,20].
In the second move, change 20 to 7. nums becomes [3,7,7].
In the third move, change 3 to 7. nums becomes [7,7,7].
After performing 3 moves, the difference between the minimum and maximum is 7 - 7 = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

### 想法
因為是要找最大值-最小值，所以一定是對於array的最大跟最小的地方進行操作。
我們可以得到以下結論:
如果排序後的陣列為:
[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
我們可以拿改變3次,所以會有以下組合。
* 改變 a1,a2,a3 =>答案為 a10 - a4
* 改變 a1,a2,a10 =>答案為 a9 - a3
* 改變 a1,a9,a10 =>答案為 a8 - a2
* 改變 a8,a9,a10 =>答案為 a7 - a1

所以我們只需要計算以上四種組合,然後在這四種組合中最小的即為答案。
