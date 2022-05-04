<template>
  <div class="editor">
    <!--<h1>This is an editor page</h1>-->
    <div class="row">
        <div class="col-auto">
          <div class=" card-edit wh">
            <div class="card-title">
              Классы
            </div>
            <div class="card-body">
              <div  class="div-card">
                <div v-for="el in allClasses" :key="el.id" class="row input-elem">
                  <input class="col-10" type="text" v-model="el.name" @change="changeClassName(el);upgradeClassInFeature()">
                  <button class="btn btn-delete col-2" @click="deleteClass(el.id);upgradeClassInFeature()">
                    <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <rect x="0.225342" y="13.2737" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(-45 0.225342 13.2737)" fill="#CD40FF"/>
                      <rect x="0.225342" y="13.2737" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(-45 0.225342 13.2737)" fill="#B7B7B7"/>
                      <rect x="2.26941" y="0.327881" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(45 2.26941 0.327881)" fill="#CD40FF"/>
                      <rect x="2.26941" y="0.327881" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(45 2.26941 0.327881)" fill="#B7B7B7"/>
                    </svg>
                  </button>
                </div>
              </div>
              <div class="row input-elem-new" style="margin-top: 10px;">
                <input class="col-10" type="text" v-model="newClassName" placeholder="Наименование класса">
                <button class="btn btn-add col-2" @click="addClass();upgradeClassInFeature()">
                  <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect x="2.33179" y="9.42773" width="17.8131" height="2.8126" rx="1.4063" fill="#CD40FF"/>
                    <rect x="2.33179" y="9.42773" width="17.8131" height="2.8126" rx="1.4063" fill="white"/>
                    <rect x="12.6448" y="1.92749" width="17.8131" height="2.8126" rx="1.4063" transform="rotate(90 12.6448 1.92749)" fill="#CD40FF"/>
                    <rect x="12.6448" y="1.92749" width="17.8131" height="2.8126" rx="1.4063" transform="rotate(90 12.6448 1.92749)" fill="white"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="col-auto">
          <div class=" card-edit wh">
            <div class="card-title">
              Признаки
            </div>
            <div class="card-body">
              <div  class="div-card">
                <div v-for="el in allFeatures" :key="el.id" class="row input-elem">
                  <input class="col-10" type="text" v-model="el.name" @change="changeFeatureName(el);upgradeClassInFeature()">
                  <button class="btn btn-delete col-2" @click="deleteFeature(el.id);upgradeClassInFeature()">
                    <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <rect x="0.225342" y="13.2737" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(-45 0.225342 13.2737)" fill="#CD40FF"/>
                      <rect x="0.225342" y="13.2737" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(-45 0.225342 13.2737)" fill="#B7B7B7"/>
                      <rect x="2.26941" y="0.327881" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(45 2.26941 0.327881)" fill="#CD40FF"/>
                      <rect x="2.26941" y="0.327881" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(45 2.26941 0.327881)" fill="#B7B7B7"/>
                    </svg>
                  </button>
                </div>
              </div>
              <div class="row input-elem-new" style="margin-top: 10px;">
                <input class="col-10" type="text" v-model="newFeatureName" placeholder="Наименование признака">
                <button class="btn btn-add col-2" @click="addFeature();upgradeClassInFeature()">
                  <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect x="2.33179" y="9.42773" width="17.8131" height="2.8126" rx="1.4063" fill="#CD40FF"/>
                    <rect x="2.33179" y="9.42773" width="17.8131" height="2.8126" rx="1.4063" fill="white"/>
                    <rect x="12.6448" y="1.92749" width="17.8131" height="2.8126" rx="1.4063" transform="rotate(90 12.6448 1.92749)" fill="#CD40FF"/>
                    <rect x="12.6448" y="1.92749" width="17.8131" height="2.8126" rx="1.4063" transform="rotate(90 12.6448 1.92749)" fill="white"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="col-auto">
          <div class="card-edit" style="width:576px;">
            <div class="card-title">
              Возможные значения признаков
            </div>
            <div class="card-body">
              <div class="row">
                <div class="col-6" style="border-right: 1px solid #EAEAEA;">
                  <div class="div-span">Выберите признак</div>
                  <select v-if="allFeatures.length" class="form-select" v-model="selectedFeature" @change="newTypeFeature = selectedFeature.type; newValues = selectedFeature.type == 0 ? {} : ''" style="margin-bottom: 18px;" >
                    <option :value="null" disabled selected hidden>Признак</option>
                    <option v-for="el in allFeatures" :key="el.id" :value="el">{{el.name}}</option>
                  </select>
                  <div v-else style="background-image: none;margin-bottom: 18px;" class="form-select">Признаков нет</div>

                  <!--<select class="form-select" v-model="newTypeFeature" @change="changeTypeFeature();upgradeClassInFeature()">
                      <option v-for="el in types" :key="el.name" :value="el.value">{{el.name}}</option>
                    </select>-->

                  <div v-if="selectedFeature" style="margin-top: 10px;">
                    <div class="div-span">Выберите тип признака</div>
                    <div v-for="el of types" :key="el.name" style="text-align: left;">
                      <input type="radio" :id="el.name" :value="el.value" :checked="newTypeFeature == el.value" @click="newTypeFeature = el.value; changeTypeFeature();upgradeClassInFeature()">
                      <label :for="el.name" style="color: #000000; margin-left: 10px;">{{el.name}}</label>
                    </div>

                    <div v-if="selectedFeature.type == 0" style="padding: 1rem 1rem; margin-top: 75px;" class="wh">
                      <div class="row">
                        <div class="row input-elem-interval-new col-12" style="align-items: center;">
                          от 
                          <input class="interval" type="number" v-model="newValues.from">
                          до
                          <input class="interval" type="number" v-model="newValues.to">
                          <button class="btn btn-add col-2" @click="addFeatureValues();upgradeClassInFeature()">
                            <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <rect x="2.33179" y="9.42773" width="17.8131" height="2.8126" rx="1.4063" fill="#CD40FF"/>
                              <rect x="2.33179" y="9.42773" width="17.8131" height="2.8126" rx="1.4063" fill="white"/>
                              <rect x="12.6448" y="1.92749" width="17.8131" height="2.8126" rx="1.4063" transform="rotate(90 12.6448 1.92749)" fill="#CD40FF"/>
                              <rect x="12.6448" y="1.92749" width="17.8131" height="2.8126" rx="1.4063" transform="rotate(90 12.6448 1.92749)" fill="white"/>
                            </svg>
                          </button>
                        </div>
                      </div>
                    </div>

                    <div v-if="selectedFeature.type == 1" style="padding: 1rem 1rem;margin-top: 75px;">
                      <div class="row input-elem-new">
                        <input class="col-auto" type="number" v-model="newValues" placeholder="Введите значение">
                        <button class="btn btn-add col-auto" @click="addFeatureValues();upgradeClassInFeature()">
                          <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="2.33179" y="9.42773" width="17.8131" height="2.8126" rx="1.4063" fill="#CD40FF"/>
                            <rect x="2.33179" y="9.42773" width="17.8131" height="2.8126" rx="1.4063" fill="white"/>
                            <rect x="12.6448" y="1.92749" width="17.8131" height="2.8126" rx="1.4063" transform="rotate(90 12.6448 1.92749)" fill="#CD40FF"/>
                            <rect x="12.6448" y="1.92749" width="17.8131" height="2.8126" rx="1.4063" transform="rotate(90 12.6448 1.92749)" fill="white"/>
                          </svg>
                        </button>
                      </div>
                    </div>

                    <div v-if="selectedFeature.type == 2" style="padding: 1rem 1rem;margin-top: 75px;">
                      <div class="row input-elem-new">
                        <input class="col-auto" type="text" v-model="newValues" placeholder="Введите значение">
                        <button class="btn btn-add col-auto" @click="addFeatureValues();upgradeClassInFeature()">
                          <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="2.33179" y="9.42773" width="17.8131" height="2.8126" rx="1.4063" fill="#CD40FF"/>
                            <rect x="2.33179" y="9.42773" width="17.8131" height="2.8126" rx="1.4063" fill="white"/>
                            <rect x="12.6448" y="1.92749" width="17.8131" height="2.8126" rx="1.4063" transform="rotate(90 12.6448 1.92749)" fill="#CD40FF"/>
                            <rect x="12.6448" y="1.92749" width="17.8131" height="2.8126" rx="1.4063" transform="rotate(90 12.6448 1.92749)" fill="white"/>
                          </svg>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-6" style="height: 330px; padding: 17px;">
                  <div v-if="selectedFeature" class="div-card" style="padding: 0;max-height: 270px;">
                    <div v-if="selectedFeature.type == 0" class="wh">
                      <div class="row">
                        <div v-for="(el, index) in selectedFeature.values" :key="index" class="row col-12 input-elem-interval" style="align-items: center;">
                          от 
                          <input class="interval" type="number" v-model="el.from" @change="changeFeatureValues(el);upgradeClassInFeature()">
                          до
                          <input class="interval" type="number" v-model="el.to" @change="changeFeatureValues(el);upgradeClassInFeature()">
                          <button class="btn btn-delete col-2" @click="deleteFeatureValues(el);upgradeClassInFeature()">
                            <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <rect x="0.225342" y="13.2737" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(-45 0.225342 13.2737)" fill="#CD40FF"/>
                              <rect x="0.225342" y="13.2737" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(-45 0.225342 13.2737)" fill="#B7B7B7"/>
                              <rect x="2.26941" y="0.327881" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(45 2.26941 0.327881)" fill="#CD40FF"/>
                              <rect x="2.26941" y="0.327881" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(45 2.26941 0.327881)" fill="#B7B7B7"/>
                            </svg>
                          </button>
                        </div>
                      </div>
                    </div>

                    <div v-if="selectedFeature.type == 1">
                      <div class="row">
                        <div v-for="(el, index) in selectedFeature.values" :key="index" class="row input-elem">
                          <input class="col-auto" type="number" v-model="el.value" @change="changeFeatureValues(el);upgradeClassInFeature()">
                          <button class="btn btn-delete col-auto" @click="deleteFeatureValues(el);upgradeClassInFeature()">
                            <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect x="0.225342" y="13.2737" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(-45 0.225342 13.2737)" fill="#CD40FF"/>
                            <rect x="0.225342" y="13.2737" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(-45 0.225342 13.2737)" fill="#B7B7B7"/>
                            <rect x="2.26941" y="0.327881" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(45 2.26941 0.327881)" fill="#CD40FF"/>
                            <rect x="2.26941" y="0.327881" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(45 2.26941 0.327881)" fill="#B7B7B7"/>
                          </svg>
                          </button>
                        </div>
                      </div>
                    </div>

                    <div v-if="selectedFeature.type == 2">
                      <div class="row">
                        <div v-for="(el, index) in selectedFeature.values" :key="index" class="row input-elem">
                          <input class="col-auto" type="text" v-model="el.value" @change="changeFeatureValues(el);upgradeClassInFeature()">
                          <button class="btn btn-delete col-auto" @click="deleteFeatureValues(el);upgradeClassInFeature()">
                            <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <rect x="0.225342" y="13.2737" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(-45 0.225342 13.2737)" fill="#CD40FF"/>
                              <rect x="0.225342" y="13.2737" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(-45 0.225342 13.2737)" fill="#B7B7B7"/>
                              <rect x="2.26941" y="0.327881" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(45 2.26941 0.327881)" fill="#CD40FF"/>
                              <rect x="2.26941" y="0.327881" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(45 2.26941 0.327881)" fill="#B7B7B7"/>
                            </svg>
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                </div>
              </div>
          </div>
        </div>

        <div class="col-auto">
          <div class=" card-edit wh">
            <div class="card-title">
              Признаки для класса
            </div>
            <div class="card-body">
              <select v-if="allClasses.length" class="form-select" v-model="selectedClass" @change="selectedFeatureInClass = null; newFeatureInClass = null; updateFeatureInClass()" :style="selectedClass != null ? 'border: 1px solid #CD40FF;' : ''" style="margin-bottom: 10px;">
                <option :value="null" disabled selected hidden>Выберите класс</option>
                <option v-for="el in allClasses" :key="el.id" :value="el">{{el.name}}</option>
              </select>
              <div v-else style="background-image: none;margin-bottom: 10px;" class="form-select">Классов нет</div>

              <div class="div-card" style="max-height: 245px;">
                <div v-for="el in allFeatures" :key="el.id" class="row input-elem">
                  <input class="col-10" type="text" v-model="el.name" disabled>

                  <button v-if="!isFeatureInClass(el)" class="btn btn-add col-2" @click="newFeatureInClass = el; addFeatureClass()" :disabled="selectedClass==null">
                    <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <rect x="2.33179" y="9.42773" width="17.8131" height="2.8126" rx="1.4063" fill="#CD40FF"/>
                      <rect x="2.33179" y="9.42773" width="17.8131" height="2.8126" rx="1.4063" fill="white"/>
                      <rect x="12.6448" y="1.92749" width="17.8131" height="2.8126" rx="1.4063" transform="rotate(90 12.6448 1.92749)" fill="#CD40FF"/>
                      <rect x="12.6448" y="1.92749" width="17.8131" height="2.8126" rx="1.4063" transform="rotate(90 12.6448 1.92749)" fill="white"/>
                    </svg>
                  </button>
                  <button v-else class="btn btn-delete col-2" @click="deleteFeatureInClass(el.id)" :disabled="selectedClass==null">
                    <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <rect x="0.225342" y="13.2737" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(-45 0.225342 13.2737)" fill="#CD40FF"/>
                      <rect x="0.225342" y="13.2737" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(-45 0.225342 13.2737)" fill="#B7B7B7"/>
                      <rect x="2.26941" y="0.327881" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(45 2.26941 0.327881)" fill="#CD40FF"/>
                      <rect x="2.26941" y="0.327881" width="18.3079" height="2.89073" rx="1.44536" transform="rotate(45 2.26941 0.327881)" fill="#B7B7B7"/>
                    </svg>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-auto">
          <div class=" card-union">
            <div class="card-title">
              Значения признаков для класса
            </div>
            <div class="card-body row">
              <div class="col-4" style="border-right: 1px solid #EAEAEA;">
                <div class="div-span">Выберите класс</div>
                <select v-if="allClasses.length" class="form-select" v-model="selectedClass" @change="selectedFeatureInClass = null; newFeatureInClass = null; updateFeatureInClass()"  :style="selectedClass != null ? 'border: 1px solid #CD40FF;' : ''" style="margin-bottom: 20px;">
                  <option :value="null" disabled selected hidden>Класс</option>
                  <option v-for="el in allClasses" :key="el.id" :value="el">{{el.name}}</option>
                </select>
                <div v-else style="background-image: none;margin-bottom: 20px;" class="form-select">Классов нет</div>

                <div v-if="selectedClass">
                  <div class="div-span">Выберите признак</div>
                  <div class="row input-elem" v-if="selectedClass.features.length">
                    <div class="col">
                      <select class="form-select" v-model="selectedFeatureInClass"  :style="selectedFeatureInClass != null ? 'border: 1px solid #CD40FF;' : ''">
                        <option :value="null" disabled selected hidden>Признак</option>
                        <option v-for="el in selectedClass.features" :key="el.id" :value="el">{{el.name}}</option>
                      </select>
                    </div>
                  </div>
                  <div v-else class="row input-elem" style="padding-left: 25px; padding-right: 15px;"><div style="background-image: none;" class="form-select">У класса нет выбранных признаков</div></div>
                </div>
              </div>
              <div class="col-8">
                <div v-if="selectedFeatureInClass">
                  <button class="btn chips" :class="checkValueFeatureInClass(item) ? 'active' :''" v-for="item in selectedFeatureInClass.values" :key="item.id" @click="clickChipsValue(item)">
                    {{selectedFeatureInClass.type == 0 ? 'от ' + item.from + ' до ' +  item.to : item.value}}
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

    </div>
  </div>
