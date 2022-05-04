import { createStore } from 'vuex'
import Service from '../services/index.services'

export default createStore({
  state: {
    classes: [],
    features: [],
  },
  getters: {
    
  },
  mutations: {
    update_classes(state, classes){
      state.classes = classes
    },
    update_features(state, features){
      state.features = features
    },
  },
  actions: {
    getAll({ commit } ){
      return Service.getAll().then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        })
    },
    updateClass({ commit }, item){
      return Service.updateClass(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    updateFeature({ commit }, item){
      return Service.updateFeature(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    updatePosValueFeature({ commit }, item){
      return Service.updatePosValueFeature(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    DeleteClass({ commit }, item){
      return Service.DeleteClass(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    DeleteFeature({ commit }, item){
      return Service.DeleteFeature(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    DeleteClassFeature({ commit }, item){
      return Service.DeleteClassFeature(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    DeletePosValueFeature({ commit }, item){
      return Service.DeletePosValueFeature(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    DeleteClassValueFeature({ commit }, item){
      return Service.DeleteClassValueFeature(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    CreateClass({ commit }, item){
      return Service.CreateClass(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    CreateFeature({ commit }, item){
      return Service.CreateFeature(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    CreateClassFeature({ commit }, item){
      return Service.CreateClassFeature(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    CreatePosValueFeature({ commit }, item){
      return Service.CreatePosValueFeature(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    CreateClassValueFeature({ commit }, item){
      return Service.CreateClassValueFeature(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    },
    CheckClass({ commit }, item){
      return Service.CheckClass(item).then(
        res => {
          return Promise.resolve(res)
        },
        err => {
          return Promise.reject(error)
        }
      )
    }
  },
  modules: {
  }
})
