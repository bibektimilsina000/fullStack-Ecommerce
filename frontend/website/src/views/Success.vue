<template>
  <div class="page-success">
    <div class="columns is-miltiline">
      <div class="column is-12">
        <h1 class="title">Thank You</h1>
        <p>Your Order will be processed within 48 hours</p>
      </div>
    </div>
    <div class>
      <router-link to="my-acc">
        <button class="buttton is-primary">View Order</button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Success",
  mounted() {
    document.title = "success|WebsiteName";
  },
 


  beforeCreate() {
    this.$store.commit("clearCart");
  },
};
</script>

<style></style>
