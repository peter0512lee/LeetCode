/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0, head);
        auto node0 = &dummy;
        auto node1 = head;
        while (node1 && node1->next) {
            auto node2 = node1->next;
            auto node3 = node2->next;

            node0->next = node2; // 0 -> 2
            node2->next = node1; // 2 -> 1
            node1->next = node3; // 1 -> 3

            node0 = node1; // 下一輪交換，0 是 1
            node1 = node3; // 下一輪交換，1 是 3
        }
        return dummy.next;
    }
};