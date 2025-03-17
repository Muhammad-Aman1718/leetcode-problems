// // String Methods

// let str = "Hello, World!";

// // charAt
// console.log(str.charAt(0)); // "H"

// // charCodeAt
// console.log(str.charCodeAt(0)); // 72 (ASCII of 'H')

// // concat
// console.log(str.concat(" How are you?")); // "Hello, World! How are you?"

// // includes
// console.log(str.includes("World")); // true

// // indexOf
// console.log(str.indexOf("o")); // 4

// // lastIndexOf
// console.log(str.lastIndexOf("o")); // 8

// // match
// console.log(str.match(/o/g)); // ['o', 'o']

// // padStart
// console.log(str.padStart(20, "*")); // "*****Hello, World!"

// // padEnd
// console.log(str.padEnd(20, "*")); // "Hello, World!*****"

// // repeat
// console.log(str.repeat(2)); // "Hello, World!Hello, World!"

// // replace
// console.log(str.replace("World", "JS")); // "Hello, JS!"

// // replaceAll
// console.log(str.replaceAll("o", "0")); // "Hell0, W0rld!"

// // search
// console.log(str.search("World")); // 7

// // slice
// console.log(str.slice(7, 12)); // "World"

// // split
// console.log(str.split(", ")); // ["Hello", "World!"]

// // startsWith
// console.log(str.startsWith("Hello")); // true

// // endsWith
// console.log(str.endsWith("!")); // true

// // substring
// console.log(str.substring(0, 5)); // "Hello"

// // toLowerCase
// console.log(str.toLowerCase()); // "hello, world!"

// // toUpperCase
// console.log(str.toUpperCase()); // "HELLO, WORLD!"

// // trim
// console.log("  Hello  ".trim()); // "Hello"

// // trimStart
// console.log("  Hello  ".trimStart()); // "Hello  "

// // trimEnd
// console.log("  Hello  ".trimEnd()); // "  Hello"

// // Arrays Method

// let arr = [10, 20, 30, 40, 50];

// // at
// console.log(arr.at(2)); // 30

// // concat
// console.log(arr.concat([60, 70])); // [10, 20, 30, 40, 50, 60, 70]

// // copyWithin
// console.log(arr.copyWithin(1, 3)); // [10, 40, 50, 40, 50]

// // entries
// let iterator = arr.entries();
// for (let e of iterator) console.log(e); // [0, 10] [1, 20] ...

// // every
// console.log(arr.every((num) => num > 5)); // true

// // fill
// console.log(arr.fill(100, 1, 3)); // [10, 100, 100, 40, 50]

// // filter
// console.log(arr.filter((num) => num > 20)); // [30, 40, 50]

// // find
// console.log(arr.find((num) => num > 20)); // 30

// // findIndex
// console.log(arr.findIndex((num) => num > 20)); // 2

// // flat
// let nestedArr = [1, [2, 3], [4, 5]];
// console.log(nestedArr.flat()); // [1, 2, 3, 4, 5]

// // flatMap
// console.log(arr.flatMap((num) => [num * 2])); // [20, 40, 60, 80, 100]

// // forEach
// arr.forEach((num) => console.log(num)); // 10 20 30 40 50

// // includes
// console.log(arr.includes(30)); // true

// // indexOf
// console.log(arr.indexOf(30)); // 2

// // join
// console.log(arr.join(" - ")); // "10 - 20 - 30 - 40 - 50"

// // keys
// let keyIterator = arr.keys();
// for (let key of keyIterator) console.log(key); // 0 1 2 3 4

// // map
// console.log(arr.map((num) => num * 2)); // [20, 40, 60, 80, 100]

// // pop
// console.log(arr.pop()); // 50

// // push
// arr.push(60);
// console.log(arr); // [10, 20, 30, 40, 60]

// // reduce
// console.log(arr.reduce((acc, num) => acc + num, 0)); // 160

// // reverse
// console.log(arr.reverse()); // [60, 40, 30, 20, 10]

// // shift
// console.log(arr.shift()); // 60

// // slice
// console.log(arr.slice(1, 3)); // [40, 30]

// // some
// console.log(arr.some((num) => num > 50)); // false

// // sort
// console.log(arr.sort((a, b) => a - b)); // [10, 20, 30, 40]

// // splice
// arr.splice(1, 1, 25);
// console.log(arr); // [10, 25, 30, 40]

// // toString
// console.log(arr.toString()); // "10,25,30,40"

// // unshift
// arr.unshift(5);
// console.log(arr); // [5, 10, 25, 30, 40]

// // values
// let valueIterator = arr.values();
// for (let val of valueIterator) console.log(val); // 5 10 25 30 40

// // Object Method

// let obj = { name: "Ali", age: 25, city: "Lahore" };

// // assign
// let newObj = Object.assign({}, obj, { country: "Pakistan" });
// console.log(newObj); // { name: "Ali", age: 25, city: "Lahore", country: "Pakistan" }

// // create
// let prototypeObj = { greet: () => "Hello" };
// let newObj2 = Object.create(prototypeObj);
// console.log(newObj2.greet()); // "Hello"

// // entries
// console.log(Object.entries(obj)); // [["name", "Ali"], ["age", 25], ["city", "Lahore"]]

// // freeze
// Object.freeze(obj);
// obj.name = "Ahmed"; // No effect
// console.log(obj.name); // "Ali"

// // fromEntries
// let arrToObject = Object.fromEntries([
//   ["a", 1],
//   ["b", 2],
// ]);
// console.log(arrToObject); // { a: 1, b: 2 }

// // getOwnPropertyNames
// console.log(Object.getOwnPropertyNames(obj)); // ["name", "age", "city"]

// // hasOwnProperty
// console.log(obj.hasOwnProperty("age")); // true

// // is
// console.log(Object.is(5, 5)); // true

// // keys
// console.log(Object.keys(obj)); // ["name", "age", "city"]

// // values
// console.log(Object.values(obj)); // ["Ali", 25, "Lahore"]

// // seal
// Object.seal(obj);
// obj.name = "Usman"; // Allowed
// delete obj.age; // Not allowed
// console.log(obj); // { name: "Usman", age: 25, city: "Lahore" }


