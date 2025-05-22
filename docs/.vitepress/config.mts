import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: '/trade-bot-site/',
  title: "BOTArmy",
  description: "A VitePress Site",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: 'https://raw.githubusercontent.com/201508876PMH/trade-bot-site/master/docs/images/robot.svg',
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Strategies', link: '/bbscalper' }
    ],

    sidebar: [
      {
        text: 'Strategies',
        items: [
          { text: 'BBScalper', link: '/bbscalper' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})

