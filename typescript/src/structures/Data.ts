export type DataKey = number;

export interface DataNodeType {
    key: DataKey;
    data: any;
    next?: DataKey | null;
}

export default class DataNode {
    static id: DataKey = 0;
    readonly key: DataKey;
    public data: any;
    private _next: DataNode | null;

    /** load data node */
    constructor(data: any, nextNode?: DataNode) {
        this.data = data;
        this._next = nextNode || null;
        this.key = DataNode.id++;
    }

    /** getter method for next node ref */
    get next(): DataNode | boolean {
        return this._next;
    }

    /** setter method for next node ref */
    set next(node: DataNode | boolean) {
        this._next = node instanceof DataNode ? node : null;
    }

    /** returns node representation */
    object(): DataNodeType {
        return {
            key: this.key,
            data: this.data,
            next: this._next === null ? null : this._next.key
        }
    }
}