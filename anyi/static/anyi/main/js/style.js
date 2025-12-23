window.addEventListener("load", function () {
    document.querySelector(".preloader").classList.add("opacity-0");
    setTimeout(function () {
        document.querySelector(".preloader").style.display = "none";
    }, 1000);
});


document.querySelectorAll(".showTextButton").forEach(button => {
    button.onclick = function () {
        const hiddenText = document.getElementById("hiddenText");
        hiddenText.style.display = "block";
    };
});


// Portfolio Filter
const filterContainer = document.querySelector(".portfolio-filter"),
    filterBtns = filterContainer.children,
    totalFilterBtn = filterBtns.length,
    portfolioItems = document.querySelectorAll(".portfolio-item"),
    totalportfolioItem = portfolioItems.length;

for (let i = 0; i < totalFilterBtn; i++) {
    filterBtns[i].addEventListener("click", function () {
        filterContainer.querySelector(".active").classList.remove("active");
        this.classList.add("active");

        const filterValue = this.getAttribute("data-filter");
        for (let k = 0; k < totalportfolioItem; k++) {
            if (filterValue === portfolioItems[k].getAttribute("data-category")) {
                portfolioItems[k].classList.remove("hide");
                portfolioItems[k].classList.add("show");
            } else {
                portfolioItems[k].classList.remove("show");
                portfolioItems[k].classList.add("hide");
            }
        }
    });
}

// Portfolio Lightbox
const lightbox = document.querySelector(".lightbox"),
    lightboxImg = lightbox.querySelector(".lightbox-img"),
    lightboxClose = lightbox.querySelector(".lightbox-close"),
    lightboxText = lightbox.querySelector(".caption-text"),
    lightboxCounter = lightbox.querySelector(".caption-counter");
let itemIndex = 0;

for (let i = 0; i < totalportfolioItem; i++) {
    portfolioItems[i].addEventListener("click", function () {
        itemIndex = i;
        changeItem();
        toggleLightbox();
    });
}

function nextItem() {
    itemIndex = (itemIndex + 1) % totalportfolioItem;
    changeItem();
}

function previousItem() {
    itemIndex = (itemIndex - 1 + totalportfolioItem) % totalportfolioItem;
    changeItem();
}

function toggleLightbox() {
    lightbox.classList.toggle("open");
}

function changeItem() {
    const imgSrc = portfolioItems[itemIndex].querySelector(".portfolio-img img").getAttribute("src");
    lightboxImg.src = imgSrc;
    lightboxText.innerHTML = portfolioItems[itemIndex].querySelector("h4").innerHTML;
    lightboxCounter.innerHTML = (itemIndex + 1) + " of " + totalportfolioItem;
}

// Close Lightbox
lightbox.addEventListener("click", function (event) {
    if (event.target === lightbox || event.target.classList.contains("lightbox-close")) {
        toggleLightbox();
    }
});

// Aside Nav
const nav = document.querySelector(".nav"),
    navList = nav.querySelectorAll("li"),
    totalNavList = navList.length,
    allSection = document.querySelectorAll(".section"),
    totalSection = allSection.length;

for (let i = 0; i < totalNavList; i++) {
    const a = navList[i].querySelector("a");
    a.addEventListener("click", function () {
        removeBackSectionClass();

        for (let j = 0; j < totalNavList; j++) {
            if (navList[j].querySelector("a").classList.contains("active")) {
                addBackSectionClass(j);
            }
            navList[j].querySelector("a").classList.remove("active");
        }
        this.classList.add("active");
        showSection(this);

        if (window.innerWidth < 1200) {
            asideSectionTogglerBtn();
        }
    });
}

function removeBackSectionClass() {
    for (let i = 0; i < totalSection; i++) {
        allSection[i].classList.remove("active");
    }
}

function addBackSectionClass(num) {
    allSection[num].classList.add("back-section");
}

function showSection(element) {
    for (let i = 0; i < totalSection; i++) {
        allSection[i].classList.remove("active");
    }
    const target = element.getAttribute("href").split("#")[1];
    document.querySelector("#" + target).classList.add("active");
}

