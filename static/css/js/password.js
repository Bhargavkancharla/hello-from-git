let a = document.getElementById('t9');   // password
let b = document.getElementById('t10');  // confirm password
let msg = document.getElementById('message');
let form = document.querySelector("form");

// Run check while typing
b.addEventListener('keyup', function() {
    if (a.value !== b.value) {
        msg.textContent = 'Passwords do not match';
        msg.style.color = 'red';
    } else {
        msg.textContent = 'Passwords match';
        msg.style.color = 'green';
    }
});

// Stop form submission if not matching
form.addEventListener("submit", function(e) {
    if (a.value !== b.value) {
        e.preventDefault(); // block submission
        msg.textContent = "Passwords do not match!";
        msg.style.color = "red";
    }
});
