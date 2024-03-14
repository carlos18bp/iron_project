import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("@/views/Home.vue"),
    },
    {
      path: "/blog/:blog_id",
      name: "blog",
      component: () => import("@/views/blog/Detail.vue"),
    },
    {
      path: "/blogs",
      name: "blogs",
      component: () => import("@/views/blog/List.vue"),
    },
    {
      path: "/about_us",
      name: "about_us",
      component: () => import("@/views/AboutUs.vue"),
    },
    {
      path: "/contact",
      name: "contact",
      component: () => import("@/views/Contact.vue"),
    },
    {
        path: "/ornamental",
        name: "ornamental",
        component: () => import("@/views/jobs/Ornamental.vue"),
    },
    {
        path: "/artistic",
        name: "artistic",
        component: () => import("@/views/jobs/Artistic.vue"),
    },
    {
        path: "/furniture",
        name: "furniture",
        component: () => import("@/views/jobs/Furniture.vue"),
    },
    {
      path: "/design",
      name: "design",
      component: () => import("@/views/jobs/Design.vue"),
    },
  ],
});

export default router;
export const routes = router.options.routes;