function updateNav(element) {
    for (let i = 0; i < totalNavList; i++) {
        navList[i].querySelector("a").classList.remove("active");
        const target = element.getAttribute("href").split("#")[1];
        if (navList[i].querySelector("a").getAttribute("href").split("#")[1] === target) {
            navList[i].querySelector("a").classList.add("active");
        }
    }
}

document.querySelector(".hire-me").addEventListener("click", function () {
    const sectionIndex = this.getAttribute("data-section-index");
    showSection(this);
    updateNav(this);
});

const navToggleBtn = document.querySelector(".nav-toggle"),
    aside = document.querySelector(".aside");

navToggleBtn.addEventListener("click", asideSectionTogglerBtn);

function asideSectionTogglerBtn() {
    aside.classList.toggle("open");
    navToggleBtn.classList.toggle("open");
    for (let i = 0; i < totalSection; i++) {
        allSection[i].classList.toggle("open");
    }
}

function showTable() {
    const table = document.getElementById('teacher');
    table.classList.remove('hidden');
}

function myFunction() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            tr[i].style.display = txtValue.toUpperCase().indexOf(filter) > -1 ? "" : "none";
        }
    }
}

// End Of Asid Nav


// test Section


// let currentTerm = 1;

// function showTable(className) {
//     // Hide all tables
//     document.querySelectorAll('.ca-table').forEach((table) => table.style.display = 'none');
//     // Show the selected class table
//     document.getElementById(`table-${className}`).style.display = 'block';
//     // Display term navigation
//     document.getElementById('prevTerm').style.display = currentTerm > 1 ? 'inline' : 'none';
//     document.getElementById('nextTerm').style.display = currentTerm < 3 ? 'inline' : 'none';
//     document.getElementById('submit-container').style.display = 'block';
// }

// function toggleTerm(direction) {
//     currentTerm += direction;
//     // Show/hide term buttons
//     document.getElementById('prevTerm').style.display = currentTerm > 1 ? 'inline' : 'none';
//     document.getElementById('nextTerm').style.display = currentTerm < 3 ? 'inline' : 'none';
// }

// function calculateTotal(input) {
//     const row = input.closest('tr');
//     const scores = row.querySelectorAll('.ca-score');
//     let total = 0;
//     scores.forEach((score) => {
//         total += Math.min(Number(score.value) || 0, Number(score.dataset.max));
//     });
//     const totalCell = row.querySelector('.total-score');
//     totalCell.textContent = Math.min(total, 40);
// }

// function submitScores() {
//     // Collect data and send via AJAX
//     const data = [];
//     document.querySelectorAll('.ca-table').forEach((table) => {
//         if (table.style.display !== 'none') {
//             table.querySelectorAll('tr').forEach((row) => {
//                 const studentName = row.cells[0].textContent;
//                 const scores = Array.from(row.querySelectorAll('.ca-score')).map((input) => input.value || 0);
//                 const total = row.querySelector('.total-score').textContent;
//                 data.push({ studentName, scores, total, term: currentTerm });
//             });
//         }
//     });

//     console.log('Submitting data:', data);
//     // TODO: Send data to the server via AJAX
// }


// // // Show Table Based on Selected Class
// // function showTable(className) {
// //     const tables = document.querySelectorAll('.ca-table');
// //     tables.forEach((table) => {
// //         if (table.id === `table-${className}`) {
// //             table.style.display = 'table'; // Show the specific table
// //         } else {
// //             table.style.display = 'none'; // Hide other tables
// //         }
// //     });
// // }

// // Calculate Total CA Score
// function calculateTotal(input) {
//     const row = input.closest('tr');
//     const scores = row.querySelectorAll('.ca-score');
//     const totalSpan = row.querySelector('.total-score');
//     let total = 0;

//     scores.forEach((score) => {
//         const value = parseInt(score.value) || 0;
//         if (value > 10) {
//             alert('Scores cannot exceed 10!');
//             score.value = 0;
//         } else {
//             total += value;
//         }
//     });

