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
import { ref } from 'vue'
const filter = ref('')

const columns = [
  { name: 'time', label: 'Visit Time', field: 'time', align: 'left' },
  { name: 'id', label: 'ID Number', field: 'id', align: 'left' },
  { name: 'name', label: 'Name', field: 'name', align: 'left' },
  { name: 'gender', label: 'Gender', field: 'gender', align: 'center' },
  { name: 'age', label: 'Age', field: 'age', align: 'center' },
  { name: 'visitType', label: 'Visit Type', field: 'visitType', align: 'left' }
]

const rows = [
  { time: 'Today, 12:37 PM', id: '1000DAW', name: 'Teju K', gender: 'F', age: 28, visitType: 'OPD Visit' },
  { time: 'Today, 06:57 AM', id: '1000C1H', name: 'CLARISSA YU', gender: 'F', age: 32, visitType: 'Facility Visit' },
  { time: 'Today, 03:59 AM', id: '1000AP4', name: 'Megha Sharma', gender: 'M', age: 34, visitType: 'Facility Visit' },
]
</script>