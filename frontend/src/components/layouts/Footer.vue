<template>
  <footer class="bg-black text-white flex flex-col items-center p-2">
    <img src="@/assets/images/logo_2.png" alt="IronWork Logo" class="w-72 h-60" />
    <div class="flex justify-center space-x-2 p-4 uppercase">
      <a>
        <RouterLink :to="{ name: 'home' }">home</RouterLink>
      </a>
      <p>|</p>
      <a>what we do</a>
      <p>|</p>
      <a>
        <RouterLink :to="{ name: 'contact' }">contact us</RouterLink>
      </a>
      <p>|</p>
      <a>
        <RouterLink :to="{ name: 'about_us' }">about us</RouterLink>
      </a>
    </div>
  </footer>
</template>

<script setup></script>
