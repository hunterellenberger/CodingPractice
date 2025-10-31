#include <iostream>
using namespace std;

struct Node{
    int number;
    int height;
    struct Node *left;
    struct Node *right;
};

struct Node *create_node(int digit, int height=0){
    struct Node *node = (struct Node*)malloc(sizeof(struct Node));
    node->number = digit;
    node->height = height;
    node->left = NULL;
    node->right = NULL;
    return node;
}

class BST{
    public:
        int c;
        Node *root;
        BST(Node *node){
            c = 0;
            root = node;
        }
        void insert_node(Node *node, int digit){
            if(digit > node->number && node->right == NULL){
                node->right = create_node(digit, (node->height) + 1);
                c += node->right->height;
            }
            else if(digit < node->number && node->left == NULL) {
                node->left = create_node(digit, (node->height) + 1);
                c += node->left->height;
            }
            else if(digit > node->number){
                insert_node(node->right, digit);
            }else{
                insert_node(node->left, digit);
            }
        }
};

int main(int argc, char *argv[]){
    int total;
    cin >> total;
    int numbers[total];

    for(int i = 0; i < total; i++){
        cin >> numbers[i];
    }

    cout << endl;

    BST bst = BST(create_node(numbers[0]));
    cout << bst.c << endl;
    for(int i = 1; i < total; i++){
        bst.insert_node(bst.root, numbers[i]);
        cout << bst.c << endl;
    }
}
