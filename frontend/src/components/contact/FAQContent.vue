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
          <svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5 5 1 1 5"/>
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