//     if (total > 40) {
//         alert('Total cannot exceed 40!');
//         total = 0;
//     }

//     totalSpan.textContent = total;
// }


// // Toggle Done/Edit Mode
// function toggleRow(button) {
//     const row = button.closest('tr');
//     const inputs = row.querySelectorAll('.ca-score');
//     const isDone = button.textContent === 'Done';

//     inputs.forEach((input) => {
//         input.disabled = isDone;
//     });

//     button.textContent = isDone ? 'Edit' : 'Done';
// }

// // Submit Scores (Stub Function)
// function submitScores() {
//     alert('Scores submitted successfully!');
//     // Implement your AJAX or form submission logic here
// }

// // Test Table  Ends







// Exam Table Begins


function showExamTable(className) {
    console.log(`Attempting to show exam table for class: ${className}`);

    // Hide all exam tables first
    document.querySelectorAll('.ba-exam-table').forEach((table) => {
        table.style.display = 'none';
    });

    // Get the specific exam table
    const selectedExamTable = document.getElementById(`exam-table-${className}`);
    if (selectedExamTable) {
        selectedExamTable.style.display = 'table';
    } else {
        console.error(`Exam table for class '${className}' not found.`);
    }
}

function calculateExamTotal(input) {
    const max = parseFloat(input.dataset.max) || 0;
    let value = parseFloat(input.value) || 0;

    // Limit the input value to the maximum allowed
    if (value > max) {
        alert(`The value cannot exceed ${max}.`);
        input.value = max; // Reset to max
        value = max;
    }

    const row = input.closest('tr');
    const inputs = row.querySelectorAll('input.ba-score');
    let total = 0;

    inputs.forEach((input) => {
        const maxInput = parseFloat(input.dataset.max) || 0;
        const inputValue = parseFloat(input.value) || 0;
        total += inputValue > maxInput ? maxInput : inputValue;
    });

    // Update total score
    row.querySelector('.total-score').innerText = total.toFixed(2);
}

function toggleRow(button) {
    const row = button.closest('tr');
    const inputs = row.querySelectorAll('input.ba-score');

    if (button.innerText === "Done") {
        // Disable inputs and change button text to "Edit"
        inputs.forEach((input) => input.setAttribute("disabled", "true"));
        button.innerText = "Edit";
    } else {
        // Enable inputs and change button text to "Done"
        inputs.forEach((input) => input.removeAttribute("disabled"));
        button.innerText = "Done";
    }
}

// Exam table ends





function showSection(sectionId) {
    // Hide all sections
    document.querySelectorAll('.section').forEach(section => {
        section.classList.remove('active');
    });

    // Remove active class from all navbar links
    document.querySelectorAll('.nav a').forEach(link => {
        link.classList.remove('active');
    });

    // Show the clicked section and add active class to the navbar link
    document.getElementById(sectionId).classList.add('active');
    document.querySelector(`.nav a[href="#${sectionId}"]`).classList.add('active');
}




function toggleCard(classId) {
    document.querySelectorAll('.student-list').forEach(div => div.style.display = 'none');
    document.getElementById(classId + '-students').style.display = 'block';
}

function toggleInput(section) {
    document.querySelectorAll('div[id$="-input"]').forEach(div => div.style.display = "none");
    document.getElementById(section + "-input").style.display = "block";
}


function showTable(className) {
    // Hide all tables
    const tables = document.querySelectorAll('.ca-table');
    tables.forEach(table => table.style.display = 'none');

    // Show the selected table
    const selectedTable = document.getElementById(`table-${className.toLowerCase()}`);
    if (selectedTable) {
        selectedTable.style.display = 'table';
        document.getElementById('submit-container').style.display = 'block';
    }
}


let currentTermIndex = 0; // Assuming terms are indexed as 0 = Term 1, 1 = Term 2, 2 = Term 3
const terms = ["First Term", "Second Term", "Third Term"]; // Example terms

