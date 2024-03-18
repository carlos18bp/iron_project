<template>
    <div class="relative flex justify-end py-16 px-8">
      <div class="w-3/5 overflow-hidden inset-y-0 left-0">
        <img
          class="w-full object-cover"
          :src="props.props.image.url"
          :alt="props.props.image.alt"
        />
      </div>
      
      <div class="w-1/2 p-16 h-auto absolute left-0 top-1/4 inline-block">
          <div class="w-full p-16 h-auto relative inline-block custom-background">
            <p class="text-3xl">{{ props.props.text }}</p>
          </div>
          <div class="flex justify-start">
              <button class="p-4 h-auto relative inline-block custom-background font-regular">
                <a class="text-lg border-b-2 border-black pe-4">{{ props.props.button.text }}</a>
              </button>
          </div>
      </div>
      
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps(['props']);

</script>

<style scoped>

.custom-background{
    background-image: url(/src/assets/images/layouts/BackgroundSection.png);
}

</style>