<template>
  <Header></Header>
  <section>
    <InitialBanner :data="initialBannerData"></InitialBanner>
  </section>

  <section id="goToDownContact" class="flex mt-10">
    <Form></Form>
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
