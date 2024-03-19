<template>
  <Header></Header>
  <InitialBanner :data="initialBannerData"></InitialBanner>
  <RightTarget id="goToDownOrnamental" :data="history1"></RightTarget>
  <LeftTarget :data="history2"></LeftTarget>
  <div class="flex justify-center">
    <CallToAction text="Get A Free Quote"></CallToAction>
  </div>
  <RightTarget :data="history3"></RightTarget>
  <Footer></Footer>
</template>

<script setup>
  import Header from "@/components/layouts/Header.vue";
  import InitialBanner from "@/components/layouts/InitialBanner.vue";
  import LeftTarget from "@/components/layouts/LeftTarget.vue";
  import  RightTarget from "@/components/layouts/RightTarget.vue"
  import CallToAction from "@/components/layouts/CallToAction.vue";
  import Footer from "@/components/layouts/Footer.vue";
  import url from "@/assets/images/initialBanners/Ornamental.png"
  import image1 from "@/assets/images/jobs/Ornamental/History1.png"
  import image2 from "@/assets/images/jobs/Ornamental/History2.png"
  import image3 from "@/assets/images/jobs/Ornamental/History3.png"

  const initialBannerData = {
    background_image: {
      url: url,
      alt: "Initial Banner Ornamental Iron Works",
    },
    title: "Iron Mastery: Crafting<br>Timeless Ornamental<br>Works",
    classes: "text-white",
    goToId: 'goToDownOrnamental'
  };
  const history1 = {
    image: {
      url: image1,
      alt: "Image History 1",
    },
    text: "Step into a world where craftsmanship meets creativity with <span class='text-white bg-black px-2' >Artisan Iron's</span> Ornamental Iron Work. Nestled in the heart of South America, our artisans blend tradition with innovation to produce captivating pieces that transcend mere functionality. From elegant gates to intricate railings, each creation tells a story of heritage and artistry, bridging continents and cultures.",
    button: {
      text: "",
      link: "",
    },
  };
  const history2 = {
    image: {
      url: image2,
      alt: "Image History 1",
    },
    text: "Beyond their aesthetic appeal, our ornamental iron pieces also embody a commitment to sustainability and social responsibility. By choosing <span class='text-white bg-black px-2' >Artisan Iron</span>, you're not just acquiring a piece of decor; you're investing in a legacy of craftsmanship and supporting communities in South America.",
    button: {
      text: "",
      link: "",
    },
  };
  const history3 = {
    image: {
      url: image3,
      alt: "Image History 1",
    },
    text: "Elevate your space with the timeless elegance of our Ornamental Iron Work. Each piece is a masterpiece in its own right, enriching your surroundings with beauty, history, and cultural significance.",
    button: {
      text: "",
      link: "",
    },
  };
</script>