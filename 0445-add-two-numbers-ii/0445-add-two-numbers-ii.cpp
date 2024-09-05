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
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        auto new_head = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return new_head;
    }

    ListNode* addTwo(ListNode* l1, ListNode* l2, int carry = 0) {
        if (l1 == nullptr && l2 == nullptr) {
            return carry ? new ListNode(carry) : nullptr;
        }
        if (l1 == nullptr) {
            swap(l1, l2);
        }
        carry += l1->val + (l2 ? l2->val : 0);
        l1->val = carry % 10;
        l1->next = addTwo(l1->next, (l2 ? l2->next : nullptr), carry / 10);
        return l1;
    }
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        l1 = reverseList(l1);
        l2 = reverseList(l2);
        auto l3 = addTwo(l1, l2);
        return reverseList(l3);
    }
};