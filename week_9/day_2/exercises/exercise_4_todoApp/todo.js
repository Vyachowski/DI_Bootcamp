// 🌟 Exercise 4: Todo List Using ES6 Module Syntax
// Instructions:
// Create a directory named todoApp.
// Inside the todoApp directory, create two files: todo.js and math.js.
// In todo.js, define an ES6 module that exports a TodoList class.
// The TodoList class should have methods to add tasks, mark tasks as complete, and list all tasks.
// Export the TodoList class
class TodoList{
  constructor(taskList = []) {
    this.taskList = taskList;
  }

  addTask(name) {
    this.taskList.push({'taskName': name, 'taskStatus': 'in progress'});
  }

  markTaskAsComplete(taskName) {
    const taskNames = this.taskList.map((task) => task.taskName);
    if (taskNames.includes(taskName)) {
      const indexOfTaskName = taskNames.indexOf(taskName);
      this.taskList[indexOfTaskName].taskStatus = 'Done';
      return true;
    }
    return false;
  }

  listAllTasks() {
    console.log(this.taskList);
  }
}

export default TodoList;