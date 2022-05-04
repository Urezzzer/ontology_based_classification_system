<template>
  <div class="home">
    <table class="table table-sm">
      <thead>
        <tr>
          <th scope="col-3"></th>
          <th scope="col-3" v-for="elem in allClasses" :key="elem.id">{{elem.name}}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="feature in allFeatures" :key="feature.id">
          <th scope="row">{{feature.name}}</th>
          <td v-for="elem in allClasses" :key="elem.id">{{getValueFeature(feature.id, elem)}}</td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
  import {  mapState } from 'vuex'

  export default {
    name: 'HomeView',
    data() {
      return {
        
      }
    },
    computed: {
      ...mapState({
        allClasses:'classes',
        allFeatures:'features',
      }),
    },
    mounted() {
      
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
    },
    methods:{
      getValueFeature(feature_id, class_elem){
        let item = class_elem.features.find(el => el.id == feature_id)
        let line = ''
        if (item && item.value.length){
          if (item.type == 0){
            for (let val of item.value) {
              line += `[${val.from} ... ${val.to}], `
            }
            line += ':'
            line = line.replace(', :', '')
          } else {
            line += '{'
            for (let val of item.value) line += (val.value + ', ')
            line += '}'
            line = line.replace(', }', '}')
          }
        } else line = ''
        return line
      }
    }
  }
</script>

<style lang="scss">
  .home{
    padding: 70px;
    th, td{
      max-width: 300px !important;
      width: 300px !important;
    }
    tr{
      border-bottom-color: #B7B7B7;
      border-bottom-width: 2px;
    }
    thead tr{
      border-bottom-color: #000000;
    }
  }
</style>