</template>

<script>
  import {  mapState } from 'vuex'

  export default {
    name: 'EditorView',
    data() {
      return {
        newClassName: '',
        newFeatureName: '',
        newTypeFeature: '',
        newValues: {},
        selectedFeature: null,
        selectedClass: null, 
        newFeatureInClass: null,
        selectedFeatureInClass: null,
        types: [{name: 'Интервал', value: 0}, {name: 'Числовое', value: 1}, {name: 'Строковое', value: 2}],

        help: ''
      }
    },
    computed: {
      ...mapState({
        allClasses:'classes',
        allFeatures:'features',
      }),
      getFeaturesSelectedClass(){
        let features = []
        for (let elem of this.allFeatures){
          if (!this.selectedClass.features.find(el => el.id == elem.id)){
            features.push(elem)
          }
        }
        return features
      },
    },
    mounted() {
      this.copy
    },
    methods: {
      isFeatureInClass(el){
        return this.selectedClass ? this.selectedClass.features.find(elem => elem.id == el.id) : false
      },
      changeClassName(el){
        el.name = el.name.trim()
        if (el.name != '' && !this.$store.state.classes.find(elem => elem.name == el.name && el.id != elem.id)){
          this.$store.dispatch("updateClass", {class_id: el.id, class_name: el.name}).then(res => {
            if (!res.success) {alert("Не сохранено"); this.updateAll()}
          })
        } else {alert("Не сохранено"); this.updateAll()}
      },
      addClass(){
        this.newClassName = this.newClassName.trim()
        if (this.newClassName != ''){
          if (this.$store.state.classes.find(el => el.name == this.newClassName)) alert('Класс с таким именем уже существует!')
          else{
            this.$store.dispatch("CreateClass", {class_name: this.newClassName}).then(res => {
              if (res.success) { 
                this.$store.state.classes.push({id: res.value.id, name: this.newClassName, features: []})
                this.newClassName = ''
              }
              else alert("Не сохранено")
            })
          }
        } else alert('Введите имя класса')
      },
      deleteClass(id){
        this.$store.dispatch("DeleteClass", {class_id: id}).then(res => {
          if (res.success) {
            let elem = this.allClasses.find(el => el.id == id)
            let ind = this.allClasses.indexOf(elem)
            this.$store.state.classes.splice(ind, 1)

            if (this.selectedClass && this.selectedClass.id == id){
              this.selectedClass = null
              this.selectedFeatureInClass = null
            }
          }
          else alert("Не удалено")
        }) 
      },
      changeFeatureName(el){
        el.name = el.name.trim()
        if (el.name != '' && !this.$store.state.features.find(elem => elem.name == el.name && elem.id != el.id)){
          this.$store.dispatch("updateFeature", {feature_id: el.id, feature_name: el.name, type: el.type}).then(res => {
            if (!res.success){alert("Не сохранено");this.updateAll()}
          })
        } else {alert("Не сохранено"); this.updateAll()}
      },
      addFeature(){
        this.newFeatureName = this.newFeatureName.trim()
        if (this.newFeatureName != ''){
          if (this.$store.state.features.find(el => el.name == this.newFeatureName)) alert('Признак с таким именем уже существует!')
          else{
            this.$store.dispatch("CreateFeature", {feature_name: this.newFeatureName, type: 0}).then(res => {
              if (res.success) { 
                this.$store.state.features.push({id: res.value.id, name: this.newFeatureName, values: [] , type: res.value.type})
                this.newFeatureName = ''
              }
              else alert("Не сохранено")
            })
          }
        } else alert('Введите имя признака')
      },
      deleteFeature(id){
        this.$store.dispatch("DeleteFeature", {feature_id: id}).then(res => {
          if (res.success) {
            let elem = this.allFeatures.find(el => el.id == id)
            let ind = this.allFeatures.indexOf(elem)
            this.$store.state.features.splice(ind, 1)

            if (this.selectedFeature && this.selectedFeature.id == id) this.selectedFeature = null
            if (this.newFeatureInClass && this.newFeatureInClass.id == id) this.newFeatureInClass = null
            if (this.selectedFeatureInClass && this.selectedFeatureInClass.id == id) this.selectedFeatureInClass = null

            for (let elem of this.allClasses){
              let el = elem.features.find(item => item.id == id)
              let ind = el ? elem.features.indexOf(el) : -1
              if (ind != -1) elem.features.splice(ind, 1)
            }
          }
          else alert("Не удалено")
        })
      },
      /*clickTypeFeature(value){
        let type = this.selectedFeature.type
        for (let el of this.selectedFeature.values){
          this.deleteFeatureValues(el, type)
        }
        this.$store.dispatch("updateFeature", {feature_id: this.selectedFeature.id, feature_name: this.selectedFeature.name, type: this.selectedFeature.type})
        this.selectedFeature.type = value
      },*/
      deleteFeatureValues(el, type){
        this.$store.dispatch("DeletePosValueFeature", {value_id: el.id, type: type ? type : this.selectedFeature.type}).then(res => { 
          if (res.success) {
            this.selectedFeature.values.splice(this.selectedFeature.values.indexOf(el), 1)
          }
          else alert("Не удалено")
        })
      },
      addFeatureValues(){
        let item = {}
        if (this.selectedFeature.type == 0){
          item = {
            type : this.selectedFeature.type,
            feature_id: this.selectedFeature.id,
            from: this.newValues.from,
            to: this.newValues.to
          }

          if (item.from > item.to || this.selectedFeature.values.find(el => el.from == item.from && el.to == item.to)){
            this.newValues = {}
            alert("Данные не сохранены, так как значения указаны не верно")
            return
          }
        } else {
          if (typeof(this.newValues) == "string") this.newValues = this.newValues.trim()
          item = {
            type : this.selectedFeature.type,
            feature_id: this.selectedFeature.id,
            value: this.newValues
          }
          console.log(typeof(this.newValues), typeof(this.newValues) == "string", typeof(this.newValues) == "string" && this.newValues == '')
          if (typeof(this.newValues) == "string" && this.newValues == '' || this.selectedFeature.values.find(el => el.value == this.newValues)){
            this.newValues = ''
            alert("Данные не сохранены, так как значение указано не верно")
            return
          }
        }
        this.$store.dispatch("CreatePosValueFeature", item).then(res => { 
          if (res.success) {
            item = {
              ...item, 
              id: res.value.id
            }
            this.selectedFeature.values.push(item)
            if (this.selectedFeature.type != 0) this.newValues = ''
            else this.newValues = {}
          }
          else alert("Не добавлено")
        })
      },
      changeFeatureValues(elem){
        let item = {}
        if (this.selectedFeature.type == 0){
          item = {
            type : this.selectedFeature.type,
            value_id: elem.id,
            from: elem.from,
            to: elem.to
          }

          if (item.from > item.to || this.selectedFeature.values.find(el => el.from == item.from && el.to == item.to)){
            alert("Данные не сохранены, так как интервал указан не верно")
            this.selectedFeature = null
            this.updateAll()
            return
          }
        } else {
          if (typeof(elem.value) == "string") elem.value = elem.value.trim()
          item = {
            type : this.selectedFeature.type,
            value_id: elem.id,
            value: elem.value
          }
          if (typeof(elem.value) == "string" && elem.value == '' || this.selectedFeature.values.find(el => el.value == elem.value && el.id != elem.id)){
            alert("Данные не сохранены, так как значение указано не верно")
            this.selectedFeature = null
            this.updateAll()
            return
          }
        }
        
        this.$store.dispatch("updatePosValueFeature", item).then(res => { 
          if (!res.success)  {alert("Не сохранено");this.updateAll()}
        })
      },
      changeTypeFeature(){
        for (let el of this.selectedFeature.values){
          this.deleteFeatureValues(el, this.selectedFeature.type)
        }
        this.$store.dispatch("updateFeature", {feature_id: this.selectedFeature.id, feature_name: this.selectedFeature.name, type: this.newTypeFeature})
        this.selectedFeature.type = this.newTypeFeature 
        this.selectedFeature.values = []
        if (this.newTypeFeature != 0) this.newValues = ''
        else this.newValues = {}
      },
      deleteFeatureInClass(id){
        this.$store.dispatch("DeleteClassFeature", {class_id: this.selectedClass.id, feature_id: id}).then(res => { 
          if (res.success) {
            let elem = this.selectedClass.features.find(el => el.id == id)
            let ind = this.selectedClass.features.indexOf(elem)
            this.selectedClass.features.splice(ind, 1)
            this.selectedFeatureInClass = null
          }
          else alert("Не удалено")
        })
      },
      addFeatureClass(){
        this.$store.dispatch("CreateClassFeature", {class_id: this.selectedClass.id, feature_id: this.newFeatureInClass.id}).then(res => { 
          if (res.success) {
            this.newFeatureInClass.value = []
            this.selectedClass.features.push(this.newFeatureInClass)
          }
          else alert("Не добавлено")
        })
      },
      checkValueFeatureInClass(val){
        return this.selectedFeatureInClass.value.find(el => el.id == val.id)
      },
      clickChipsValue(val){
        console.log({class_id: this.selectedClass.id, value_id: val.id, type: this.selectedFeatureInClass.type})
        let feat = this.selectedFeatureInClass.value.find(el => el.id == val.id)
        if (feat){
          this.$store.dispatch("DeleteClassValueFeature", {class_id: this.selectedClass.id, value_id: val.id, type: this.selectedFeatureInClass.type}).then(res => { 
            if (res.success) {
              let ind = this.selectedFeatureInClass.value.indexOf(feat)
              this.selectedFeatureInClass.value.splice(ind, 1)
            }
          })
        } else {
          this.$store.dispatch("CreateClassValueFeature", {class_id: this.selectedClass.id, value_id: val.id, type: this.selectedFeatureInClass.type}).then(res => { 
            if (res.success) {
              this.selectedFeatureInClass.value.push(val)
            }
          })
        }
      },
      updateFeatureInClass(){
        for(let elem of this.selectedClass.features){
          let feat = this.allFeatures.find(el => el.id == elem.id)
          elem.name = feat.name
          elem.type = feat.type
          elem.values = feat.values
        }
      },
      upgradeClassInFeature(){
        this.selectedFeatureInClass = null
        this.selectedClass = null
      },
      updateAll(){
        this.$store.dispatch("getAll").then(data => {
          console.log(data)
          let features = []

          for (let elem of data.possible_value2feature){
            let featureElem = {
              id: elem.id,
              name: elem.feature_name,
              type: elem.type,
              values: []
            }
            let values = []
            if (elem.type != 0) values = elem.values
            else 
              for (let elemVal of elem.values){
                let val = {
                  id: elemVal.id,
                  feature_id: elemVal.feature_id,
                  from: elemVal.value_beg,
                  to: elemVal.value_end
                }
                values.push(val)
              }
            featureElem.values = values
            features.push(featureElem)
          }
          
          let classes = []
          for (let elem of data.class2feature2value){
            let classElem = {
              id: elem.id, 
              name: elem.class_name,
              features: []
            }
            for (let feature of elem.features){
              let feat = features.find(el => el.id == feature.id)
              let featureElem = {id: feat.id, name: feat.name, values: feat.values, value: [], type: feat.type}
              console.log(feature)
              if (featureElem.type !== 0){
                for (let elemVal of feature.values){
                  featureElem.value.push(elemVal)
                }
              } else {
                for (let elemVal of feature.values){
                  let val = {
                    id: elemVal.id,
                    feature_id: elemVal.feature_id,
                    from: elemVal.value_beg,
                    to: elemVal.value_end
                  }
                  featureElem.value.push(val)
                }
              }
              classElem.features.push(featureElem)
            }
            classes.push(classElem)
          }

          this.$store.commit('update_classes', classes)

          this.$store.commit('update_features', features)
        })
      }
    }
  }
