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



// Test Table

// Function to show the selected class table
function showTable(className) {
    // Hide all tables
    document.querySelectorAll('.ca-table').forEach((table) => table.style.display = 'none');

    // Show the selected class table
    const table = document.getElementById(`table-${className}`);
    if (table) {
        table.style.display = 'table';
        document.getElementById('submit-container').style.display = 'block';
    } else {
        alert(`Table for class '${className}' not found.`);
    }
}


// function toggleRow(button) {
//     const row = button.closest('tr');
//     const inputs = row.querySelectorAll('.ca-score');

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

// Function to toggle between Done and Edit mode
function toggleRowHandler(button) {
    // Locate the parent row
    const row = button.closest('tr');
    if (!row) {
        console.error('No parent row found for the button');
        return;
    }

    // Locate all inputs in the row with the 'ca-score' class
    const inputs = row.querySelectorAll('.ca-score');
    if (!inputs.length) {
        console.error('No input fields found in the row');
        return;
    }

    // Determine the current state (Done or Edit)
    const isDone = button.textContent.trim().toLowerCase() === 'done';

    // Toggle 'disabled' property for each input
    inputs.forEach((input) => {
        input.disabled = isDone;
    });

    // Update the button's text
    button.textContent = isDone ? 'Done' : 'Edit';
}

// Event listener for handling the toggle button click
document.addEventListener('click', (event) => {
    if (event.target.classList.contains('toggle-btn')) {
        toggleRowHandler(event.target); // Call the function with the button as the argument
    }
});

// Function to calculate the total score in a row
function calculateTotal(input) {
    const row = input.closest('tr');
    const scores = row.querySelectorAll('.ca-score');
    let total = 0;

    scores.forEach((score) => {
        const max = parseInt(score.dataset.max) || 0;
        let value = parseInt(score.value) || 0;

        if (isNaN(value) || value < 0) {
            alert('Please enter a valid score.');
            score.value = '';
            value = 0;
        }

        if (value > max) {
            alert(`Score cannot exceed ${max}!`);
            score.value = max;
            value = max;
        }
        total += value;
    });

    if (total > 40) {
        alert('Total cannot exceed 40!');
        total = 40;
    }

    const totalCell = row.querySelector('.total-score');
    totalCell.textContent = total;
}

// Function to calculate the total score in a row
function calculateTotal(input) {
    const row = input.closest('tr');
    const scores = row.querySelectorAll('.ca-score');
    let total = 0;

    scores.forEach((score) => {
        const max = parseInt(score.dataset.max) || 0;
        let value = parseInt(score.value) || 0;

        if (isNaN(value) || value < 0) {
            alert('Please enter a valid score.');
            score.value = '';
            value = 0;
        }

        if (value > max) {
            alert(`Score cannot exceed ${max}!`);
            score.value = max;
            value = max;
        }
        total += value;
    });

    if (total > 40) {
        alert('Total cannot exceed 40!');
        total = 40;
    }

    const totalCell = row.querySelector('.total-score');
    totalCell.textContent = total;
}

// Function to calculate total scores from the test page
function calculateTestTotal(input) {
    const row = input.closest('tr');
    const inputs = row.querySelectorAll('input.ca-score');
    let total = 0;

    inputs.forEach((input) => {
        const max = parseInt(input.dataset.max) || 0;
        let value = parseInt(input.value) || 0;

        if (isNaN(value) || value < 0) {
            alert('Please enter a valid score.');
            input.value = '';
            value = 0;
        }

        if (value > max) {
            alert(`The value cannot exceed ${max}.`);
            input.value = max;
            value = max;
        }
        total += value;
    });

    // Update total score
    const totalCell = row.querySelector('.total-score');
    totalCell.textContent = Math.min(total, 40);
}

// Function to submit test scores to the exam table
function submitTestScores() {
    const testScores = {};

    // Collect test scores
    document.querySelectorAll('.ca-table tbody tr').forEach((row) => {
        const studentName = row.querySelector('td:first-child').textContent.trim();
        const totalScore = parseFloat(row.querySelector('.total-score').textContent) || 0;
        if (totalScore > 0) {
            testScores[studentName] = totalScore;
        }
    });

    if (Object.keys(testScores).length === 0) {
        alert('No scores to submit.');
        return;
    }

    // Update the exam table
    document.querySelectorAll('.ba-exam-table tbody tr').forEach((row) => {
        const studentName = row.querySelector('td:first-child').textContent.trim();
        if (testScores.hasOwnProperty(studentName)) {
            const examInput = row.querySelector('input[data-max="40"]');
            if (examInput) {
                examInput.value = testScores[studentName];
                examInput.setAttribute('readonly', 'true'); // Lock input
            }
        }
    });

    alert('Test scores submitted successfully!');
}

// Event listeners for dynamic content
document.addEventListener('DOMContentLoaded', () => {
    document.addEventListener('input', (event) => {
        if (event.target.classList.contains('ca-score')) {
            calculateTotal(event.target);
        }
    });

    document.addEventListener('click', (event) => {
        if (event.target.classList.contains('toggle-btn')) {
            toggleRow(event.target);
        }
    });

    const submitButton = document.getElementById('submit-scores');
    if (submitButton) {
        submitButton.addEventListener('click', submitTestScores);
    }
});





