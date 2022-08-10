import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import myAcc from '../views/myAcc.vue'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'
 
import store from '@/store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path:'/:category_slug/:product_slug/',
    name:'Product',
    component:Product
  },
  {
    path:'/:category_slug/',
    name:'Category',
    component:Category
  },
  {
    path:'/search',
    name:'search',
    component:Search
  },
  {
    path:'/cart',
    name:'cart',
    component:Cart
  },
  {
    path:'/sign-up',
    name:'sign-up',
    component:SignUp
  },
  {
    path:'/log-in',
    name:'log-in',
    component:Login
  },
  {
    path:'/my-acc',
    name:'my-acc',
    component:myAcc,
    meta:{
      requireLogin:true
    }
  },
  {
    path:'/Checkout',
    name:'Checkout',
    component:Checkout,
    meta:{
      requireLogin:true
    }
  },
  {
    path:'/success',
    name:'success',
    component:Success,
    meta:{
      requireLogin:true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to,from,next)=>{
  if(to.matched.some(record=>record.meta.requireLogin) && !store.state.isAuthenticated){
    next({name:'log-in',query:{to:to.path}})
  }else{
    next()
  }
})

export default router
