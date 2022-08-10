<template>
  <div class="page-checkout">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Checkout</h1>
      </div>

      <div class="column is-12 box">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="item in cart.items" v-bind:key="item.product.id">
              <td>{{ item.product.name }}</td>
              <td>${{ item.product.price }}</td>
              <td>{{ item.quantity }}</td>
              <td>${{ getItemTotal(item).toFixed(2) }}</td>
            </tr>
          </tbody>

          <tfoot>
            <tr>
              <td colspan="2">Total</td>
              <td>{{ cartTotalLength }}</td>
              <td>${{ cartTotalPrice.toFixed(2) }}</td>
            </tr>
          </tfoot>
        </table>
      </div>

      <div class="column is-12 box">
        <h2 class="subtitle">Shipping details</h2>

        <p class="has-text-grey mb-4">* All fields are required</p>

        <div class="columns is-multiline">
          <div class="column is-6">
            <div class="field">
              <label>First name*</label>
              <div class="control">
                <input type="text" class="input" v-model="first_name" />
              </div>
            </div>

            <div class="field">
              <label>Last name*</label>
              <div class="control">
                <input type="text" class="input" v-model="last_name" />
              </div>
            </div>

            <div class="field">
              <label>E-mail*</label>
              <div class="control">
                <input type="email" class="input" v-model="email" />
              </div>
            </div>

            <div class="field">
              <label>Phone*</label>
              <div class="control">
                <input type="text" class="input" v-model="phone" />
              </div>
            </div>
          </div>

          <div class="column is-6">
            <div class="field">
              <label>Address*</label>
              <div class="control">
                <input type="text" class="input" v-model="address" />
              </div>
            </div>

            <div class="field">
              <label>Zip code*</label>
              <div class="control">
                <input type="text" class="input" v-model="zipcode" />
              </div>
            </div>

            <div class="field">
              <label>Place*</label>
              <div class="control">
                <input type="text" class="input" v-model="place" />
              </div>
            </div>
          </div>
        </div>

        <div class="notification is-danger mt-4" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>

        <hr />

        <div id="card-element" class="mb-5"></div>

        <template v-if="cartTotalLength">
          <hr />

          <button
            class="button is-dark"
            v-on:click="cashdelv = true"
            @click="submitForm"
            
          >
            Pay with cash
          </button>
          <button
            class="button is-dark"
             v-on:click="esewa = true"
            @click="submitForm"
           
          >
            Pay with Esewa
          </button>
        </template>
        <button class="button is-dark" @click="edata">check items</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Checkout",
  data() {
    return {
      //esewa data

      esewa: false,
      cashdelv: false,
      path: "https://uat.esewa.com.np/epay/main",
      params: {
        amt: 0,
        psc: 0,
        pdc: 0,
        txAmt: 0,
        tAmt: 0,
        pid: "",
        scd: "EPAYTEST",
        su: "http://",
        fu: "http://merchant.com.np/page/esewa_payment_failed",
      },
      //esewa data

      cart: {
        items: [],
      },
      first_name: "",
      last_name: "",
      email: "",
      phone: "",
      address: "",
      zipcode: "",
      place: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Checkout | Djackets";

    this.cart = this.$store.state.cart;
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    submitForm() {
      this.errors = [];

      if (this.first_name === "") {
        this.errors.push("The first name field is missing!");
      }

      if (this.last_name === "") {
        this.errors.push("The last name field is missing!");
      }

      if (this.email === "") {
        this.errors.push("The email field is missing!");
      }

      if (this.phone === "") {
        this.errors.push("The phone field is missing!");
      }

      if (this.address === "") {
        this.errors.push("The address field is missing!");
      }

      if (this.zipcode === "") {
        this.errors.push("The zip code field is missing!");
      }

      if (this.place === "") {
        this.errors.push("The place field is missing!");
      }

      if (!this.errors.length) {
        this.submmit();
      }
    },
    async submmit() {
      const items = [];

      for (let i = 0; i < this.cart.items.length; i++) {
        const item = this.cart.items[i];
        const obj = {
          product: item.product.id,
          quantity: item.quantity,
          price: item.product.price * item.quantity,
        };

        items.push(obj);
      }

      const data = {
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
        address: this.address,
        zipcode: this.zipcode,
        place: this.place,
        phone: this.phone,
        items: items,
      };
      const token = localStorage.getItem("token");
      const headers = {
        Authorization: `Token ${token}`,
      };

      await axios
        .post("/api/v1/checkout/", data, { headers })
        .then((response) => {
          if (this.esewa) {
            this.edata();
            this.epay(this.path, this.params);
          }
          if (this.cashdelv) {
            this.$store.commit("clearCart");
            this.$router.push("/success");
          }
        })
        .catch((error) => {
          this.errors.push("Something went wrong. Please try again");

           
        });
    },

    epay(path, params) {
      var form = document.createElement("form");
      form.setAttribute("method", "POST");
      form.setAttribute("action", path);

      for (var key in params) {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);
        form.appendChild(hiddenField);
      }

      document.body.appendChild(form);
      form.submit();
    },

    edata() {
      const items = [];

      for (let i = 0; i < this.cart.items.length; i++) {
        const item = this.cart.items[i];
        const obj = {
          product: item.product.id,
          quantity: item.quantity,
          price: item.product.price * item.quantity,
        };

        items.push(obj);
      }

      let price = items[0].price;
      let id = items[0].product;

       
      this.params.amt = price;

      this.params.pid = id;

      let productServiceCharge = 0;
      this.params.psc = productServiceCharge;

      let productDeliveryCharge = 0;
      this.params.pdc = productDeliveryCharge;

      let taxAmount = 0;
      this.params.txAmt = taxAmount;

      this.params.tAmt = 0;
      this.params.tAmt =
        price + productServiceCharge + productDeliveryCharge + taxAmount;
    },
  },
  computed: {
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.product.price * curVal.quantity);
      }, 0);
    },
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },
  },
};
</script>
