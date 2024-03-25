<template>
  <Header></Header>
  <div v-if="blog" class="flex flex-col px-16 mt-24">
    <div class="relative flex pb-8">
      <div class="w-full max-h-96 flex items-center justify-center">
        <img
          v-if="blog && blog.image_url"
          :src="`${blog.image_url}`"
          class="object-cover w-full h-full"
        />
      </div>
      <div
        class="bg-white absolute bottom-0 -left-px p-8 pt-4 flex flex-col">
        <h1 class="font-regular font-bold text-4xl tracking-wider">{{ blog.title }}</h1>
      </div>
    </div>
    <div class="flex justify-center">
      <p class="font-regular text-xl tracking-wider">
        {{ blog.description }}
      </p>
    </div>
  </div>
  <BlogCarousel :top="{ top_blog }" class="mb-16"> </BlogCarousel>
  <Footer></Footer>
</template>

<script setup>
  import { onMounted, reactive, ref, watchEffect } from "vue";
  import { useRoute } from "vue-router";
  import { useBlogStore } from "@/stores/blog";
  import Header from "@/components/layouts/Header.vue";
  import Footer from "@/components/layouts/Footer.vue";
  import BlogCarousel from "@/components/blog/BlogCarousel.vue";

  const route = useRoute();
  const blogStore = useBlogStore();
  const blog_id = ref(0);
  const blog = reactive({});
  const top_blog = ref(null);

  if (window.innerWidth >= 1024) {
    top_blog.value = 3;
  } else if (window.innerWidth < 1024 && 760 <= window.innerWidth) {
    top_blog.value = 2;
  } else if (window.innerWidth < 760) {
    top_blog.value = 1;
  }

  onMounted(async () => await blogStore.fetchBlogsData());

  watchEffect(async () => {
    blog_id.value = parseInt(route.params.blog_id);
    if (blog_id.value) Object.assign(blog, blogStore.blogById(blog_id.value));
    window.scrollTo({
        top: 0,
        behavior: "smooth",
    });
  });
</script>