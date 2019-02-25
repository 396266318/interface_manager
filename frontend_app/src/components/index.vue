<template>
  <div>
    Hello I am index
  </div>
</template>

<script>
  // 引入 requests/user js 文件 引入user 包
  import {get_user} from "../requests/user";

  // 返回当前用户
  export default {
    name: 'index',
    data() {
      return {
        current_user: {}
      }
    },
    mounted() {
      get_user().then(data =>{
        if (true === data.success){
          this.current_user = data.data;
        }else{
          this.$router.push('/login');
        }
      })
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>

</style>
