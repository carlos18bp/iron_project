<template>
  <Header></Header>
  <section>
    <InitialBanner :data="initialBannerData"></InitialBanner>
  </section>

  <section id="goToDownHome" class="my-28 px-16">
    <div class="flex justify-evenly">
      <div class="inline-block">
        <img src="@/assets/images/home/carousel/OrnamentalWorks.png" class="w-72" alt="Ornamental carousel"/>
        <div class="flex justify-center h-24">
          <div
            class="w-3/4 px-4 py-2 h-full bg-gray_p grid justify-center content-center mt-2">
            <a
              href="ornamental"
              class="text-center font-regular flex justify-center text-white text-3xl">
              Ornamental<br/>Works
            </a>
          </div>
        </div>
      </div>

      <div class="inline-block">
        <img src="@/assets/images/home/carousel/ArtisticWorks.png" class="w-72" alt="Artistic carousel" />
        <div class="flex justify-center h-24">
          <div
            class="w-3/4 px-4 py-2 h-full bg-gray_p grid justify-center content-center mt-2">
            <a
              href="artistic"
              class="text-center font-regular flex justify-center text-white text-3xl">
              Artistic<br/>Works
            </a>
          </div>
        </div>
      </div>

      <div class="inline-block">
        <img src="@/assets/images/home/carousel/Furniture.png" class="w-72" alt="Furniture carousel" />
        <div class="flex justify-center h-24">
          <div
            class="w-3/4 px-4 py-2 h-full bg-gray_p grid justify-center content-center mt-2">
            <a
              href="furniture"
              class="text-center font-regular flex justify-center text-white text-3xl">
              Furtniture
            </a>
          </div>
        </div>
      </div>

      <div class="inline-block">
        <img src="@/assets/images/home/carousel/Design.png" class="w-72" alt="..." />
        <div class="flex justify-center h-24">
          <div
            class="w-3/4 px-4 py-2 h-full bg-gray_p grid justify-center content-center mt-2">
            <a
              href="design"
              class="text-center font-regular flex justify-center text-white text-3xl">
              Design
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <RightTarget :data="history1"></RightTarget>
  </section>

  <section>
    <Carousel></Carousel>
  </section>

  <section>
    <LeftTarget :data="history2"></LeftTarget>
  </section>

  <section>
    <RightTarget :data="history3"></RightTarget>
  </section>

  <section>
    <div class="p-16 flex">
      <h2 class="w-1/2 text-5xl font-regular">
        Are you prepared to accelerate your project with our exquisite forged
        creations?
      </h2>
      <div
        class="w-1/4 flex justify-start items-center border-t-black border-2 border-white">
        <CallToAction
          text="Contact"
        ></CallToAction>
      </div>
    </div>
  </section>

  <Footer></Footer>
</template>

<script setup>
  import Header from "@/components/layouts/Header.vue";
  import Footer from "@/components/layouts/Footer.vue";
  import CallToAction from "@/components/layouts/CallToAction.vue";
  import InitialBanner from "@/components/layouts/InitialBanner.vue";
  import RightTarget from "@/components/layouts/RightTarget.vue";
  import LeftTarget from "@/components/layouts/LeftTarget.vue";
  import Carousel from "@/components/layouts/Carousel.vue";
  import url from "@/assets/images/initialBanners/Home.png";
  import image1 from "@/assets/images/home/History1.png";
  import image2 from "@/assets/images/home/History2.png";
  import image3 from "@/assets/images/home/History3.png";


  const initialBannerData = {
    background_image: {
      url: url,
      alt: "Initial Banner Home",
    },
    title: "Forged Legacies:<br>Where Tradition Meets<br>MODERNITY",
    classes: "text-white",
    goToId: 'goToDownHome',
  };

  const history1 = {
    image: {
      url: image1,
      alt: "Image History 1",
    },
    text: "Transform your living or workspace into a gallery of elegance and distinction with our exclusive collection of decorative ironwork.",
    button: {
      text: "CONTACT",
      link: "contact",
    },
  };

  const history2 = {
    image: {
      url: image2,
      alt: "Image History 2",
    },
    text: "Our portfolio includes bespoke gates, intricate grilles, elegant railings, and statement furniture, each designed to elevate the aesthetic of your environment.",
    button: {
      text: "ABOUT",
      link: "about_us",
    },
  };

  const history3 = {
    image: {
      url: image3,
      alt: "Image History 3",
    },
    text: "Join us in redefining luxury and style with ironwork that's more than just decoration—it's a lifestyle.",
    button: {
      text: "ABOUT",
      link: "about_us",
    },
  };
</script>

<style scoped>
  .swiper-container {
    width: 100%;
    height: 300px;
  }
</style>
