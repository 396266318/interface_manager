<template>
  <div class="index-main-div">
    <el-menu :default-active="active_tab" class="el-menu-vertical-demo index-menu" @select="handle_select" :collapse="isCollapse">
      <el-menu-item index="1">
        <i class="el-icon-document"></i>
        <span slot="title">接口</span>
      </el-menu-item>

      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">任务</span>
      </el-menu-item>

      <el-menu_item index="3">
        <i class="el-icon-star-on"></i>
        <span slot="title">mock</span>
      </el-menu_item>

      <el-menu-item index="4">
        <i class="el-icon-rank"></i>
        <span slot="title">调试</span>
      </el-menu-item>
    </el-menu>

    <div class="index-context">
      <services></services>
    </div>
  </div>
</template>

<script>
  // 引入 requests/user js 文件 引入user 包
  import {get_user} from "../requests/user";
  import services from "./serivce/services";

  // 返回当前用户
  export default {
    name: 'index',
    props: ['tab'],  // url 里面的参数
    comments: {
      services,
    },
    data() {
      return {
        current_user: {},
        isCollapse: true,
        active_tab: '1',
      }
    },
    methods: {
      handle_select(index, index_path) {
        this.$router.push('/index/' + index);
      }
    },

    mounted() {
      get_user().then(data =>{
        if (true === data.success){
          this.current_user = data.data;
        } else {
          this.$router.push('/login');
        }
      }),
        this.active_tab = this.tab;
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style scoped>
  .el-menu-vertical-demo:not(.el-menu--collapse){
    width: 200px;
    min-height: 400px;
  }

  .index-main-div {
    display: flex;
  }

  .index-menu {
    width: 5%;
  }

  .index-context {
    width: 95%;
  }
</style>
