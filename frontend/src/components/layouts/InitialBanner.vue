<script setup>
import { defineProps } from 'vue';

const props = defineProps(['props']);

</script>

<template>
    <div class="relative h-screen">
        <div class="absolute inset-0">
            <img
            class="w-full h-full object-cover"
            :src="props.props.background_image.url"
            :alt="props.props.background_image.alt"
            />
        </div>
        <div class="absolute inset-0 flex items-center justify-center">
            <h1 class="text-8xl text-white text-center font-bold leading-normal" v-html="props.props.title"></h1>
        </div>
        <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2">
        <img
            src="@/assets/images/vectors/arrow.png"
            alt="Arrow to down"
        />
        </div>
    </div>
</template>
