/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head){
    struct ListNode* p1 = head;
    struct ListNode* p2 = head;

    while (p1!= NULL && p1->next != NULL){
        p1=p1->next->next;
        p2 = p2->next;
    }
    return p2;
}