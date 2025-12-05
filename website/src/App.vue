<script setup lang="ts">
import { ref, useTemplateRef } from 'vue';
import SnakeInput from './components/SnakeInput.vue';

const mainElem = useTemplateRef("view")
const snakeInputModel = ref("")

// Menu items avec emojis
const menuItems = [
  { emoji: '🐝', label: 'Accueil', href: '#accueil' },
  { emoji: '🚸', label: 'Démarche', href: '#demarche' },
  { emoji: '🏫', label: 'Pilotes', href: '#pilotes' },
  { emoji: '🐧', label: 'Linux', href: '#linux' },
  { emoji: '🧰', label: 'Boîte à outils', href: '#outils' },
  { emoji: '♻️', label: 'Reconditionnement', href: '#reconditionnement' },
  { emoji: '🏛️', label: 'Collectivités', href: '#collectivites' },
  { emoji: '❓', label: 'Pourquoi', href: '#pourquoi' },
]

// Menu mobile toggle
const mobileMenuOpen = ref(false)
</script>

<template>
  <div class="min-h-screen bg-gradient-to-bl from-nird-night via-nird-night to-nird-night">
    <!-- Header / Navigation -->
    <header class="sticky top-0 z-50 backdrop-blur-lg bg-nird-night/80 border-b border-nird-purple/30">
      <nav class="container mx-auto px-4 py-4">
        <div class="flex items-center justify-between">

          <!-- Logo NIRD -->
          <div class="flex items-center space-x-3">
            <div
              class="w-12 h-12 bg-gradient-to-br from-nird-purple to-nird-yellow rounded-2xl flex items-center justify-center text-2xl font-bold shadow-lg shadow-nird-purple/50">
              🐝
            </div>
            <div>
              <h1
                class="text-xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-nird-yellow to-nird-purple">
                NIRD
              </h1>
              <p class="text-xs text-gray-400">Village Numérique Résistant</p>
            </div>
          </div>

          <!-- Desktop Menu -->
          <div class="hidden lg:flex items-center space-x-1">
            <a v-for="item in menuItems" :key="item.label" :href="item.href"
              class="px-3 py-2 rounded-xl hover:bg-nird-purple/20 transition-all duration-300 flex items-center space-x-2 group">
              <span class="text-lg group-hover:scale-125 transition-transform">{{ item.emoji }}</span>
              <span class="text-sm text-gray-300 group-hover:text-nird-yellow">{{ item.label }}</span>
            </a>
          </div>

          <!-- Mobile Menu Button -->
          <button @click="mobileMenuOpen = !mobileMenuOpen"
            class="lg:hidden p-2 rounded-xl bg-nird-purple/20 hover:bg-nird-purple/40 transition-all">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>

        <!-- Mobile Menu Dropdown -->
        <div v-if="mobileMenuOpen" class="lg:hidden mt-4 space-y-2">
          <a v-for="item in menuItems" :key="item.label" :href="item.href"
            class="block px-4 py-3 rounded-xl bg-nird-purple/10 hover:bg-nird-purple/20 transition-all flex items-center space-x-3"
            @click="mobileMenuOpen = false">
            <span class="text-xl">{{ item.emoji }}</span>
            <span class="text-sm">{{ item.label }}</span>
          </a>
        </div>
      </nav>
    </header>

    <main ref="view">
      <SnakeInput v-if="mainElem !== null" :ref-elem="mainElem!" v-model="snakeInputModel" />
      <div v-if="snakeInputModel.length" class="w-screen flex flex-col mt-3 p-2 bg-slate-400">
        <p class="mx-auto">Snake input:</p>
        <input readonly class="mx-auto rounded-sm bg-slate-200 text-slate-800" type="text" :value="snakeInputModel" />
      </div>

      <RouterView />
    </main>

    <!-- Footer -->
    <footer class="container mx-auto px-4 py-12 border-t border-nird-purple/30 mt-16">
      <div class="text-center">
        <div class="flex justify-center items-center space-x-3 mb-6">
          <div
            class="w-10 h-10 bg-gradient-to-br from-nird-purple to-nird-yellow rounded-xl flex items-center justify-center text-xl">
            🐝
          </div>
          <span
            class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-nird-yellow to-nird-purple">
            NIRD
          </span>
        </div>

        <p class="text-gray-400 mb-4">
          Démarche portée par un collectif enseignant de la Forge des communs numériques éducatifs
        </p>

        <div class="flex flex-wrap justify-center gap-6 text-sm text-gray-500">
          <a href="https://nird.forge.apps.education.fr/" target="_blank"
            class="hover:text-nird-yellow transition-colors">
            🌐 Site officiel
          </a>
          <a href="https://edurl.fr/tchap-laforgeedu-nird" target="_blank"
            class="hover:text-nird-yellow transition-colors">
            💬 Forum Tchap
          </a>
          <span>🆓 Licence Libre</span>
          <span>🇫🇷 Made with ❤️ pour l'Éducation</span>
        </div>

        <p class="text-xs text-gray-600 mt-8">
          Projet minimal créé pour La Nuit de l'Info 2025
        </p>
      </div>
    </footer>
  </div>
</template>
