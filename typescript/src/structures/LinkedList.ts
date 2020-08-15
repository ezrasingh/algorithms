import DataNode, { DataNodeType, DataKey } from './Data';

export default class LinkedList {
    private head: DataNode;

    constructor(state: any | any[]) {
        if (Array.isArray(state)) {
            state = state.reverse()
            this.head = new DataNode(state[0]);
            for(let i =0; i<state.length; i++){
                this.prepend(state[i])
            }
        } else {
            this.head = new DataNode(state);
        }
    }

    prepend(data: any): LinkedList {
        this.head = new DataNode(data, this.head);
        return this;
    }

    object(): DataNodeType[] {
        const representation = []
        let cursor: DataNode | null = this.head;
        while (cursor !== null) {
            if (cursor.next instanceof DataNode) {
                representation.push(cursor.object())
                cursor = cursor.next;
            } else {
                break;
            }
        }
        return representation;
    }
}