// let currentTermIndex = 0; // Assuming terms are indexed as 0 = Term 1, 1 = Term 2, 2 = Term 3
// const terms = ["First Term", "Second Term", "Third Term"]; // Example terms

// function toggleTerm(direction) {
//     // Update the current term index
//     currentTermIndex += direction;

//     // Ensure index stays within bounds
//     if (currentTermIndex < 0) currentTermIndex = 0;
//     if (currentTermIndex >= terms.length) currentTermIndex = terms.length - 1;

//     // Display the current term
//     alert(`Navigated to: ${terms[currentTermIndex]}`);

//     // Update button visibility
//     document.getElementById("prevTerm").style.display = currentTermIndex === 0 ? "none" : "inline-block";
//     document.getElementById("nextTerm").style.display = currentTermIndex === terms.length - 1 ? "none" : "inline-block";
// }

// // Initialize the button states
// window.onload = () => {
//     toggleTerm(0); // Run initially to set up visibility
// };



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
        document.getElementById('submit-btn').style.display = 'block';
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

// // Function to show the next term's section
// function showNextTerm(currentButtonId, nextSectionId) {
//     document.getElementById(currentButtonId).addEventListener("click", function () {
//         document.getElementById(nextSectionId).classList.add("active");
//         this.style.display = "none"; // Hide current button
//     });
// }

// // Setup buttons for each term
// showNextTerm("submit-term1", "term2-section");
// showNextTerm("submit-term2", "term3-section");



// Attendance and test scores //

// document.addEventListener('DOMContentLoaded', () => {
//     fetch('/api/get-data?class_name=JSS1')
//         .then(response => response.json())
//         .then(data => {
//             populateAttendance(data.attendance);
//             populateTestScores(data.test_scores);
//         });
// });

// function populateAttendance(attendance) {
//     attendance.forEach(record => {
//         const row = document.querySelector(`#attendance-row-${record.student_id}`);
//         if (row) {
//             row.querySelector('.status').textContent = record.status;
//         }
//     });
// }

// function populateTestScores(scores) {
//     scores.forEach(score => {
//         const row = document.querySelector(`#score-row-${score.student_id}`);
//         if (row) {
//             row.querySelector('.test-score').value = score.test_score;
//             row.querySelector('.exam-score').value = score.exam_score;
//         }
//     });
// }
// // Save Data  for Atten and Test //

// function saveData() {
//     const attendance = [];
//     document.querySelectorAll('.attendance-row').forEach(row => {
//         attendance.push({
//             student_id: row.dataset.studentId,
//             status: row.querySelector('.status').textContent
//         });
//     });

//     const scores = [];
//     document.querySelectorAll('.score-row').forEach(row => {
//         scores.push({
//             student_id: row.dataset.studentId,
//             test_score: row.querySelector('.test-score').value,
//             exam_score: row.querySelector('.exam-score').value
//         });
//     });

//     fetch('/api/save-data', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ attendance, scores })
//     }).then(response => response.json())
//         .then(data => {
//             if (data.success) alert('Data saved successfully!');
//         });
// }


// Attendance Js //

document.addEventListener('DOMContentLoaded', function () {
    loadAttendance();

    // Add event listener to all checkboxes
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', debounce(saveAttendance, 200));
    });

    document.getElementById('save-attendance').addEventListener('click', function () {
        submitAttendance();
        alert('Attendance saved successfully!');
    });
});

function saveAttendance() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const attendanceData = [];

    checkboxes.forEach(checkbox => {
        attendanceData.push({
            student_id: checkbox.dataset.student,
            week: checkbox.dataset.week,
            term: checkbox.dataset.term,
            present: checkbox.checked
        });
    });

    // Save the attendance data to localStorage
    localStorage.setItem('attendanceData', JSON.stringify(attendanceData));
    console.log("Attendance data saved to localStorage:", attendanceData); // Debugging line
}

function loadAttendance() {
    const attendanceData = JSON.parse(localStorage.getItem('attendanceData')) || [];
    console.log("Loaded attendance data from localStorage:", attendanceData); // Debugging line

    attendanceData.forEach(item => {
        const checkbox = document.querySelector(`input[data-student="${item.student_id}"][data-week="${item.week}"][data-term="${item.term}"]`);
        if (checkbox) {
            checkbox.checked = item.present;
            // Force a re-render by creating a new element and replacing the old one
            const newCheckbox = checkbox.cloneNode(true);
            checkbox.parentNode.replaceChild(newCheckbox, checkbox);
            console.log(`Checkbox found and updated: student_id=${item.student_id}, week=${item.week}, term=${item.term}, present=${item.present}`); // Debugging line
        } else {
            console.warn(`Checkbox not found: student_id=${item.student_id}, week=${item.week}, term=${item.term}`); // Debugging line
        }
    });
}

function submitAttendance() {
    // Simply call saveAttendance to ensure data is saved when the button is clicked
    saveAttendance();
}

// Debounce function to limit how often a function can be executed
function debounce(func, delay) {
    let timeoutId;
    return function (...args) {
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        timeoutId = setTimeout(() => {
            func.apply(this, args);
        }, delay);
    };
}
