<template>
  <div class="home">
    <div class="alert alert-light" role="alert" v-if="info != ''" style=" white-space:pre-wrap;">
      {{info}}
    </div>
    <div v-show="feats.length && info == ''" class="shell-classifier">
      <div class="row" >
        <div class="col-3" v-for="elem in features" :key="elem.id">
          <div class="name-feat">{{elem.name}}</div>
          <select v-if="elem.type != 0" class="form-select" v-model="elem.valueSelected" :style="elem.valueSelected != null ? 'border: 1px solid #CD40FF;' : ''"> 
            <option hidden disabled selected value="null" style="color:#A9A9A9;">Значение</option>
            <option v-for="el in elem.values" :key="el.id" :value="el">{{elem.type == 0 ? 'от ' + el.from + ' до ' +  el.to : el.value}}</option>
          </select>
          <input v-else type="number" v-model="elem.valueSelected" style="background-image: none;" :style="elem.valueSelected != '' ? 'border: 1px solid #CD40FF;' : ''" class="form-select" placeholder="Значение">
        </div>
        <div class="col-12" style="text-align: center;">
          <button class="btn btn-success-class" @click="clickCheckClass()">Определить класс</button>
        </div>
      </div>
    </div>

    <div class="modal-answer" v-if="modal">
      <div>Результат
        <button class="btn" @click="clickBtn()" style="float: right; margin: -10px;">
          <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect y="12.9336" width="18.2907" height="2.888" rx="1.444" transform="rotate(-45 0 12.9336)" fill="#CD40FF"/>
            <rect y="12.9336" width="18.2907" height="2.888" rx="1.444" transform="rotate(-45 0 12.9336)" fill="#B7B7B7"/>
            <rect x="2.04199" width="18.2907" height="2.888" rx="1.444" transform="rotate(45 2.04199 0)" fill="#CD40FF"/>
            <rect x="2.04199" width="18.2907" height="2.888" rx="1.444" transform="rotate(45 2.04199 0)" fill="#B7B7B7"/>
          </svg>
        </button>

      </div>
      <div v-if="!classAnswer.length">Класс не определен. Все классы в Базе Знаний были опровергнуты.</div>
      <button v-for="(elem, index) in classAnswer" :key="index" class="btn chips-res" disabled>{{elem}}</button>
      <div v-if="explaination.length">
        <a type="button" style="margin-top: 20px;" :style="isShowCollapse() ? 'color: #A9A9A9;' : 'color: #CD40FF;'" href="#collapseExample" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample" @click="clickButton()">{{isShowCollapse() ? 'Свернуть' : 'Объяснить'}}</a>
        <div class="collapse" id="collapseExample">
          Ниже представлен список опровергнутых классов и причина опровержения (признаки) <br/>
          <span v-for="(el, index) in explaination" :key="index"><b>{{el.class_name}}</b>: {{getLine(el.feature_list)}} <br/></span> 
          
        </div>
      </div>
    </div>
    <div class="back" v-if="modal"> </div>
  </div>
</template>

<script>
import {  mapState } from 'vuex'

