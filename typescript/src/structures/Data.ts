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

    constructor(data: any, nextNode?: DataNode) {
        this.data = data;
        this._next = nextNode || null;
        this.key = DataNode.id++;
    }

    get next(): DataNode | boolean {
        return this._next;
    }

    set next(node: DataNode | boolean) {
        this._next = node instanceof DataNode ? node : null;
    }

    object(): DataNodeType {
        return {
            key: this.key,
            data: this.data,
            next: this._next === null ? null : this._next.key
        }
    }
}