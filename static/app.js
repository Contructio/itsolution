Vue.component('message-item', {
  template: '\
    <li>\
      {{ title }}\
      <button v-on:click="$emit(\'remove\')">Прочитано</button>\
    </li>\
  ',
  props: ['title', 'date', 'key']
})

new Vue({
    el: '#messages',
    data: {
        messages: []
    },
    created: function () {
        const vm = this;
        axios.get('api/get_messages?last_id=0')
            .then(function (response){
                vm.messages = response.data;
            })
        setInterval(function () {vm.upd()}, 10000)
        },
    methods:{
        markread: function (index, id){
            const vm = this
            axios.get('api/mark_read?id=' + id)
            vm.messages.splice(index, 1)
        },
        upd: function (){
            const vm = this;
            axios.get('api/get_messages?last_id=' + vm.messages[vm.messages.length-1].id)
                .then(function (response){
                    response.data.splice(0, 1)
                    vm.messages = vm.messages.concat(response.data)
                })
        }
    }
})