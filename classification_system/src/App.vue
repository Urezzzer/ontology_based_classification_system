<template>
  <nav class="fixed-top">
    <router-link to="/knowledge">База знаний</router-link>
    <router-link to="/editor">Редактор</router-link> 
    <router-link to="/">Классификатор</router-link> 
  </nav>
  <div style="margin-top: 50px;">
    <router-view/>
  </div>
</template>

<script>
  import {  mapState } from 'vuex'
  //import $ from "jquery" 

  export default {
    data() {
        return {
            
        }
    },            
    computed: {
      ...mapState({
        //allClasses:'classes',
        //allFeatures:'features',
      }),
    },
    mounted(){
      // knowledge
      this.$router.push({ name: 'knowledge'})
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
      
    },
    methods: {}
}
</script>

<style lang="scss">
html {
  background: #EAEAEA;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
    padding: 20px;
    background: #FFFFFF;
    height: 64px;

  a {
    font-weight: bold;
    color: #000000;
    text-decoration: none;
    margin: 0px 15px;

    &.router-link-exact-active {
      border-bottom: 3px solid #CD40FF;
      border-radius: 2px;
    }
    &:active, &:focus, &:hover{
      color: #000000;
    }
  }
}

input:focus, input:active, select:focus {
    outline-style: none;
    outline-width: 0px !important;
    outline-color: none !important;
    outline: none !important;
    border: 1px solid #A9A9A9 !important;
    box-shadow:  0 1px 1px #a9a9a900 inset, 0 0 8px #a9a9a949 !important;
}

@font-face {
	font-family: 'VK Sans Display'; 
	src: url(./assets/fonts/VKSansDisplay-Regular.ttf); 
}
 
*, td, select, input, input::placeholder{
	font-family: 'VK Sans Display' !important;
  font-style: normal
}
</style>
