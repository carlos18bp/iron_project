<template>
    <div class="relative flex justify-end py-16 px-8">
      <div class="w-3/5 overflow-hidden inset-y-0 left-0">
        <img
          class="w-full object-cover"
          :src="props.data.image.url"
          :alt="props.data.image.alt"
        />
      </div>
      
      <div class="w-1/2 p-16 h-auto absolute left-0 top-1/4 inline-block">
          <div class="w-full p-16 h-auto relative inline-block custom-background">
            <h2 v-if="props.data.title" class="font-bold text-black text-5xl pb-10">{{ props.data.title }}</h2>
            <p class="text-3xl font-regular" v-html="props.data.text"></p>
          </div>
          <div v-if="props.data.button.text" class="flex justify-start">
              <button class="p-4 h-auto relative inline-block custom-background font-regular">
                <a :href="props.data.button.link" class="text-lg border-b-2 border-black pe-4">{{ props.data.button.text }}</a>
              </button>
          </div>
      </div>
      
    </div>
</template>

<script setup>
  const props = defineProps(['data']);
</script>

<style scoped>
  .custom-background{
      background-image: url(/src/assets/images/layouts/BackgroundSection.png);
  }
</style>