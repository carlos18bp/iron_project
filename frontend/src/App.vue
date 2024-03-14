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
