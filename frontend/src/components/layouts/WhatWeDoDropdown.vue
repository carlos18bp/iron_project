<template>
  <!-- Dropdown menu -->
  <div
    id="dropdown"
    class="z-10 hidden divide-y divide-gray-100 rounded-lg shadow bg-header_p bg-opacity-50">
    <ul class="py-2 text-sm text-white" aria-labelledby="WhatWeDoDropdown">
      <li>
        <a href="#" class="block px-4 py-2 hover:bg-gray-400">
          <RouterLink :to="{ name: 'ornamental' }">Ornamental Iron Works</RouterLink
          >
        </a>
      </li>
      <li>
        <a href="#" class="block px-4 py-2 hover:bg-gray-400">
          <RouterLink :to="{ name: 'artistic' }">Artistic Iron Works</RouterLink
          >
        </a>
      </li>
      <li>
        <a href="#" class="block px-4 py-2 hover:bg-gray-400">
          <RouterLink :to="{ name: 'furniture' }">Furniture</RouterLink>
        </a>
      </li>
      <li>
        <a href="#" class="block px-4 py-2 hover:bg-gray-400">
          <RouterLink :to="{ name: 'design' }">Design</RouterLink>
        </a>
      </li>
    </ul>
  </div>
</template>

<script setup></script>