function toggleTerm(direction) {
    // Update the current term index
    currentTermIndex += direction;

    // Ensure index stays within bounds
    if (currentTermIndex < 0) currentTermIndex = 0;
    if (currentTermIndex >= terms.length) currentTermIndex = terms.length - 1;

    // Display the current term
    alert(`Navigated to: ${terms[currentTermIndex]}`);

    // Update button visibility
    document.getElementById("prevTerm").style.display = currentTermIndex === 0 ? "none" : "inline-block";
    document.getElementById("nextTerm").style.display = currentTermIndex === terms.length - 1 ? "none" : "inline-block";
}

// Initialize the button states
window.onload = () => {
    toggleTerm(0); // Run initially to set up visibility
};





// function showExamTable(className) {
//     console.log(`Attempting to show exam table for class: ${className}`);

//     // Hide all exam tables first
//     document.querySelectorAll('.ba-exam-table').forEach((table) => {
//         table.style.display = 'none';
//     });

//     // Get the specific exam table
//     const selectedExamTable = document.getElementById(`exam-table-${className}`);
//     if (selectedExamTable) {
//         selectedExamTable.style.display = 'table';
//     } else {
//         console.error(`Exam table for class '${className}' not found.`);
//     }
// }


// function calculateExamTotal(input) {
//     const max = parseFloat(input.dataset.max) || 0;
//     let value = parseFloat(input.value) || 0;

//     // Limit the input value to the maximum allowed
//     if (value > max) {
//         alert(`The value cannot exceed ${max}.`);
//         input.value = max; // Reset to max
//         value = max;
//     }

//     const row = input.closest('tr');
//     const inputs = row.querySelectorAll('input.ba-score');
//     let total = 0;

//     inputs.forEach((input) => {
//         const maxInput = parseFloat(input.dataset.max) || 0;
//         const inputValue = parseFloat(input.value) || 0;
//         total += inputValue > maxInput ? maxInput : inputValue;
//     });

//     // Update total score
//     row.querySelector('.total-score').innerText = total.toFixed(2);
// }

// function toggleRow(button) {
//     const row = button.closest('tr');
//     const inputs = row.querySelectorAll('input.ba-score');

//     if (button.innerText === "Done") {
//         // Disable inputs and change button text to "Edit"
//         inputs.forEach((input) => input.setAttribute("disabled", "true"));
//         button.innerText = "Edit";
//     } else {
//         // Enable inputs and change button text to "Done"
//         inputs.forEach((input) => input.removeAttribute("disabled"));
//         button.innerText = "Done";
//     }
// }



// const socket = new WebSocket('ws://' + window.location.host + '/ws/test/');

// // Send test scores when the teacher submits them
// function submitTestScores(studentId, caScore) {
//     const data = {
//         'student_id': studentId,
//         'ca_score': caScore
//     };

//     // Send data to WebSocket server
//     socket.send(JSON.stringify(data));
// }

// // Handle WebSocket messages (receive updated scores)
// socket.onmessage = function (event) {
//     const data = JSON.parse(event.data);
//     const studentId = data['student_id'];
//     const caScore = data['ca_score'];

//     // Update the exam page with the test score
//     const row = document.getElementById(`student-row-${studentId}`);
//     if (row) {
//         const caColumn = row.querySelector('.ca-score');
//         caColumn.textContent = caScore; // Display the CA score in real-time
//     }
// };


// const socket = new WebSocket('ws://' + window.location.host + '/ws/test/');

// // Handle WebSocket messages (update the CA score on the exam page)
// socket.onmessage = function (event) {
//     const data = JSON.parse(event.data);
//     const studentId = data['student_id'];
//     const caScore = data['ca_score'];

//     // Update the row corresponding to the student with the test score (CA score)
//     const row = document.getElementById(`student-row-${studentId}`);
//     if (row) {
//         const caColumn = row.querySelector('.ca-score');
//         caColumn.textContent = caScore; // Update the displayed CA score
//     }
// };






