<template>
  <div class="flex flex-col">
    <div>
      <img
        v-if="blog && blog.image_url"
        :src="`/api/${blog.image_url}`"
        class="object-cover w-full h-96 pb-4"
      />
    </div>
    <h2 class="font-light text-gray_p tracking-widest text-xl uppercase pb-2">
      {{ blog.category }}
    </h2>
    <RouterLink
      v-if="blog.id"
      :to="{
        name: 'blog',
        params: { blog_id: blog.id },
      }"
      class="font-bold text-3xl tracking-wider pb-3">
      {{ blog.title }}
    </RouterLink>
  </div>
</template>

<script setup>
  import { RouterLink } from "vue-router";

  const props = defineProps({
  blog: Object,
  });
</script>
