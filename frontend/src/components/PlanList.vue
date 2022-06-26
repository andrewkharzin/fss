
<template lang="pug">
  #app
    .card(v-for="plan in plans")
      .card-header
        button.btn.btn-clear.float-right(@click="deleteNote(note)")
        .card-title {{ plan.task_type }}
        .card-subtitle {{ note.task_status }}
        .card-body {{ note.task_addtime }}
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'plan-list',
  computed: mapGetters(['plans']),
  methods: {
    deleteNote (plan) {
      // Вызываем действие `deleteNote` из нашего хранилища, которое
      // попытается удалить заметку из нашех базы данных, отправив запрос к API
      this.$store.dispatch('deletePlan', plan)
    }
  },
  beforeMount () {
    // Перед тем как загрузить страницу, нам нужно получить список всех
    // имеющихся заметок. Для этого мы вызываем действие `getNotes` из
    // нашего хранилища
    this.$store.dispatch('getPlans')
  }
}
</script>
<style>
  header {
    margin-top: 50px;
  }
</style>
