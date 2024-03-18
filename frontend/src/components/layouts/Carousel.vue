<template>
  <vue-marquee-slider
    id="marquee-slider-cards"
    :space="25"
    :speed="20000"
    :width="420"
  >
    <img src="@/assets/images/home/Gallery/Carousel1.png" />
    <img src="@/assets/images/home/Gallery/Carousel2.png" />
    <img src="@/assets/images/home/Gallery/Carousel3.png" />
    <img src="@/assets/images/home/Gallery/Carousel4.png" />
  </vue-marquee-slider>

  <vue-marquee-slider
    class="mt-6"
    id="marquee-slider-reverse"
    :space="25"
    :speed="20000"
    :width="420"
    reverse
  >
    <img src="@/assets/images/home/Gallery/Carousel5.png" />
    <img src="@/assets/images/home/Gallery/Carousel6.png" />
    <img src="@/assets/images/home/Gallery/Carousel7.png" />
    <img src="@/assets/images/home/Gallery/Carousel8.png" />
  </vue-marquee-slider>
</template>

<script setup>
  import { VueMarqueeSlider } from "vue3-marquee-slider";
</script>

<style>
  ._marqueeSlider_1htck_3 {
    overflow: hidden;
  }
  ._marqueeSliderContainer_1htck_11 {
    width: 100%;
    animation-name: _horizontalAnimation_1htck_1;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    display: flex;
  }
  ._marqueeSliderContainerVertical_1htck_27 {
    height: fit-content;
    animation-name: _verticalAnimation_1htck_1;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    display: flex;
    flex-direction: column;
  }
  @keyframes _horizontalAnimation_1htck_1 {
    0% {
      transform: translate(0);
    }
    to {
      transform: translate(-100%);
    }
  }

  @keyframes _verticalAnimation_1htck_1 {
    0% {
      transform: translateY(0);
    }
    to {
      transform: translateY(-100%);
    }
  }
</style>
