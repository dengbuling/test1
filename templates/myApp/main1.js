/*function people(firstname, middlename, lastname) {
    this.fname = firstname;
    this.mname = middlename;
    this.lname = lastname;
    this.getFullName = function() {
        return `${this.fname} + ${this.mname} + ${this.lname}`;
    }
}

people.prototype.getFullName = function() {
    return `${this.fname} + ${this.mname} + ${this.lname}`;
}*/

class people {
    constructor(firstname, middlename, lastname) {
        this.fname = firstname;
        this.mname = middlename;
        this.lname = lastname;
    }
    getFullName(){
        return `${this.fname} + ${this.mname} + ${this.lname}`;
    }
}


console.log((new people('Harry', 'Jame', 'Potter')).getFullName())
person1 = (new people('Harry', 'Jame', 'Potter')).getFullName()
console.log(typeof person1)
console.log(new people('Harry', 'Jame', 'Potter'))