<template>
  <div>
    <button
      class="bg-gray_p px-12 py-4 text-white font-regular text-2xl uppercase"
      @click="handleButtonClick">
      {{ text }}
    </button>
  </div>
</template>

<script setup>
    import { useRouter } from 'vue-router';

    const props = defineProps({
        text: String,
    });
    const router = useRouter();

    const handleButtonClick = () => {
   
      router.push({ name: 'contact' }).then(() => {
        const targetElement = document.getElementById('goToDownContact');
        if (targetElement) {
          targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    };
</script>
