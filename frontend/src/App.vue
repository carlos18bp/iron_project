<template>
  <div>
    <RouterView/>
  </div>
</template>

<script setup>
  import { onMounted } from 'vue';
  import { RouterView } from "vue-router";
  import { useBlogStore } from '@/stores/blog';
  import { useUserStore } from '@/stores/user';
  
  const blogStore = useBlogStore();
  const userStore = useUserStore();

  onMounted(async () => {
    await blogStore.init();
    await userStore.init();
  });
</script>

<style>
  body {
    overflow-x: hidden;
  }
  #app {
    max-width: 100vw; 
    overflow-x: hidden; 
  }
</style>