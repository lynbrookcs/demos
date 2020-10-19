// Syntax Sugars in JavaScript

// declare variables without "var"
myVar = 123;

// no semicolon
console.log(myVar)

// lambda function
myFunc = (a, b) => {
    console.log("A is " + a);
    // template literals
    console.log(`B is ${b}`);
    console.log(`
        Template literals
        can be multiple lines
    `);
}

myFunc(420, 69);

myArray = [1, 2, 3, 4, 5];
myArray.forEach(item => {
    console.log(item);
});