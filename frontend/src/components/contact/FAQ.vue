<template>
  <section id="accordion-collapse" data-accordion="collapse" class="flex flex-col items-center w-full pb-12">
    <h1 class="p-12 text-5xl">Frequently Asked Questions</h1>
    <FAQContent
      question="What makes Artisan Iron's products unique?"
      answer="Our products are unique due to the blend of traditional craftsmanship rooted in South American heritage and contemporary design sensibilities."
      headerId="accordion-collapse-heading-1"
      bodyId="accordion-collapse-body-1"
    ></FAQContent>

    <FAQContent
      question="How much does it cost?"
      answer="Our range of prices vary by design. You could be looking between $$$$ and $$$$ for most of our designs. Contact us to receive a quote on what you’re looking for."
      headerId="accordion-collapse-heading-2"
      bodyId="accordion-collapse-body-2"
    ></FAQContent>

    <FAQContent
      question="Where are Artisan Iron's products made?"
      answer="Our products are crafted in workshops located in South America, where our skilled artisans bring our designs to life."
      headerId="accordion-collapse-heading-3"
      bodyId="accordion-collapse-body-3"
    ></FAQContent>

    <FAQContent
      question="What materials are used in Artisan Iron's creations?"
      answer="We primarily use iron and bronze in our creations, both of which are meticulously shaped and crafted by our artisans."
      headerId="accordion-collapse-heading-4"
      bodyId="accordion-collapse-body-4"
    ></FAQContent>

    <FAQContent
      question="Can I request custom designs or modifications to existing pieces?"
      answer="Yes, we welcome custom design requests and modifications to existing pieces. Our team will work closely with you to bring your vision to life."
      headerId="accordion-collapse-heading-5"
      bodyId="accordion-collapse-body-5"
    ></FAQContent>

    <FAQContent
      question="How durable are Artisan Iron's products?"
      answer="Our products are crafted with the highest quality materials and techniques, ensuring durability and longevity for life."
      headerId="accordion-collapse-heading-6"
      bodyId="accordion-collapse-body-6"
    ></FAQContent>

    <FAQContent
      question="Is Artisan Iron committed to sustainability and ethical practices?"
      answer="Yes, we are committed to sustainability and positive social impact. We support the preservation of traditional arts and provide economic opportunities in South America."
      headerId="accordion-collapse-heading-7"
      bodyId="accordion-collapse-body-7"
    ></FAQContent>

    <FAQContent
      question="Do Artisan Iron's products require special maintenance?"
      answer="While our products are durable, we recommend occasional maintenance to preserve their beauty and integrity. Cleaning with a soft cloth and mild detergent is usually sufficient."
      headerId="accordion-collapse-heading-8"
      bodyId="accordion-collapse-body-8"
    ></FAQContent>

    <FAQContent
      question="What is the lead time for custom orders?"
      answer="Lead times for custom orders vary depending on the complexity of the design and current workshop capacity. Usually between 3-6 months total. Our team will provide you with an estimated timeline upon request."
      headerId="accordion-collapse-heading-9"
      bodyId="accordion-collapse-body-9"
    ></FAQContent>

    <FAQContent
      question="Does Artisan Iron offer installation services?"
      answer="Yes, we offer installation services for our products. Our team of experts will ensure that your piece is installed safely and securely, enhancing the beauty of your space."
      headerId="accordion-collapse-heading-10"
      bodyId="accordion-collapse-body-10"
    ></FAQContent>
  </section>
</template>

<script setup>
  import { onMounted } from 'vue';
  import { initFlowbite } from 'flowbite';
  import FAQContent from "@/components/contact/FAQContent.vue";

  onMounted(() => {
    initFlowbite();
  });
</script>
