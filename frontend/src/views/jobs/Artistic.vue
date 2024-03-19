<template>
  <Header></Header>
  <InitialBanner :data="initialBannerData"></InitialBanner>
  <RightTarget id="goToDownArtistic" :data="history1"></RightTarget>
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
  import url from "@/assets/images/initialBanners/Artistic.png"
  import image1 from "@/assets/images/jobs/Artistic/History1.png"
  import image2 from "@/assets/images/jobs/Artistic/History2.png"

  const initialBannerData = {
    background_image: {
      url: url,
      alt: "Initial Banner Ornamental Iron Works",
    },
    title: "Artistic Iron Works:<br>Crafting Masterpieces",
    classes: "text-white",
    goToId: 'goToDownArtistic'
  };
  const history1 = {
    image: {
      url: image1,
      alt: "Image History 1",
    },
    text: "Immerse yourself in the world of Artistic Iron Work by <span class='text-white bg-black px-2' >Artisan Iron</span>, where imagination knows no bounds. Inspired by the vibrant cultures of South America, our artisans push the boundaries of creativity to produce captivating pieces that redefine the notion of functional art. From intricate sculptures to bold installations, each creation is a celebration of innovation and expression.",
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