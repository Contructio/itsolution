var messages = new Vue({
    el: '#messages',
    data: {
        messages: []
    },
    created: function () {
        axios.get('api/get_messages')
            .then(function (response){
                console.log(response.data)
                this.messages = response.data
            })
    }
})