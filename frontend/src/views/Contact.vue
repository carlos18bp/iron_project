<template>
  <Header></Header>
  <section>
    <InitialBanner :data="initialBannerData"></InitialBanner>
  </section>

  <section id="goToDownContact" class="flex mt-10">
    <Form></Form>
    <div class="mt-8 p-8">
      <p class="uppercase text-2xl pb-4">Contact</p>
      <p class="uppercase text-1xl">Showroom</p>
      <p class="text-lg">4457 Main St</p>
      <p class="text-lg">Philadelphia, PA 19127</p>
      <p class="text-lg pt-4">Phone: 215.483.9273</p>
      <p class="text-lg">Hours: Monday to Friday: 9-5pm</p>
    </div>
  </section>

  <FAQ></FAQ>
  <section class="flex justify-center p-8">
    <CallToAction
      text="Contact us now"
    ></CallToAction>
  </section>
  <Footer></Footer>
</template>

<script setup>
  import Header from "@/components/layouts/Header.vue";
  import Footer from "@/components/layouts/Footer.vue";
  import CallToAction from "@/components/layouts/CallToAction.vue";
  import InitialBanner from "@/components/layouts/InitialBanner.vue";
  import url from "@/assets/images/initialBanners/Contact.jpeg";
  import Form from "@/components/contact/Form.vue";
  import FAQ from "@/components/contact/FAQ.vue";

  const initialBannerData = {
    background_image: {
      url: url,
      alt: "Initial Banner Contact",
    },
    title: "Tell Us About Your<br>Project",
    classes: "text-black",
    goToId: 'goToDownContact'
  };
</script>
