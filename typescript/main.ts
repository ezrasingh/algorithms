import { LinkedList } from './src/structures';
//import * as algorithms from '@algorithms';

/**
 * Insert implementation driver code here
 */
async function main(): Promise<any>{
    const list = new LinkedList([12, 10, 9])
    console.log(list.object());
};

main();