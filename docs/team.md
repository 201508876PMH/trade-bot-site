---
layout: page
---
<script setup>
import {
  VPTeamPage,
  VPTeamPageTitle,
  VPTeamMembers,
  VPTeamPageSection
} from 'vitepress/theme'

const coreMembers = [
  {
    avatar: 'https://avatars.githubusercontent.com/u/38226095?v=4',
    name: 'Anton',
    title: 'MSc, Civil Engineer in Computer Technology, (Developer)',
    links: [
      { icon: 'github', link: 'https://github.com/antonercool' }
    ]
  },
  {
    avatar: 'https://avatars.githubusercontent.com/u/42763743?v=4',
    name: 'Peter',
    title: 'MSc, Civil Engineer in Computer Technology, (Infrastructure & devOps)',
    links: [
      { icon: 'github', link: 'https://github.com/201508876PMH' }
    ]
  },
  {
    avatar: 'https://avatars.githubusercontent.com/u/32189116?v=4',
    name: 'Johannes',
    title: 'MSc, Cand.scient.oecon, (Analytics, performance and math)',
    links: [
      { icon: 'github', link: 'https://github.com/Meltrox' }
    ]
  }
]
const partners = [
    {
    avatar: 'https://raw.githubusercontent.com/201508876PMH/trade-bot-site/06bc01a97f078199a42bc09644369ed43761296a/public/images/candlestick.svg',
    name: 'Hans Kristian',
    title: 'Crypto, stocks & trading',
  }
]
</script>

<VPTeamPage>
  <VPTeamPageTitle>
    <template #title>Our Team</template>
    <template #lead> The development of T-BOTs is guided by a mixed team of friends, some of whom have chosen to be featured below.</template>
  </VPTeamPageTitle>
  <VPTeamMembers size="medium" :members="coreMembers" />
  <VPTeamPageSection>
    <template #title>Partners</template>
    <template #lead> Trusted collaborators and advisors who have contributed valuable insights, tools, and support to the T-BOTs project.
</template>
    <template #members>
      <VPTeamMembers size="small" :members="partners" />
    </template>
  </VPTeamPageSection>
</VPTeamPage>