</script>

<style lang="scss">
  .editor{
    padding: 40px;
    background: #EAEAEA;

    .row{
      justify-content: center;

      .input-elem{
        padding: 0;
      }
    }
    select{
      margin: 5px 0px;
    }
    .interval{
      margin: 0px 5px;
    }
  }
  .card-edit, .card-union{
    margin-top: 15px;
    margin-bottom: 38px;
  }
  .card-union{
    width: 860px;
    margin-left: 15px;
  }
  .card-union .card-body{
    max-height: 186px;
    height: 186px;
  }
  .card-title{
    margin-bottom: 18px !important;
    font-weight: 500 !important;
    line-height: 20px;
    color: #6B6B6B !important;
  }
  .card-edit .card-body, .card-union .card-body{
    padding: 17px;
    background: #FFFFFF !important;
    box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.05) !important;
    border-radius: 6px !important;
  }
  .div-span{
    font-weight: 400;
    line-height: 15px;
    color: #B7B7B7;
    margin-bottom: 10px;
  }
  .card-body{
    height: 330px;
  }
  .div-card{
    padding: 15px;
    padding-top: 0px;
    max-height: 256px;
    overflow-y: auto;
    overflow-x: hidden;
  }
  .form-select{
    background: #FFFFFF;
    border: 1px solid #B7B7B7 !important;
    border-radius: 6px;
  }

  *::-webkit-scrollbar { width: 0; }
  *{
    -ms-overflow-style: none;
    overflow: -moz-scrollbars-none;
  }
  .input-elem, .input-elem-interval{
    margin: 6px 0px;
  }
  .input-elem-interval input {
    height: 34.5px;
    background: #FFFFFF;
    border: 1px solid #A9A9A9;
    border-radius: 6px;
    width: 60px;
  }
  .input-elem-interval-new input{
    height: 34.5px;
    background: #FFFFFF;
    border: 1px solid #CD40FF;
    border-radius: 6px;
    width: 60px;
  }
  .input-elem-new input{
      width: 200px;
      height: 34.5px;
      background: #FFFFFF;
      border: 1px solid #CD40FF;
      border-radius: 6px;
  }
  .input-elem input{
      width: 200px;
      height: 34.5px;
      background: #FFFFFF;
      border: 1px solid #A9A9A9;
      border-radius: 6px;
  }
  .btn-add, .btn-delete{
    background: #FFFFFF !important;
    border: 1px solid #A9A9A9 !important;
    border-radius: 6px !important;
    width: 34.69px !important;
    height: 34.69px !important;
    padding: 0.1rem 0.35rem !important;
    margin-left: 10px;
  }
  .btn-add{
    background: #CD40FF !important;
  }
  .chips{
    color: black !important;
    font-weight: 400 !important;
    margin: 5px;
    background: #FFFFFF !important;
    border: 1px solid #A9A9A9 !important;
    border-radius: 6px !important;
  }
  .chips.active{
    border: 1px solid #CD40FF !important;
  }
  .invalid {
    border: 1px solid red !important;
  }

  input[type="radio"]:checked, 
  input[type="radio"]:not(:checked) 
  {
    position: absolute;
    left: -9999px;
  }
  input[type="radio"]:checked + label, 
  input[type="radio"]:not(:checked) + label {
    display: inline-block;
    position: relative;
    padding-left: 28px;
    line-height: 20px;
    cursor: pointer;
  }

  input[type="radio"]:checked + label:before, 
  input[type="radio"]:not(:checked) + label:before {
    content: "";
    position: absolute;
    left: 0px;
    top: 2.5px;
    background-color: #ffffff;
    width: 13.42px;
    height: 13.42px;
    border: 3px solid #C4C4C4;
  }
  input[type="radio"]:checked + label:before, 
  input[type="radio"]:not(:checked) + label:before {
    border-radius: 100%;
  }
  input[type="radio"]:checked + label:after, 
  input[type="radio"]:not(:checked) + label:after {
    content: "";
    position: absolute;
    -webkit-transition: all 0.2s ease;
    -moz-transition: all 0.2s ease;
    -o-transition: all 0.2s ease;
    transition: all 0.2s ease;
  }
  input[type="radio"]:checked + label:after, 
  input[type="radio"]:not(:checked) + label:after {
    left: 0px;
    top: 2.5px;
    border-radius: 100%;
    width: 13.42px;
    height: 13.42px;
    background: #CD40FF;
  }
  input[type="radio"]:not(:checked) + label:after {
      opacity: 0;
  }
  input[type="radio"]:checked + label:after {
      opacity: 1;
  }
</style>