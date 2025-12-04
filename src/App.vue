<script setup lang="ts">
import { ref } from 'vue'

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

// Les 3 piliers NIRD
const piliers = [
  {
    emoji: '🤝',
    title: 'Inclusion',
    description: 'Accès équitable au numérique et réduction de la fracture numérique pour tous les élèves',
    color: 'from-nird-purple to-nird-cyan'
  },
  {
    emoji: '🛡️',
    title: 'Responsabilité',
    description: 'Usage raisonné et réflexif de technologies souveraines et respectueuses des données personnelles',
    color: 'from-nird-cyan to-purple-600'
  },
  {
    emoji: '🌱',
    title: 'Durabilité',
    description: 'Lutte contre l\'obsolescence programmée par le choix de Linux, maîtrise des coûts et reconditionnement',
    color: 'from-purple-600 to-nird-purple'
  }
]

// Menu mobile toggle
const mobileMenuOpen = ref(false)
</script>

<template>
  <div class="min-h-screen bg-gradient-to-br from-nird-night via-slate-900 to-nird-night">
    
    <!-- Header / Navigation -->
    <header class="sticky top-0 z-50 backdrop-blur-lg bg-nird-night/80 border-b border-nird-purple/30">
      <nav class="container mx-auto px-4 py-4">
        <div class="flex items-center justify-between">
          
          <!-- Logo NIRD -->
          <div class="flex items-center space-x-3">
            <div class="w-12 h-12 bg-gradient-to-br from-nird-purple to-nird-yellow rounded-2xl flex items-center justify-center text-2xl font-bold shadow-lg shadow-nird-purple/50">
              🐝
            </div>
            <div>
              <h1 class="text-xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-nird-yellow to-nird-purple">
                NIRD
              </h1>
              <p class="text-xs text-gray-400">Village Numérique Résistant</p>
            </div>
          </div>

          <!-- Desktop Menu -->
          <div class="hidden lg:flex items-center space-x-1">
            <a 
              v-for="item in menuItems" 
              :key="item.label"
              :href="item.href"
              class="px-3 py-2 rounded-xl hover:bg-nird-purple/20 transition-all duration-300 flex items-center space-x-2 group"
            >
              <span class="text-lg group-hover:scale-125 transition-transform">{{ item.emoji }}</span>
              <span class="text-sm text-gray-300 group-hover:text-nird-yellow">{{ item.label }}</span>
            </a>
          </div>

          <!-- Mobile Menu Button -->
          <button 
            @click="mobileMenuOpen = !mobileMenuOpen"
            class="lg:hidden p-2 rounded-xl bg-nird-purple/20 hover:bg-nird-purple/40 transition-all"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>

        <!-- Mobile Menu Dropdown -->
        <div v-if="mobileMenuOpen" class="lg:hidden mt-4 space-y-2">
          <a 
            v-for="item in menuItems" 
            :key="item.label"
            :href="item.href"
            class="block px-4 py-3 rounded-xl bg-nird-purple/10 hover:bg-nird-purple/20 transition-all flex items-center space-x-3"
            @click="mobileMenuOpen = false"
          >
            <span class="text-xl">{{ item.emoji }}</span>
            <span class="text-sm">{{ item.label }}</span>
          </a>
        </div>
      </nav>
    </header>

    <!-- Hero Section -->
    <section id="accueil" class="container mx-auto px-4 py-16 md:py-24">
      <div class="text-center max-w-4xl mx-auto">
        
        <!-- Badge "Initiative d'en bas" -->
        <div class="inline-flex items-center space-x-2 px-4 py-2 bg-nird-purple/20 border border-nird-purple/50 rounded-full mb-8">
          <span class="text-2xl">✊</span>
          <span class="text-sm text-nird-yellow font-medium">Initiative spontanée • Communauté enseignante</span>
        </div>

        <!-- Titre principal -->
        <h2 class="text-5xl md:text-6xl font-bold mb-6 leading-tight">
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-nird-yellow via-nird-purple to-nird-cyan">
            Numérique Libre
          </span>
          <br />
          <span class="text-white">& Écocitoyen</span>
        </h2>

        <!-- Sous-titre -->
        <p class="text-xl md:text-2xl text-gray-300 mb-8 leading-relaxed">
          Pour un numérique <strong class="text-nird-yellow">Inclusif</strong>, 
          <strong class="text-nird-purple">Responsable</strong> et 
          <strong class="text-nird-cyan">Durable</strong> dans les établissements scolaires
        </p>

        <!-- Description contextuelle -->
        <div class="bg-gradient-to-r from-nird-purple/10 via-purple-900/20 to-nird-purple/10 rounded-3xl p-8 mb-8 border border-nird-purple/30">
          <p class="text-gray-200 leading-relaxed mb-4">
            À l'heure où la fin du support de Windows 10 nous rappelle notre dépendance technologique et nous oblige à faire des choix, 
            un collectif enseignant issu de la <strong>Forge des communs numériques éducatifs</strong> invite les établissements scolaires 
            et les collectivités qui les accompagnent à s'engager progressivement vers un Numérique qui soit davantage Inclusif, Responsable et Durable.
          </p>
          <p class="text-gray-300 text-sm">
            🎯 Rejoignez la démarche NIRD et participez à la construction d'un <strong class="text-nird-yellow">village numérique résistant</strong> !
          </p>
        </div>

        <!-- CTA Buttons -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <a 
            href="https://edurl.fr/tchap-laforgeedu-nird" 
            target="_blank"
            class="px-8 py-4 bg-gradient-to-r from-nird-purple to-nird-cyan rounded-2xl font-semibold text-white shadow-xl shadow-nird-purple/50 hover:shadow-2xl hover:shadow-nird-purple/70 hover:scale-105 transition-all duration-300"
          >
            💬 Rejoindre la communauté Tchap
          </a>
          <a 
            href="#demarche"
            class="px-8 py-4 bg-nird-night border-2 border-nird-yellow rounded-2xl font-semibold text-nird-yellow hover:bg-nird-yellow hover:text-nird-night transition-all duration-300"
          >
            📚 Découvrir la démarche
          </a>
        </div>
      </div>
    </section>

    <!-- Les 3 Piliers NIRD -->
    <section id="piliers" class="container mx-auto px-4 py-16">
      <div class="text-center mb-12">
        <h3 class="text-4xl font-bold text-white mb-4">Les 3 Piliers NIRD</h3>
        <p class="text-gray-400">Au carrefour de la transformation numérique et de la transition écologique</p>
      </div>

      <div class="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
        <div 
          v-for="pilier in piliers" 
          :key="pilier.title"
          class="group relative bg-gradient-to-br from-slate-800/50 to-slate-900/50 backdrop-blur-sm rounded-3xl p-8 border border-nird-purple/30 hover:border-nird-yellow/50 transition-all duration-500 hover:scale-105 hover:shadow-2xl hover:shadow-nird-purple/30 float-animation"
        >
          <!-- Icon -->
          <div 
            class="w-20 h-20 mx-auto mb-6 rounded-2xl flex items-center justify-center text-4xl shadow-lg group-hover:scale-110 transition-transform duration-500"
            :class="`bg-gradient-to-br ${pilier.color}`"
          >
            {{ pilier.emoji }}
          </div>

          <!-- Title -->
          <h4 class="text-2xl font-bold text-white mb-4 text-center">
            {{ pilier.title }}
          </h4>

          <!-- Description -->
          <p class="text-gray-300 text-center leading-relaxed">
            {{ pilier.description }}
          </p>

          <!-- Decorative gradient overlay on hover -->
          <div 
            class="absolute inset-0 rounded-3xl opacity-0 group-hover:opacity-10 transition-opacity duration-500"
            :class="`bg-gradient-to-br ${pilier.color}`"
          ></div>
        </div>
      </div>
    </section>

    <!-- Section Résistance Numérique -->
    <section id="resistance" class="container mx-auto px-4 py-16">
      <div class="max-w-5xl mx-auto">
        
        <!-- Header avec métaphore Astérix -->
        <div class="text-center mb-12">
          <div class="inline-flex items-center space-x-3 px-6 py-3 bg-gradient-to-r from-nird-purple/20 to-purple-900/20 rounded-full mb-6 border border-nird-purple/50">
            <span class="text-3xl">🛡️</span>
            <span class="text-lg font-semibold text-nird-yellow">David contre Goliath</span>
            <span class="text-3xl">⚔️</span>
          </div>
          
          <h3 class="text-4xl md:text-5xl font-bold text-white mb-4">
            Le Village Numérique Résistant
          </h3>
          <p class="text-xl text-gray-300">
            Comment les établissements scolaires peuvent tenir tête aux Big Tech
          </p>
        </div>

        <!-- Le problème : Goliath numérique -->
        <div class="bg-gradient-to-br from-red-900/20 to-slate-900/50 rounded-3xl p-8 mb-8 border-2 border-red-500/30">
          <div class="flex items-start space-x-4">
            <div>
              <h4 class="text-2xl font-bold text-red-400 mb-4">L'Empire numérique nous impose...</h4>
              <ul class="space-y-3 text-gray-300">
                <li class="flex items-start space-x-3">
                  <span class="text-red-400 flex-shrink-0">❌</span>
                  <span><strong>Obsolescence programmée</strong> : matériel rendu obsolète alors qu'il fonctionne encore</span>
                </li>
                <li class="flex items-start space-x-3">
                  <span class="text-red-400 flex-shrink-0">❌</span>
                  <span><strong>Licences coûteuses</strong> : abonnements indispensables qui pèsent sur les budgets publics</span>
                </li>
                <li class="flex items-start space-x-3">
                  <span class="text-red-400 flex-shrink-0">❌</span>
                  <span><strong>Données hors UE</strong> : stockage dans des clouds étrangers sans souveraineté</span>
                </li>
                <li class="flex items-start space-x-3">
                  <span class="text-red-400 flex-shrink-0">❌</span>
                  <span><strong>Écosystèmes fermés</strong> : dépendance structurelle aux Big Tech</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- La solution : Village résistant -->
        <div class="bg-gradient-to-br from-green-900/20 to-slate-900/50 rounded-3xl p-8 border-2 border-nird-yellow/50">
          <div class="flex items-start space-x-4">
            <div>
              <h4 class="text-2xl font-bold text-nird-yellow mb-4">L'École devient un village résistant !</h4>
              <p class="text-gray-300 mb-6 leading-relaxed">
                À l'image du célèbre village d'Astérix, l'École peut devenir un <strong>village résistant, ingénieux, autonome et créatif</strong>. 
                La démarche NIRD redonne du <strong class="text-nird-yellow">pouvoir d'agir</strong> aux équipes éducatives en renforçant leur 
                <strong class="text-nird-purple">autonomie technologique</strong>.
              </p>
              
              <div class="grid md:grid-cols-2 gap-4">
                <div class="bg-nird-purple/10 rounded-xl p-4 border border-nird-purple/30">
                  <div class="text-2xl mb-2">🐧</div>
                  <h5 class="font-semibold text-nird-yellow mb-2">Linux & Logiciels Libres</h5>
                  <p class="text-sm text-gray-400">Lutte contre l'obsolescence et maîtrise de nos outils</p>
                </div>
                
                <div class="bg-nird-purple/10 rounded-xl p-4 border border-nird-purple/30">
                  <div class="text-2xl mb-2">♻️</div>
                  <h5 class="font-semibold text-nird-yellow mb-2">Reconditionnement</h5>
                  <p class="text-sm text-gray-400">Donner une seconde vie au matériel avec les élèves</p>
                </div>
                
                <div class="bg-nird-purple/10 rounded-xl p-4 border border-nird-purple/30">
                  <div class="text-2xl mb-2">🤝</div>
                  <h5 class="font-semibold text-nird-yellow mb-2">Communauté & Partage</h5>
                  <p class="text-sm text-gray-400">Mutualisation des ressources et solutions ouvertes</p>
                </div>
                
                <div class="bg-nird-purple/10 rounded-xl p-4 border border-nird-purple/30">
                  <div class="text-2xl mb-2">🎓</div>
                  <h5 class="font-semibold text-nird-yellow mb-2">Pédagogie Active</h5>
                  <p class="text-sm text-gray-400">Sensibilisation et projets avec les éco-délégués</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Citation inspirante -->
        <div class="mt-8 text-center">
          <p class="text-lg italic text-gray-400">
            "Une initiative <strong class="text-nird-purple">d'en bas</strong> pour montrer 
            <strong class="text-nird-yellow">en haut</strong> qu'il y a urgence à agir."
          </p>
        </div>
      </div>
    </section>

    <!-- Section Origine & Lycée Carnot -->
    <section id="origine" class="container mx-auto px-4 py-16">
      <div class="max-w-4xl mx-auto bg-gradient-to-br from-nird-purple/10 to-slate-900/50 rounded-3xl p-10 border border-nird-purple/30">
        <div class="flex items-start space-x-6">
          <div>
            <h3 class="text-3xl font-bold text-white mb-4">
              Né au Lycée Carnot de Bruay-la-Buissière
            </h3>
            <p class="text-gray-300 leading-relaxed mb-6">
              Le projet NIRD est né au <strong class="text-nird-yellow">lycée Carnot</strong> dans les Hauts-de-France. 
              Cette expérience réussie démontre qu'il est possible de construire un numérique éducatif plus autonome, 
              plus durable, plus éthique. La démarche NIRD cherche maintenant à <strong class="text-nird-purple">faire essaimer</strong> 
              ce modèle vers un maximum d'établissements scolaires français.
            </p>
            <p class="text-sm text-gray-400 mb-4">
              🎯 Objectif : passer à l'échelle et fédérer les initiatives existantes
            </p>
            
            <!-- Statut actuel -->
            <div class="bg-amber-900/20 border border-amber-500/30 rounded-xl p-4">
              <p class="text-amber-300 text-sm">
                ⚠️ <strong>Cette démarche n'a pas encore de reconnaissance officielle.</strong> 
                Elle provient du terrain et est dictée par un sentiment d'urgence. Rien ne pourra se faire à terme 
                sans la mobilisation de nombreux acteurs et le soutien de l'institution.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FutureHiddenGame: Snake will go here -->
    <!-- 
      🎮 Future Easter Egg Zone:
      Ici sera implémenté un jeu Snake caché, activable par un konami code ou une combinaison de touches.
      Le Snake pourrait être thématisé NIRD avec des pixels qui "mangent" des logos Big Tech.
    -->

    <!-- Footer -->
    <footer class="container mx-auto px-4 py-12 border-t border-nird-purple/30 mt-16">
      <div class="text-center">
        <div class="flex justify-center items-center space-x-3 mb-6">
          <div class="w-10 h-10 bg-gradient-to-br from-nird-purple to-nird-yellow rounded-xl flex items-center justify-center text-xl">
            🐝
          </div>
          <span class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-nird-yellow to-nird-purple">
            NIRD
          </span>
        </div>
        
        <p class="text-gray-400 mb-4">
          Démarche portée par un collectif enseignant de la Forge des communs numériques éducatifs
        </p>
        
        <div class="flex flex-wrap justify-center gap-6 text-sm text-gray-500">
          <a href="https://nird.forge.apps.education.fr/" target="_blank" class="hover:text-nird-yellow transition-colors">
            🌐 Site officiel
          </a>
          <a href="https://edurl.fr/tchap-laforgeedu-nird" target="_blank" class="hover:text-nird-yellow transition-colors">
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

<style scoped>
/* Animations supplémentaires si besoin */
</style>

