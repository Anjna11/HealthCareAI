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

            <template v-slot:body-cell-actions="props">
              <q-td :props="props">
                <q-btn-dropdown
                  flat
                  dense
                  size="sm"
                  auto-close
                >
                  <q-list>
                    <q-item clickable v-close-popup @click="viewProfile(props.row)">
                      <q-item-section avatar><q-icon name="person" /></q-item-section>
                      <q-item-section>View Profile</q-item-section>
                    </q-item>
                  
                    <q-item clickable v-close-popup @click="makeAppointment(props.row)">
                      <q-item-section avatar><q-icon name="event" /></q-item-section>
                      <q-item-section>Appointment</q-item-section>
                    </q-item>
                  </q-list>
                </q-btn-dropdown>
              </q-td>
            </template>
            </q-table>


            <!-- View Profile Dialog -->
            <q-dialog v-model="showProfileDialog">
              <q-card style="min-width: 350px">
                <q-card-section class="text-h6">
                  Profile: {{ selectedPatient?.fname }} {{ selectedPatient?.lname }}
                </q-card-section>
              
                <q-card-section>
                  <div><strong>Gender:</strong> {{ selectedPatient?.gender }}</div>
                  <div><strong>DOB:</strong> {{ selectedPatient?.dob }}</div>
                </q-card-section>
              
                <q-card-actions align="right">
                  <q-btn flat label="Close" color="primary" v-close-popup />
                </q-card-actions>
              </q-card>
            </q-dialog>

            <!-- Appointment Dialog -->
            <q-dialog v-model="showAppointmentDialog">
              <q-card style="min-width: 300px">
                <q-card-section class="text-h6">
                  Patient Name: {{ selectedPatient?.fname }} {{ selectedPatient?.lname }}
                </q-card-section>
              
                <q-card-section>
                  <q-input label="Date And Time" outlined v-model="AppointmentStartDate"/>
                  <q-input label="Visit Type" outlined v-model="AppointmentVisitType" class="q-mt-sm" />
                </q-card-section>
              
                <q-card-actions align="right">
                  <q-btn flat label="Cancel" color="primary" v-close-popup />
                  <q-btn flat label="Confirm" color="primary" @click="confirmAppointment" />
                </q-card-actions>
              </q-card>
            </q-dialog>

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

const showProfileDialog = ref(false)
const showAppointmentDialog = ref(false)
const selectedPatient = ref(null)

const AppointmentStartDate = ref('')
const AppointmentVisitType = ref('')

const columns = [
  { name: 'patient_id', label: 'ID', field: 'patient_id', align: 'left' },
  { name: 'name', label: 'Name', field: row => `${row.fname} ${row.lname}`, align: 'left' },
  { name: 'gender', label: 'Gender', field: 'gender', align: 'center' },
  { name: 'dob', label: 'Date of Birth', field: 'dob', align: 'center' },
  { name: 'actions', label: '', align: 'center', align: 'right', sortable: false }
]

function GoToAddPatient() {
  router.push('/AddPatient')
}

function loadPatients() {
  axios.get('http://localhost:8000/patients')
    .then(res => {
      debugger;
      rows.value = res.data
    })
    .catch(err => {
      console.error('Error', err)
    })
}

function viewProfile(row) {
  selectedPatient.value = row
  showProfileDialog.value = true
}

function makeAppointment(row) {
  selectedPatient.value = row
  showAppointmentDialog.value = true
}

function confirmAppointment() {
  axios.post('http://localhost:8000/makeAppointment', {
    patient_id: selectedPatient.value.patient_id,
    visitType_id: parseInt(AppointmentVisitType.value),
    startTime: AppointmentStartDate.value
  })
  .then(() => {
    showAppointmentDialog.value = false
    AppointmentStartDate.value = ''
    AppointmentVisitType.value = ''
  })
  .catch(err => {
    console.error('Error creating appointment', err)
  })
}


onMounted(loadPatients)
</script>

