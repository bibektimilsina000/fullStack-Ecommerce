<template>
  <div class="page-sign-up">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Log in</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="">Username</label>
            <div class="control">
              <input
                type="text"
                required
                name=""
                id="username"
                class="input"
                placeholder="Enter username or email"
                v-model="username"
              />
            </div>
          </div>

          <!-- <div class="field">
            <label for="">Email</label>
            <div class="control">
              <input
                type="email"
                required
                name=""
                id="email"
                class="input"
                v-model="email"
              />
            </div>
          </div> -->

          <div class="field">
            <label for="">Password</label>
            <div class="control">
              <input
                required
                type="password"
                name=""
                id="password"
                class="input"
                v-model="password"
              />
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-dark">Log in</button>
            </div>
          </div>
          <hr>
          <div class="field">
            <div class="control">
              <button class="button is-primary">Sign Up with google </button>
            </div>
          </div>
          <hr />
          Or <router-link to="sign-up">Click Here </router-link> to sign up!
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },

  mounted() {
    document.title = "Log in | Websitename";
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      const formData = {
        username: this.username,
        password: this.password,
      };

      await axios
        .post("/api/v1/token/login/", formData)
        .then((response) => {
          const token = response.data.auth_token;
          this.$store.commit("setToken", token);
          axios.defaults.headers.common["Authorization"] = "Token" + token;
          localStorage.setItem("token", token);
          const toPath = this.$route.query.to || "/cart";
          this.$router.push(toPath);
        })

        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}:${error.response.data[property]}`);
            }
          } else {
            this.errors.push("Something went wrong. Please try again");
          }
        });
    },
  },
};
</script>

<style></style>
