<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Парки</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" @click="onFillPark()">Заполнить</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
            <th scope="col">#</th>
              <th scope="col">Latitude</th>
              <th scope="col">Longitude</th>
              <th scope="col">Distance</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(park, index) in parks" :key="index">
                <td>{{ (index+1) }}</td>
                <td>{{ park.Latitude }}</td>
                <td>{{ park.Longitude }}</td>
                <td>{{ park.Distance }}</td>
              <td>
                <button type="button"
                        class="btn btn-danger btn-sm"
                        @click="onDeletePark(park)">
                    x
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { HTTP } from '../api/common'

export default {
  data() {
    return {
      parks: [],
    };
  },
  methods: {
    getParks() {
        HTTP.get('/parks')
            .then((res) => {
            this.parks = res.data.parks;
            })
            .catch((error) =>
            {
            console.error(error);
            });
    },
      fillParks() {
        HTTP.put('/parks').then(() => {
                this.getParks();
            })
            .catch((error) =>
            {
            console.error(error);
            });
    },
    removePark(park_id) {
        const params = JSON.stringify({ park_id: park_id });
        HTTP.delete('/parks', {
            data: {  park_id: park_id}
        })
            .then(() => {
                this.getParks();
            })
            .catch((error) => {
                console.error(error);
            });

        },
    onDeletePark(park) {
        this.removePark(park.Id);
        },
      onFillPark() {
        this.fillParks();
        },
  },
  created() {
    this.getParks();
  },
};
</script>
