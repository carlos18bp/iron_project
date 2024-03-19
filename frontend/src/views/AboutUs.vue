<template>
  <Header></Header>
  <InitialBanner :data="initialBannerData"></InitialBanner>
  <RightTarget id="goToAboutUs" :data="history1"></RightTarget>
  <div class="flex justify-center">
    <CallToAction text="Get A Free Quote"></CallToAction>
  </div>
  <LeftTarget :data="history2"></LeftTarget>
  <RightTarget :data="history3"></RightTarget>
  <div class="flex justify-center">
    <CallToAction text="Get A Free Quote"></CallToAction>
  </div>
  <LeftTarget :data="history4"></LeftTarget>
  <Footer></Footer>
</template>

<script setup>
  import Header from "@/components/layouts/Header.vue";
  import InitialBanner from "@/components/layouts/InitialBanner.vue";
  import Footer from "@/components/layouts/Footer.vue";
  import RightTarget from "../components/layouts/RightTarget.vue";
  import LeftTarget from "../components/layouts/LeftTarget.vue";
  import CallToAction from "../components/layouts/CallToAction.vue";
  import url from "@/assets/images/initialBanners/AboutUs.png";
  import image1 from "@/assets/images/AboutUs/History1.png";
  import image2 from "@/assets/images/AboutUs/History2.png";
  import image3 from "@/assets/images/AboutUs/History3.png";
  import image4 from "@/assets/images/AboutUs/History4.png";

  const initialBannerData = {
    background_image: {
      url: url,
      alt: "Initial Banner About Us",
    },
    title: "Crafting Excellence for<br>Discerning Clients<br>Worldwide",
    classes: "text-white",
    goToId: "goToAboutUs",
  };

  const history1 = {
    image: {
      url: image1,
      alt: "Image History 1",
    },
    text: "Deep in the heart of South America, where ancient traditions weave into the vibrant pulse of rich and diverse cultures, the essence of <span class='text-white bg-black px-2'>Artisan Iron</span> is born. In workshops bathed in the soft light of dawn and the glow of the forges, generations of artisans forge with expert hands and hearts full of passion.",
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
    text: "Every gate, railing, balcony, and accessory from <span class='text-white bg-black px-2' >Artisan Iron</span> is a symphony of skill and art, a fusion of South America's rich heritage with the modernity and style demanded by the exclusive California market. Each piece is a bridge between continents, a celebration of diversity and artisanal mastery.",
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
    text: "Beyond providing exceptional decorative elements for residences and commercial spaces in California, <span class='text-white bg-black px-2' >Artisan Iron</span> is committed to sustainability and positive social impact. Investing in our products not only beautifies Californian spaces but also supports the preservation of a traditional art and provides economic opportunities in South America.",
    button: {
      text: "",
      link: "",
    },
  };
  const history4 = {
    image: {
      url: image4,
      alt: "Image History 1",
    },
    text: "175 SW 7th St, Suite 1524 <br>Miami, Florida <br>33130 <br><br>info@artisaniron.co <br><br>Phone: +571 5523012 <br>Mobile: +57 3182064153",
    button: {
      text: "",
      link: "",
    },
    title: "Artisian Iron",
  };
</script>
