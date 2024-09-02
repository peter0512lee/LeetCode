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
    ListNode* reverseKGroup(ListNode* head, int k) {
        // get the length
        int n = 0;
        ListNode* cur = head;
        while (cur != nullptr) {
            n += 1;
            cur = cur->next;
        }

        ListNode dummy(0, head);
        ListNode* p0 = &dummy;
        ListNode* pre = nullptr;
        cur = p0->next;
        while (n >= k) {
            n -= k;
            for (int i = 0; i < k; i++) {
                ListNode* nxt = cur-> next;
                cur->next = pre;
                pre = cur;
                cur = nxt;
            }

            ListNode* nxt = p0->next;
            p0->next->next = cur;
            p0->next = pre;
            p0 = nxt;
        }

        return dummy.next;
    }
};