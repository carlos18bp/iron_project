<template>
  <div class="relative h-screen">
    <div class="absolute inset-0">
      <img
        class="w-full h-full object-cover"
        :src="props.data.background_image.url"
        :alt="props.data.background_image.alt"
      />
    </div>
    <div class="absolute inset-0 flex items-center justify-center">
      <h1
        class="text-8xl text-center font-bold leading-normal"
        :class="props.data.classes"
        v-html="props.data.title"></h1>
    </div>
    <a 
      href="#"
      @click.prevent="scrollToTarget"
      class="absolute bottom-8 left-1/2 transform -translate-x-1/2">
      <img src="@/assets/images/vectors/arrow.png" alt="Arrow to down" />
    </a>
  </div>
</template>

<script setup>
  const props = defineProps(["data"]);

  const scrollToTarget = () => {
    const targetId = props.data.goToId;
    
    const targetElement = document.getElementById(targetId);
    
    if (targetElement) {
      targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };
</script>
