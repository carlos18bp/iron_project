<template>
  <div class="flex flex-col w-full items-center">
    <div class="w-1/2">
      <h2 id="{{ headerId }}">
        <button 
          type="button" 
          class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 gap-3" 
          :data-accordion-target="'#' + bodyId"
          aria-expanded="false" 
          :aria-controls="bodyId">
          <span>{{ question }}</span>
          <svg class="w-6 h-6 text-gray-800" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14m-7 7V5"/>
          </svg>
        </button>
      </h2>
      <div 
        :id="bodyId" 
        class="hidden" 
        aria-labelledby="{{ headerId }}">
        <div class="p-5 border border-b-0 border-gray-200">
          <p class="mb-2 text-gray-500">{{ answer }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  const props = defineProps({
    question: String,
    answer: String,
    headerId: String,
    bodyId: String
  });
</script>
