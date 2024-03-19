<template>
  <Header></Header>
  <InitialBanner :data="initialBannerData"></InitialBanner>
  <RightTarget id="goToDownDesign" :data="history1"></RightTarget>
  <Carousel></Carousel>
  <LeftTarget :data="history2"></LeftTarget>
  <Footer></Footer>
</template>

<script setup>
  import Header from "@/components/layouts/Header.vue";
  import InitialBanner from "@/components/layouts/InitialBanner.vue";
  import LeftTarget from "@/components/layouts/LeftTarget.vue";
  import  RightTarget from "@/components/layouts/RightTarget.vue"
  import Carousel from "@/components/layouts/Carousel.vue";
  import Footer from "@/components/layouts/Footer.vue";
  import url from "@/assets/images/initialBanners/Design.png"
  import image1 from "@/assets/images/jobs/Design/History1.png"
  import image2 from "@/assets/images/jobs/Design/History2.png"

  const initialBannerData = {
    background_image: {
      url: url,
      alt: "Initial Banner Ornamental Iron Works",
    },
    title: "Furniture Forge:<br>Handcrafted Iron<br>Creations",
    classes: "text-white",
    goToId: 'goToDownDesign'
  };
  const history1 = {
    image: {
      url: image1,
      alt: "Image History 1",
    },
    text: "At <span class='text-white bg-black px-2' >Artisan Iron</span>, our process is as meticulous as it is inspiring. It all begins with the conception of each piece, where our skilled designers breathe life into their visions on the canvas of a computer screen. With precision and creativity, they sculpt digital blueprints that serve as the foundation for what will become a tangible work of art.",
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
    text: "But the magic truly unfolds when these designs come to life in the hands of our allied artisans. With a profound respect for tradition and a deep connection to their craft, these artisans infuse each piece with a spirit that transcends mere materiality. Drawing upon the wisdom passed down through generations, they mold iron and bronze with a reverence for the past and a vision for the future.",
    button: {
      text: "",
      link: "",
    },
  };
</script>