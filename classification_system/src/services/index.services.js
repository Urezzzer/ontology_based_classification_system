import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/'

class Service {
    async getAll() {
        return axios
            .get(API_URL + 'get_knowledge/')
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }

    async updateClass(item){
        return axios
            .put(API_URL + 'update_class/', {...item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }
    async updateFeature(item){
        return axios
            .put(API_URL + 'update_feature/', {...item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }
    async updatePosValueFeature(item){
        return axios
            .put(API_URL + 'update_posvalue2feature/', {...item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }

    async DeleteClass(item){
        console.log(item)
        return axios
            .delete(API_URL + 'delete_class/', {data: item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }
    async DeleteFeature(item){
        return axios
            .delete(API_URL + 'delete_feature/', {data: item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }
    async DeleteClassFeature(item){
        return axios
            .delete(API_URL + 'delete_feature2class/', {data: item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }
    async DeletePosValueFeature(item){ //удаление возможного значения для признака
        return axios
            .delete(API_URL + 'delete_posvalue2feature/', {data: item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }
    async DeleteClassValueFeature(item){ //удаляет связь между классом и значением признака
        return axios
            .delete(API_URL + 'delete_picked_value2feature2class/', {data: item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }

    async CreateClass(item){
        return axios
            .post(API_URL + 'insert_class/', {...item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }
    async CreateFeature(item){
        return axios
            .post(API_URL + 'insert_feature/', {...item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }
    async CreateClassFeature(item){
        return axios
            .post(API_URL + 'insert_feature2class/', {...item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }
    async CreatePosValueFeature(item){
        return axios
            .post(API_URL + 'insert_posvalue2feature/', {...item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }
    async CreateClassValueFeature(item){
        return axios
            .post(API_URL + 'insert_picked_value2feature2class/', {...item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }

    async CheckClass(item){
        return axios
            .post(API_URL + '', {...item})
            .then(response => {
                if (response.data) {
                    console.log(response.data)
                    return response.data
                } else {
                    return null
                }
            })
    }
}

export default new Service()