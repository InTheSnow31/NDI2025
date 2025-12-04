<script setup lang="ts">
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
</script>

<template>
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
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-nird-cyan via-nird-purple to-nird-yellow">
            Numérique Libre
          </span>
          <br />
          <span class="text-white">& Écocitoyen</span>
        </h2>

        <!-- Sous-titre -->
        <p class="text-xl md:text-2xl text-gray-300 mb-8 leading-relaxed">
          Pour un numérique <strong class="text-nird-cyan">Inclusif</strong>, 
          <strong class="text-nird-purple">Responsable</strong> et 
          <strong class="text-nird-yellow">Durable</strong> dans les établissements scolaires
        </p>

        <!-- Description contextuelle -->
        <div class="bg-gradient-to-r from-nird-purple/10 via-purple-900/20 to-nird-purple/10 rounded-3xl p-8 mb-8 border border-nird-purple/30">
          <p class="text-lg text-gray-200 leading-relaxed mb-4">
            À l'heure où la fin du support de Windows 10 nous rappelle notre dépendance technologique et nous oblige à faire des choix, 
            un collectif enseignant issu de la <strong>Forge des communs numériques éducatifs</strong> invite les établissements scolaires 
            et les collectivités qui les accompagnent à s'engager progressivement vers un Numérique qui soit davantage Inclusif, Responsable et Durable.
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
        <h3 class="text-4xl font-bold text-white mb-4">Les 3 Piliers 
          <strong class="text-transparent bg-clip-text bg-gradient-to-r from-nird-cyan via-nird-purple to-nird-yellow">NIRD</strong>
        </h3>
        <p class="text-lg text-gray-400">Au carrefour de la transformation numérique et de la transition écologique</p>
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
          <p class="text-lg text-gray-300 text-center leading-relaxed">
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
      <div class="text-center mb-12">
        <h3 class="text-4xl font-bold text-white mb-4"><strong class="text-nird-yellow">David</strong> contre <strong class="text-nird-purple">Goliath</strong></h3>
        <p class="text-lg text-gray-400">Le Village Numérique Résistant</p>
      </div>
      <div class="max-w-5xl mx-auto">

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
      </div>
    </section>

    <!-- Section Origine & Lycée Carnot -->
    <section id="origine" class="container mx-auto px-4 py-16">
      <div class="text-center mb-12">
        <h3 class="text-4xl font-bold text-white mb-4">L'origine du projet</h3>
        <p class="text-lg text-gray-400">Au Cœur des Hauts-de-France</p>
      </div>

      <div class="max-w-4xl mx-auto bg-gradient-to-br from-nird-purple/10 to-slate-900/50 rounded-3xl p-10 border border-nird-purple/30">
        <div class="flex items-start space-x-6">
          <div>
            <h3 class="text-3xl font-bold text-white mb-4">
              Né au Lycée Carnot de Bruay-la-Buissière
            </h3>
            <p class="text-lg text-gray-300 leading-relaxed mb-6">
              Le projet NIRD est né au <strong class="text-nird-yellow">lycée Carnot</strong> dans les Hauts-de-France. 
              Cette expérience réussie démontre qu'il est possible de construire un numérique éducatif plus autonome, 
              plus durable, plus éthique. La démarche NIRD cherche maintenant à <strong class="text-nird-purple">faire essaimer</strong> 
              ce modèle vers un maximum d'établissements scolaires français.
            </p>
            
            <!-- Statut actuel -->
            <div class="bg-amber-900/20 border border-amber-500/30 rounded-xl p-4">
              <p class="text-amber-300 text-base">
                ⚠️ <strong>Cette démarche n'a pas encore de reconnaissance officielle.</strong> 
                Elle provient du terrain et est dictée par un sentiment d'urgence. Rien ne pourra se faire à terme 
                sans la mobilisation de nombreux acteurs et le soutien de l'institution.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
</template>

<style scoped>
/* Animations supplémentaires si besoin */
</style>