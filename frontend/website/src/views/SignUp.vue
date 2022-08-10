<template>
  <div class="page-sign-up">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign up</h1>

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
                v-model="username"
              />
            </div>
          </div>

          <div class="field">
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
          </div>

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

          <div class="field">
            <label for="">Repeat Password</label>
            <div class="control">
              <input
                required
                type="password"
                name=""
                id="re-password"
                class="input"
                v-model="password2"
              />
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-dark">Sign Up</button>
            </div>
          </div>
          <hr />
          <div class="field">
            <div class="control">
              <button class="button is-primary">Sign Up with google</button>
            </div>
            <hr />
            Or <router-link to="log-in">Click Here </router-link> to log in!
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
  name: "SignUp",

  data() {
    return {
      username: "",
      email: "",
      password: "",
      password2: "",
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      this.errors = [];
      if (password.length < 8) {
        this.errors.push("Enter a secure password");
      }
      if (this.password !== this.password2) {
        this.errors.push("The password doen't match");
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          email: this.email,
          password: this.password,
        };
        await axios
          .post("/api/v1/users/", formData)
          .then((response) => {
            toast({
              message: "Account created successfully , please log in ! ",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });

            this.$router.push("/log-in");
          })

          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}:${error.response.data[property]}`
                );
              }
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");
            }
          });
      }
    },
  },
};
</script>

<style></style>
