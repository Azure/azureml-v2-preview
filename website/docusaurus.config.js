module.exports = {
  title: 'AMLv2',
  tagline: 'this website is under development',
  url: 'https://github.com/Azure/',
  baseUrl: '/azureml-v2-preview/',
  onBrokenLinks: 'ignore',
  favicon: 'img/logo.svg',
  organizationName: 'Azure', // Usually your GitHub org/user name.
  projectName: 'azureml-v2-preview', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'AMLv2',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          to: 'docs/userguide/',
          label: 'User Guide',
          position: 'left',
        },
        {
          href: 'https://github.com/Azure/azureml-v2-preview',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Documentation',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/Azure/azureml-v2-preview',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub (Issues)',
              href: 'https://github.com/Azure/azureml-v2-preview/issues',
            },
          ],
        },
        {
          title: 'Coming soon...',
          items: [
            {
              label: 'Blog',
              to: 'blog',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Microsoft`,
    },
    algolia: {
      apiKey: 'b12ff2d7b13980e0983244167d1c2450',
      indexName: 'azure',
      searchParameters: {},
      placeholder: 'Search'
    },
    googleAnalytics: {
      trackingID: 'G-2DKKZ26VP0',
    }
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/Azure/azureml-v2-preview/tree/main/website/',
        },
        cookbook: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/Azure/azureml-v2-preview/tree/main/website/blog',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