export default {
  name: 'HomeView',
  data() {
    return {
      features: [],
      modal: false,
      check: true,
      classAnswer: [],
      explaination: [],
    }
  },
  computed:{
    ...mapState({
      allClasses:'classes',
      allFeatures:'features',
    }),
    feats(){
      this.initF()
      return this.allFeatures
    },
    info(){
      let str = ''
      let classInFeatures = []
      let checkA = false
      let checkB = false
      for (let elem of this.allClasses){
        let item = {class_name: elem.name, features: []}

        //if (elem.features.length) если класс есть, а признаков у него нету
        for (let feature of elem.features){
          if (feature.value.length == 0) {
            item.features.push(feature.name)
            checkA = true
          }
        }
        if (item.features.length) classInFeatures.push(item)
      }
      let arrayFeaturesNoValues = []
      for (let feature of this.allFeatures){
        if (feature.values.length == 0) {
          arrayFeaturesNoValues.push(feature.name)
          checkB = true
        }
      }
      if (!this.allClasses.length || !this.allFeatures.length) {
        str = "Данных нет! Нет"
        if (!this.allClasses.length) str += ' классов '
        if (!this.allClasses.length && !this.allFeatures.length) str += 'и'
        if (!this.allFeatures.length) str += ' признаков'
      }
      if (checkA || checkB) str += "Заполните базу знаний! "
      if (checkA) {
        str += "\nНет значений признаков для классов: "
        for (let item of classInFeatures){
          str += item.class_name + ` (а именно: ${item.features.join(", ")}), `
        }
        str += ':'
        str = str.replace(', :', '. ')
      }
      if (checkB){
        str += "\nНет возможных значений признаков: " + arrayFeaturesNoValues.join(", ") + '.'
      }
      return str
    }
  },
  mounted() {
    /*let checkA = false
    if (feature.values.length == 0) check = true
    if (check) this.info = "База знаний заполнена не до конца!"
        if (this.allClasses.length && this.allFeatures.length) this.info = "Данных нет!"*/
    if (this.allFeatures.length) this.check = false
    if (this.check)
      for (let elem of this.allFeatures){
        if (elem.type == 0) this.features.push(Object.assign({valueSelected: ''}, elem))
        else this.features.push(Object.assign({valueSelected: null}, elem))
      }

  },
  methods: {
    isShowCollapse(){
      let col = document.querySelector('#collapseExample')
      return col ? col.classList.value.includes('show') : false
    },
    initF(){
      for (let elem of this.allFeatures){
        if (elem.type == 0) this.features.push(Object.assign({valueSelected: ''}, elem))
        else this.features.push(Object.assign({valueSelected: null}, elem))
      }
    },
    clickBtn(){
      this.modal = false
      for (let elem of this.features){
        if (elem.type == 0) elem.valueSelected = ''
        else elem.valueSelected = null
      }
    },
    clickCheckClass(){
      let object = []
      for (let elem of this.features){
        if (elem.valueSelected){
          object.push({
            id: Number(elem.id),
            feature_name: elem.name,
            type: elem.type,
            value: elem.type == 0 ? Number(elem.valueSelected) : elem.valueSelected
          })
        }
      }
      console.log(object)
      this.$store.dispatch("CheckClass", {object}).then(res => {
        this.classAnswer = res.predicted_classes
        console.log("CheckClass", res, res.predicted_classes)
        this.explaination = res.explaination
        console.log(this.explaination)
        this.modal = true
      })
    },
    getLine(el){
      console.log(el)
      return el.join(", ")
    },
    clickButton(){
      let div = document.querySelector('#collapseExample')
      if (div.classList.value.includes('show')) div.classList.remove('show')
      else div.classList.add('show')
    }
  }
}
</script>

<style lang="scss">
  .home{
    padding: 70px;
    background: #EAEAEA;

    .shell-classifier{
      background: #FFFFFF;
      box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.05);
      border-radius: 6px;
      padding: 40px 100px;

      div{
        text-align: left;
      }

      .name-feat{
        font-style: normal;
        font-weight: 400;
        line-height: 20px;
        color: #000000;
        margin-bottom: 20px;
      }

      select, input{
        margin-bottom: 20px
      }
      input::placeholder{
        color: #000000;
      }
      option:active, option:focus, option:hover{
        background: rgba(205, 64, 255, 0.1) !important;
      }

      .btn-success-class{
        width: 202px;
        height: 42px;
        background: #CD40FF;
        border-radius: 6px;
        font-style: normal;
        font-weight: 400;
        color: white;
      }
    }

    .col-3 {
      margin-bottom: 15px;
    }

    .modal-answer{
      width: 600px;
      height: auto;
      position: fixed;
      z-index: 1000;
      left: calc(50% - 300px);
      top: calc(50% - 150px);
      background: #ffffff !important;
      border: 1px solid #d4d3d3;
      padding: 20px;
      border-radius: 30px;
      

      button{
        margin: 10px;
      }
    }
    .back{
      width: 100% !important;
      height: 100% !important;
      background-color: #00000054;
      position: fixed;
      left: 0;
      top: 0;
      z-index: 800;
    }
    #collapseExample{
      border: 1px solid #A9A9A9;
      margin: 15px;
      padding: 5px;
    }

    .chips-res{
      background: rgb(205 64 255) !important;
      border-radius: 6px !important;
      padding: 10px 25px;
      color: #FFFFFF !important;
      font-style: normal;
      font-weight: 400;
      font-size: 14px;
    }
  }
</style>