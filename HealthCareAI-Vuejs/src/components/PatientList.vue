<template>
  <q-page-container>
    <q-page>
      <div>
        <q-card>
          <q-card-section>
            <div style="display: flex; align-items: center; justify-content: space-between;">
              <div class="text-h6">Patients</div>
              <q-btn
                style="border-radius: 5px;"
                label="Patient"
                icon="person_add"
                unelevated
                class="q-px-md hover-color"
                @click="GoToAddPatient"
              />
            </div>
          </q-card-section>

          <q-separator />

          <q-card-section>
            <q-input
              dense
              outlined
              placeholder="Filter table"
              v-model="filter"
              style="flex: 1;"
            />

            <q-table
              :rows="rows"
              :columns="columns"
              row-key="id"
              :filter="filter"
              flat
            >
            </q-table>

          </q-card-section>
        </q-card>
      </div>
    </q-page>
  </q-page-container>
</template>

<script setup>
import '/mnt/anjna/workspace/Workspace/HealthCareAI/HealthCareAI-Vuejs/src/assets/app.css'
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const router = useRouter()
const filter = ref('')
const rows = ref([])


const columns = [
  { name: 'id', label: 'ID', field: 'id', align: 'left' },
  { name: 'name', label: 'Name', field: row => `${row.fname} ${row.lname}`, align: 'left' },
  { name: 'gender', label: 'Gender', field: 'gender', align: 'center' },
  { name: 'dob', label: 'Date of Birth', field: 'dob', align: 'center' }
]

function GoToAddPatient() {
  router.push('/AddPatient')
}

function loadPatients() {
  axios.get('http://localhost:8000/patients')
    .then(res => {
      rows.value = res.data
    })
    .catch(err => {
      console.error('Error', err)
    })
}


onMounted(loadPatients)
</script>

