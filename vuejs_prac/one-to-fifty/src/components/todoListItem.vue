<template>
  <div>
    <li>
      <span 
      @click="updateTodo(todo)"
      :class="{ 'is-completed': todo.is_completed }"
      >Todo : {{ todo.title }}</span>
      <span>
        <button @click="deleteTodo(todo)">삭제</button>
      </span>
    </li>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object,
    }
  },
  methods: {
    ...mapActions(['deleteTodo', 'updateTodo'])
    // deleteTodo(){
    //   this.$store.dispatch('deleteTodo', this.todo)
    // },
  },
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>