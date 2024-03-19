<template>
  <Header></Header>
  <div class="flex flex-col">
    <div class="flex p-32 pl-20 pb-8">
      <div class="w-full">
        <img
          v-if="firstBlog && firstBlog.image_url"
          :src="`/api/${firstBlog.image_url}`"
          class="w-full object-cover"
        />
      </div>
      <div class="w-full flex flex-col justify-center pl-20">
        <p
          class="font-regular tracking-widest text-lg text-gray_p uppercase pb-2">
          {{ firstBlog.category }}
        </p>
        <h1 class="py-3">
          <RouterLink
            v-if="firstBlog.id"
            :to="{
              name: 'blog',
              params: { blog_id: firstBlog.id },
            }"
            class="font-regular font-bold text-3xl tracking-wider break-all">
            {{ firstBlog.title }}
          </RouterLink>
        </h1>
        <p class="font-regular text-1xl line-clamp-5 tracking-wider pt-4">
          {{ firstBlog.description }}
        </p>
      </div>
    </div>

    <div class="mb-16 px-14 pt-16">
      <div class="grid grid-cols-3 gap-12 pb-8">
        <BlogPresentation
          v-for="blog in paginatedBlogs"
          :blog="blog"
        ></BlogPresentation>
      </div>
      <nav
        class="flex items-center justify-between border-t border-gray-200 px-4 ">
        <!-- Previous page button -->
        <a
          href="#"
          class="inline-flex items-center border-t-2 border-transparent pr-1 pt-4 text-sm font-medium text-gray-500"
          @click="goToPage(currentPage - 1)"
          :disabled="currentPage === 1">
          <ArrowLongLeftIcon
            class="mr-3 h-5 w-5"
            aria-hidden="true"
          />
          Previous
        </a>

        <!-- Show page numbers -->
        <div class="block">
          <template v-for="page in totalPages" :key="page">
            <a
              href="#"
              class="inline-flex items-center border-t-2 border-transparent px-4 pt-4 text-sm font-medium"
              :class="{
                'border-primary_p text-primary_p': currentPage === page,
                'text-gray-500 hover:text-terciary_p hover:border-terciary_p':
                  currentPage !== page,
              }"
              @click="goToPage(page)">
              {{ page }}
            </a>
          </template>
        </div>

        <!-- Next page button -->
        <a
          href="#"
          class="inline-flex items-center border-t-2 border-transparent pl-1 pt-4 text-sm font-medium text-gray-500 hover:border-terciary_p hover:text-terciary_p"
          @click="goToPage(currentPage + 1)"
          :disabled="currentPage === totalPages">
          Next
          <ArrowLongRightIcon
            class="ml-3 h-5 w-5 text-terciary_p"
            aria-hidden="true"
          />
        </a>
      </nav>
    </div>
  </div>
  <Footer></Footer>
</template>

<script setup>
  import { RouterLink } from "vue-router";
  import { computed, reactive, ref, onMounted } from "vue";
  import Header from "@/components/layouts/Header.vue";
  import Footer from "@/components/layouts/Footer.vue";
  import { useBlogStore } from "@/stores/blog";
  import BlogPresentation from "@/components/blog/BlogPresentation.vue";
  import { ArrowLongLeftIcon, ArrowLongRightIcon } from "@heroicons/vue/20/solid";

  const blogStore = useBlogStore();
  const blogs = ref([]);
  const firstBlog = reactive({});
  const currentPage = ref(1);
  const isBlogsLoaded = ref(false);
  let blogsPerPage;

  onMounted(async () => fetchBlogs());

  if (window.innerWidth >= 1024) {
    blogsPerPage = 6;
  } else if (window.innerWidth < 1024 && 760 <= window.innerWidth) {
    blogsPerPage = 4;
  } else if (window.innerWidth < 760) {
    blogsPerPage = 2;
  }

  /**
   * Fetch and update blogs data.
   */
  async function fetchBlogs() {
    await blogStore.fetchBlogsData();
    blogs.value = blogStore.blogs;

    isBlogsLoaded.value = true;

    if (blogStore.blogs.length > 0) {
        Object.assign(firstBlog, blogStore.blogs[0]);
    }
  }

  // Calculate the total number of pages
  const totalPages = computed(() => {
    if (isBlogsLoaded.value) {
        return Math.ceil(blogs.value.length / blogsPerPage);
    }
    return 0;
  });

  // Calculate the blogs to display on the current page
  const paginatedBlogs = computed(() => {
    if (isBlogsLoaded.value) {
        const start = (currentPage.value - 1) * blogsPerPage;
        const end = start + blogsPerPage;
        return blogs.value.slice(start, end);
    }
    return [];
  });

  // Property to store the scroll position
  const scrollPosition = ref(0);

  // Function to go to a specific page
  const goToPage = (page) => {
    if (isBlogsLoaded.value && page >= 1 && page <= totalPages.value) {
        // Save current scroll position
        scrollPosition.value = window.scrollY;
        currentPage.value = page;

        setTimeout(() => {
        window.scrollTo(0, scrollPosition.value);
        }, 0);
    }
  };
</script>