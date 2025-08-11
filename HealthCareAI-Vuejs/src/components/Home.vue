<template>
    <q-page-container>
        <q-page>
            <!-- Main Content -->
            <div>

              <!-- Info Cards -->
              <div class="row q-col-gutter-md q-mb-md">
                <div class="col-12 col-sm-4">
                  <q-card>
                    <q-card-section>
                      <div class="text-h6">Active Visits</div>
                      <div class="text-caption text-grey">Patients</div>
                      <div class="text-h4 text-primary">68</div>
                    </q-card-section>
                  </q-card>
                </div>

                <div class="col-12 col-sm-4">
                  <q-card>
                    <q-card-section>
                      <div class="text-h6">Total Visits Today</div>
                      <div class="text-caption text-grey">Patients</div>
                      <div class="text-h4 text-primary">0</div>
                    </q-card-section>
                  </q-card>
                </div>

                <div class="col-12 col-sm-4">
                  <q-card>
                    <q-card-section>
                      <div class="text-h6">Scheduled For Today</div>
                      <div class="text-caption text-grey">Patients</div>
                      <div class="text-h4 text-primary">0</div>
                    </q-card-section>
                  </q-card>
                </div>
              </div>

              <!-- Table -->
              <q-card>
                <q-card-section class="text-h6 q-pb-none">Active Visits</q-card-section>
                <q-separator />
                <q-card-section>
                  <q-input dense  placeholder="Filter table" outlined v-model="filter" class="q-mb-md" />
                  <q-table
                    :rows="rows"
                    :columns="columns"
                    row-key="id"
                    :filter="filter"
                    flat
                  />
                </q-card-section>
              </q-card>
            </div>
        </q-page>
      </q-page-container>
    
</template>

<script setup>
import '/mnt/anjna/workspace/Workspace/HealthCareAI/HealthCareAI-Vuejs/src/assets/app.css' 
import { ref, onMounted } from 'vue'
import axios from 'axios'
const filter = ref('')

const rows = ref([])
const columns = [
  { name: 'patient_id', label: 'ID', field: 'patient_id', align: 'left' },
  { name: 'name', label: 'Name', field: row => `${row.fname} ${row.lname}`, align: 'left' },
  { name: 'gender', label: 'Gender', field: 'gender', align: 'center' },
  { name: 'dob', label: 'Date of Birth', field: 'dob', align: 'center' },
  { name: 'Visit_name', label: 'Visit Type', field: 'Visit_name', align: 'left' },
  { name: 'actions', label: '', align: 'center', align: 'right', sortable: false }
]

function loadPatients() {
  axios.get('http://localhost:8000/activePatients')
    .then(res => {
      rows.value = res.data
    })
    .catch(err => {
      console.error('Error', err)
    })
}

onMounted(loadPatients)
</script>