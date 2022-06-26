import Vue from 'vue'
import Vuex from 'vuex'
import { Plan } from '../api/plans'
import {
  ADD_PLAN,
  REMOVE_PLAN,
  SET_PLAN
} from './mutation-types.js'
Vue.use(Vuex)
// Состояние
const state = {
  plans: [] // список заметок
}
// Геттеры
const getters = {
  plans: state => state.plans // получаем список заметок из состояния
}
// Мутации
const mutations = {
  // Добавляем заметку в список
  [ADD_PLAN] (state, plan) {
    state.plans = [plan, ...state.plans]
  },
  // Убираем заметку из списка
  [REMOVE_PLAN] (state, { id }) {
    state.plans = state.plans.filter(plan => {
      return plan.id !== id
    })
  },
  // Задаем список заметок
  [SET_PLAN] (state, { plans }) {
    state.plans = plans
  }
}
// Действия
const actions = {
  createPlan ({ commit }, planData) {
    Plan.create(planData).then(plan => {
      commit(ADD_PLAN, plan)
    })
  },
  deletePlan ({ commit }, plan) {
    Plan.delete(plan).then(response => {
      commit(REMOVE_PLAN, plan)
    })
  },
  getPlans ({ commit }) {
    Plan.list().then(plans => {
      commit(SET_PLAN, { plans })
    })
  }
}
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
