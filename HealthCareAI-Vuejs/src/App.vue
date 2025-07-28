<template>
    <q-layout view="lHh Lpr lFf">
      <!-- Header -->
      <q-header elevated class="fancy-header">
        <q-toolbar class="q-px-md q-gutter-sm">
          <q-icon name="healing" size="30px" class="text-white q-mr-sm" />
          <div class="brand-wrapper">
            <div class="header-title">Dr.<span class="accent">Assist</span></div>
            <div class="header-tagline">Your AI-Powered Health Companion</div>
          </div>
          <q-space />
          <q-btn flat round dense icon="settings" style="margin-top: 20px;" />
        </q-toolbar>
      </q-header>

      <!-- Page content -->
      <q-page-container>
        <q-page class="row q-col-gutter-md">

          <!-- Sidebar -->
          <div class="col-12 col-md-2">
            <q-card class="sidebar-white sidebar-no-scroll q-pa-sm q-mb-md">
              <q-list>
                <q-item clickable v-ripple @click="GoToHome">
                  <q-item-section avatar>
                    <q-icon name="home" class="text-sidebar" />
                  </q-item-section>
                  <q-item-section class="sidebar-text-shadow text-dark">Home</q-item-section>
                </q-item>

                <q-item clickable v-ripple @click="GoToPatientList">
                  <q-item-section avatar>
                    <q-icon name="people" class="text-sidebar" />
                  </q-item-section>
                  <q-item-section class="sidebar-text-shadow text-dark">Patient List</q-item-section>
                </q-item>
              </q-list>
            </q-card>
          </div>

          <div class="col-12 col-md-10">
            <router-view />
          </div>

        </q-page>
      </q-page-container>
    </q-layout>
</template>

<script setup>
import '/mnt/anjna/workspace/Workspace/HealthCareAI/HealthCareAI-Vuejs/src/assets/app.css'
import { useRouter } from 'vue-router'

const router = useRouter()

function GoToHome() {
  router.push('/Home')
}

function GoToPatientList() {
  router.push('/PatientList')
}
</script>

  
