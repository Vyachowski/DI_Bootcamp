// In math.js, import the TodoList class from the todo.js module.
// Create an instance of the TodoList class.
import TodoList from "./todo.js";
// Add a few tasks, mark some as complete, and list all tasks.
const todoList = new TodoList();
// Run math.js and verify that the todo list operations are working correctly.
todoList.addTask('Buy a beaver');
todoList.addTask('Buy a chocolate');
todoList.addTask('Send a cv in google');
todoList.markTaskAsComplete('Buy a beaver');
todoList.markTaskAsComplete('Buy a chocolate');
todoList.markTaskAsComplete('Send a cv in google');
todoList.listAllTasks();
// ->
// [
//   { taskName: 'Buy a beaver', taskStatus: 'Done' },
//   { taskName: 'Buy a chocolate', taskStatus: 'Done' },
//   { taskName: 'Send a cv in google', taskStatus: 'Done' }
// ]