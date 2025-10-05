const usersDatabase = {
    'karatu501': {
        firstName: 'Karatu',
        lastName: 'Oyekunle',
        email: 'menuthegod@gmail.com',
        accountActivated: true,
        password: 'password123'
    },
    'johndoe': {
        firstName: 'John',
        lastName: 'Doe',
        email: 'adebayoismail@gmail.com',
        accountActivated: false,
        password: 'password456'
    },           
}

function displayUserDetails() {
    let username = prompt("Enter your username");

    while (validateUsername(username) == false) {
        username = prompt("Please enter a valid username")
    }
    if (username == null || username == "") {
        return;
    }

    let password = prompt("Enter your password");

    while (validatePassword(password) == false) {
        password = prompt("Incorrect password. Please enter a valid password")
    }
    if (username == null || username == "") {
        return;
    }

    let passwordConfirm = prompt("Confirm your password");
    
    while (passwordConfirm !== password) {
        passwordConfirm = prompt("Password does not match. Please confirm your password")
    }
    if (passwordConfirm == null || passwordConfirm == "") {
        return;
    }
   
    if (username == undefined) {
        alert("Password doesn't exist. Find another way to login");
        return
    }
    console.log(username, password, passwordConfirm);
}
console.log (user)
    alert("Welcome " + usersDatabase[username].firstName + " " + usersDatabase[username].lastName + "!");
    alert("Your email is " + usersDatabase[username].email);
    if (usersDatabase[username].accountActivated) {
        alert("Your account is activated");
    } else {
        alert("Your account is not activated");
    } 
    const user = usersDatabase[username];
displayUserDetails();
alert("You have come the end of this prompt. Goodbye!"); 

// const validateUsername = (name) => {
//     return name.length <= 10;
// }

function validateUsername(username) {
    if (username == null || username == "") {
        return true;
    } 

    if (username.length > 10) {
        return false;
    } else {
        return true;
    }
}
function validatePassword(password) {
    if (password == null) {
        return true;
    }
    if (password.length < 6) {
        return false;
    } else  {
        return true;
    }
}

