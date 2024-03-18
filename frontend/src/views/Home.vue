<template>
  <Header></Header>
    <section>
        <InitialBanner :props="initialBannerData"></InitialBanner>
    </section>
    
    <section class="my-28 px-16">
        <div class="flex justify-evenly">
            <div class="inline-block">
                <img src="@/assets/images/home/carousel/OrnamentalWorks.jpg" alt="...">
                <div class="flex justify-center h-24">
                    <div class="w-3/4 px-4 py-2 h-full bg-gray_p grid justify-center content-center mt-2">
                        <a class="text-center font-regular flex justify-center text-white text-3xl">Ornamental<br>Works</a>
                    </div>
                </div>
            </div>

            <div class="inline-block">
                <img src="@/assets/images/home/carousel/ArtisticWorks.png" alt="...">
                <div class="flex justify-center h-24">
                    <div class="w-3/4 px-4 py-2 h-full bg-gray_p grid justify-center content-center mt-2">
                        <a class="text-center font-regular flex justify-center text-white text-3xl">Artistic<br>Works</a>
                    </div>
                </div>
            </div>

            <div class="inline-block">
                <img src="@/assets/images/home/carousel/Furniture.png" alt="...">
                <div class="flex justify-center h-24">
                    <div class="w-3/4 px-4 py-2 h-full bg-gray_p grid justify-center content-center mt-2">
                        <a class="text-center font-regular flex justify-center text-white text-3xl">Furtniture</a>
                    </div>
                </div>
            </div>

            <div class="inline-block">
                <img src="@/assets/images/home/carousel/Design.png" alt="...">
                <div class="flex justify-center h-24">
                    <div class="w-3/4 px-4 py-2 h-full bg-gray_p grid justify-center content-center mt-2">
                        <a class="text-center font-regular flex justify-center  text-white text-3xl">Design</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <RightTarget :props="history1"></RightTarget>
    </section>
    
    <section>
        <Carousel></Carousel>
    </section>

    <section>
        <LeftTarget :props="history2"></LeftTarget>
    </section>

    <section>
        <RightTarget :props="history3"></RightTarget>
    </section>

    <section>
        <div class="p-16 flex">
            <h2 class="w-1/2 text-5xl font-regular">Are you prepared to accelerate your project with our exquisite forged creations?</h2>
            <div class="w-1/4 flex justify-start items-center border-t-black border-2 border-white">
                <button class="bg-gray_p px-12 py-4 text-white font-regular text-2xl">CONTACT</button>
            </div>
        </div>
    </section>

    <Footer></Footer>
</template>

<script setup>
import Header from "@/components/layouts/Header.vue";
import Footer from "@/components/layouts/Footer.vue";
import InitialBanner from '../components/layouts/InitialBanner.vue';
import RightTarget from '../components/layouts/RightTarget.vue';
import LeftTarget from '../components/layouts/LeftTarget.vue';
import Carousel from '../components/layouts/Carousel.vue'
import url from '@/assets/images/initialBanners/Home.jpg';
import image1 from '@/assets/images/home/History1.png'
import image2 from '@/assets/images/home/History2.png'
import image3 from '@/assets/images/home/History3.png'

const initialBannerData = {
    background_image: {
        url: url,
        alt: 'Initial Banner Home',
    },
    title: 'Forged Legacies:<br>Where Tradition Meets<br>MODERNITY',
};

const history1 = {
    image: {
        url: image1,
        alt: "Image History 1",
    },
    text: "Transform your living or workspace into a gallery of elegance and distinction with our exclusive collection of decorative ironwork.",
    button: {
        text: "CONTACT",
        link: "",
    }
}

const history2 = {
    image: {
        url: image2,
        alt: "Image History 2",
    },
    text: "Our portfolio includes bespoke gates, intricate grilles, elegant railings, and statement furniture, each designed to elevate the aesthetic of your environment.",
    button: {
        text: "ABOUT",
        link: "",
    }
}

const history3 = {
    image: {
        url: image3,
        alt: "Image History 3",
    },
    text: "Join us in redefining luxury and style with ironwork that's more than just decoration—it's a lifestyle.",
    button: {
        text: "ABOUT",
        link: "",
    }
}
</script>


<style scoped>
/* Estilos opcionales para el contenedor del carrusel */
.swiper-container {
  width: 100%;
  height: 300px; /* Ajusta la altura según tus necesidades */
}
</style>
