<template>
  <div>
    <h1>Todo Form</h1>
    <input type="text" @keyup.enter="inputTodo">
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  methods: {
    inputTodo(event){
      const todoTitle = event.target.value.trim()
      const todoItem = {
        title : todoTitle,
        is_completed : false,
        date : new Date().getTime(),
      }
      if (todoTitle){
        console.log(todoItem)
        this.$store.dispatch('createTodo', todoItem)
      }
      event.target.value=""
    }
  }
}
</script>

<style>

</style>