// Set and Objects is use hashing in the background
// Hash Table is an data structure that use hash function to map keys to buckets or slots
// to store values

// This is user defined sets and objects
class HashTable {
  constructor() {
    this.size = 10;
    this.table = Array.from({ length: this.size }, () => []);
    console.log("this is self table    -       -       -> ", this.table);
  }

  add(key) {
    const idx = key % this.size; //  Hash Function
    console.log(
      "this is add idx -> ",
      idx,
      "this is key -> ",
      key,
      "this is total size -> ",
      this.size
    );
    if (!this.table[idx].includes(key)) {
      this.table[idx].push(key);
    }
  }
  contains(key) {
    const idx = key % this.size; //  Hash Function
    return this.table[idx].includes(key);
  }
}

const hashTable = new HashTable();
hashTable.add(2);
hashTable.add(234);
hashTable.add(5432);
hashTable.add(432);
hashTable.add(453);
hashTable.add(48732);
hashTable.add(454332);

console.log(hashTable.table);

// this is built-in set

const sets = new Set(); // If you want make simple only Values
sets.add(324);
sets.add(432);
sets.add(324234);
sets.add(543);
sets.add(4398);
console.log(sets.has(3));
console.log(sets);

const objects = {};
objects[32] = 35432;
console.log(objects);
