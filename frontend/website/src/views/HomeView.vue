<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome To Djackets</p>
        <p class="subtitle">The Best jacket Store Online</p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import axios from "axios";
import ProductBox from "@/components/ProductBox.vue";

export default {
  name: "HomeView",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    ProductBox,
    
  },
  mounted() {
    this.getlatestProduct();
  },

  methods: {
    async getlatestProduct() {
      await axios
        .get("/api/v1/latest-products")
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
         
        });
    },
  },
};
</script>

 
