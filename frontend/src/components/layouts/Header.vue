<template>
  <header class="bg-header_p bg-opacity-50 flex justify-between p-3 fixed w-full top-0 z-20">
    <a href="#" class="overflow-hidden size-10 ml-4">
      <img
        src="@/assets/images/logo_1.png"
        alt="IronWork Logo"
      />
      <RouterLink class="font-light" :to="{ name: 'home' }">home</RouterLink>
    </a>
    <div class="space-x-8 text-white uppercase flex items-center pr-4">
      <a>
        <RouterLink class="font-light" :to="{ name: 'home' }">home</RouterLink>
      </a>
      <a
        href="#"
        id="WhatWeDoDropdown" 
        data-dropdown-toggle="dropdown" 
        class="inline-flex items-center font-light">
          what we do
        <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
        </svg>
      </a>
      <WhatWeDoDropdown class="font-light"></WhatWeDoDropdown>
      <a>
        <RouterLink class="font-light" :to="{ name: 'contact' }">contact us</RouterLink>
      </a>
      <a>
        <RouterLink class="font-light" :to="{ name: 'about_us' }">about us</RouterLink>
      </a>
    </div>
  </header>
</template>

<script setup>
  import { onMounted } from 'vue';
  import { initFlowbite } from 'flowbite';
  import WhatWeDoDropdown from "@/components/layouts/WhatWeDoDropdown.vue";

  onMounted(async () => initFlowbite());
</script>
