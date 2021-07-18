<template>
  <div>
    <div class="container">
      <button type="button" class="btn btn-primary">{{ msg }}</button>
    </div>
  </div>
</template>

<script>
import { HTTP } from '../api/common'

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      HTTP.get('ping')
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
