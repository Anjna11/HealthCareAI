<template>
    <div class="q-pa-md flex flex-center" style="height: 65vh;">
      <div style="width: 730px; text-align: left;">
        <div class="text-h6 q-mb-md">Basic Info</div>
  
        <!-- Name Fields -->
        <q-input filled v-model="firstName" label="First Name" class="q-mb-md" />
        <q-input filled v-model="lastName" label="Last Name" class="q-mb-md" />
  
        <!-- gender -->
        <div class="text-subtitle2 q-mb-sm">Gender</div>
        <q-option-group
          v-model="gender"
          :options="genderList"
          type="radio"
          inline
          class="q-mb-md"
        />
  
        <!-- Date of Birth -->
        <div class="text-subtitle2 q-mb-sm">Date of Birth</div>
        <q-input
          filled
          v-model="dob"
          label="Date of Birth"
          mask="##/##/####"
          placeholder="dd/mm/yyyy"
          class="q-mb-md"
        />
  
        <!-- Identifier Info -->
        <div class="text-subtitle2 q-mt-md">Identifiers</div>
        <div class="text-caption">Dr.Asist: <span class="text-primary">Auto-generated</span></div>
  
        <!-- Actions -->
        <div class="q-mt-lg">
          <q-btn label="Register" style="background-color: #0e3d56; color: white" class="q-mr-sm" @click="register"/>
        </div>
      </div>
    </div>
  </template>
  
<script setup>
import { ref } from 'vue'
import axios from 'axios'

const firstName = ref('')
const lastName = ref('')
const gender = ref('')
const dob = ref('')

const genderList = [
  { label: 'Male', value: 'M' },
  { label: 'Female', value: 'F' },
  { label: 'Other', value: 'O' },
  { label: 'Unknown', value: 'U' }
]

function register(){
    axios.post('http://localhost:8000/register', {
        fname: firstName.value,
        lname:lastName.value,
        gender: gender.value,
        dob:dob.value
    })
}

</script>
  