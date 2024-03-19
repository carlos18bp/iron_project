<template>
  <Header></Header>
  <InitialBanner :data="initialBannerData"></InitialBanner>
  <RightTarget id="goToDownFurtniture" :data="history1"></RightTarget>
  <div class="flex justify-center">
    <CallToAction text="Get A Free Quote"></CallToAction>
  </div>
  <LeftTarget :data="history2"></LeftTarget>
  <Footer></Footer>
</template>

<script setup>
  import Header from "@/components/layouts/Header.vue";
  import InitialBanner from "@/components/layouts/InitialBanner.vue";
  import LeftTarget from "@/components/layouts/LeftTarget.vue";
  import  RightTarget from "@/components/layouts/RightTarget.vue"
  import CallToAction from "@/components/layouts/CallToAction.vue";
  import Footer from "@/components/layouts/Footer.vue";
  import url from "@/assets/images/initialBanners/Furtniture.png"
  import image1 from "@/assets/images/jobs/Furtniture/History1.png"
  import image2 from "@/assets/images/jobs/Furtniture/History2.png"

  const initialBannerData = {
    background_image: {
      url: url,
      alt: "Initial Banner Ornamental Iron Works",
    },
    title: "Furniture Forge:<br>Handcrafted Iron<br>Creations",
    classes: "text-white",
    goToId: 'goToDownFurtniture'
  };
  const history1 = {
    image: {
      url: image1,
      alt: "Image History 1",
    },
    text: "Transform your space with the elegance and craftsmanship of our furniture. Each piece is a reflection of our dedication to quality, beauty, and cultural heritage, enriching your home with warmth, style, and character.",
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
    text: "Our furniture pieces also embody a commitment to sustainability and social responsibility. By choosing <span class='text-white bg-black px-2' >Artisan Iron</span>, you're not just investing in furniture; you're supporting a legacy of craftsmanship and empowering communities in South America.",
    button: {
      text: "",
      link: "",
    },
  };
</script>