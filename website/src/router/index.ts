import { createRouter, createWebHistory } from "vue-router";
import DefiNational from "../views/DefiNational.vue";

const DEFAULT_TITLE = "NDI2025";

const routes = [
  {
    path: "/",
    name: "Accueil",
    component: DefiNational,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.afterEach((to) => {
  document.title =
    Object.keys(to.params).length === 0
      ? DEFAULT_TITLE
      : `${DEFAULT_TITLE} | ${String(to.name)}`;
});

export { router };
