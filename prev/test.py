struct Node{
    Node * next;
    int value;
}

main(){
    Node * head = new Node;
    head->next = new Node;
    head->value = 10;

    head->next->next = new Node;
    head->next->value = 20;


}