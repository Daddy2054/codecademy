// all is broken!!!

let menu = {
    courses: {
        _appetizers: [],
        get appetizers() {
            return this.courses._appetizers;
        },
        set appetizers(appetizers1) {
//            this.courses.appetizers.push(appetizerIn);
            this.courses._appetizers = appetizers1;
        },
        mains: [],
        get mains() {
            return this.courses.mains;
        },
        set mains(mains) {
            this.courses.mains = mains;
        },
        desserts: [],
        get desserts() {
            return this.courses.desserts;
        },
        set desserts(desserts) {
            this.courses.desserts = desserts;
        },
    },

 /*   get courses() {
        return {
            appetizers: this.appetizers,
            mains: this.mains,
            desserts: this.desserts,
        }; */
  get courses() {
        return {
            appetizers: this.appetizers,
            mains: this.mains,
            desserts: this.desserts,
        };
    },

    addDishToCourse(courseName, dishName, dishPrice) {
        const dish = {
            name: dishName,
            price: dishPrice,
        };
       // return 
       this.courses[courseName].push(dish);
       // this.courses[courseName] = dish;
    },

    getRandomDishFromCourse(courseName) {
        const dishes = this.courses[courseName];
        const randomIndex = Math.floor(Math.random()*dishes.length);
        return dishes[randomIndex];
    },

    generateRandomMeal() {
        const appetizer = this.getRandomDishFromCourse('appetisers');
        const main = this.getRandomDishFromCourse('mains');
        const dessert = this.getRandomDishFromCourse('desserts');
        const totalPrice = appetizer.price + main-price + dessert.price;
        return 'Your meal is ${appetizer.name}, ${main.name} and ${dessert.name}, \
        and the total price is ${totalPrice}';
    },
};

menu.addDishToCourse('appetizers','Tuna Apple Bites', 2.67);
menu.addDishToCourse('appetizers','Spiced Cauliflower Tacos', 3.67);
menu.addDishToCourse('appetizers','corn Chip Fish Fingers', 5.67);
menu.addDishToCourse('mains','Beef Ramen', 3.38);
menu.addDishToCourse('mains','Minestrone', 4.38);
menu.addDishToCourse('mains','Tofu Miso Soup', 4.82);
menu.addDishToCourse('desserts','Lemon Coconut Slice', 2.27);
menu.addDishToCourse('desserts','Carrot Cake', 3.27);
menu.addDishToCourse('desserts','Easy Hedgehog Slice', 4.27);

let meal =menu.generateRandomMeal();
console.log(meal);


