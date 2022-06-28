<template>
  <div>
    <ul>
      <todo-list-item
      v-for="todo in todos"
      :key="todo.date"
      :todo="todo"
      ></todo-list-item>
    </ul>
  </div>
</template>

<script>
import TodoListItem from '@/components/todoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todos: function () {
      return this.$store.state.todos
    }
  }
}
</script>

<style>

</style>