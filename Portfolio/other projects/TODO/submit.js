const taskInput = document.getElementById('taskInput');
const addTaskBtn = document.getElementById('addTaskBtn');
const taskList = document.getElementById('taskList');

function addTask() {
    const taskText = taskInput.value.trim();
    
    if (taskText !== "") {
        const li = document.createElement('li');
        li.textContent = taskText;

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = "X";
        deleteBtn.className = "delete-btn"; // Add a class for styling
        deleteBtn.onclick = function() {
            taskList.removeChild(li);
        };

        // Add the button to the list item
        li.appendChild(deleteBtn);

        taskList.appendChild(li);
        taskInput.value = '';

        // Completion toggle
        li.addEventListener('click', function() {
            li.classList.toggle('completed');
        });
    } else {
        window.alert('Walang utos');
    }
}

addTaskBtn.addEventListener('click', addTask);
taskInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        addTask();
    }
});
