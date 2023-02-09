/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

import java.io.*;
import java.util.*;
class Solution {
    public List<Integer> preorder(Node root) {
        ArrayList<Integer> ret = new ArrayList<Integer>();
        // Node current = root;
        // ret.add(current.val);
        if (root==null){
            return ret;
        }
        Stack<Node>  s = new Stack<Node>();
        s.push(root);


        while (!s.isEmpty()){
            Node current = s.pop();
           try{
                List<Node> temp = current.children;
                Collections.reverse((temp));

                for (Node child : temp){
                    if (!ret.contains(child)){
                        s.push(child);
                    }
                }
                ret.add(current.val);
           }
           catch(Exception e){
               
           }
            
        }
        return ret;
    }
}