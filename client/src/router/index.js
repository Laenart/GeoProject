import Vue from 'vue';
import Router from 'vue-router';
import GeoPoint from '@/components/GeoPoint';
import Parks from '@/components/Parks';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Parks',
      component: Parks,
    },
    {
      path: '/ping',
      name: 'GeoPoint',
      component: GeoPoint,
    },
  ],
  mode: 'history',
}

);

