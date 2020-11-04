module.exports = {
  userguide:{
    'User Guide': [
      {
        type: 'doc',
        id: 'userguide/README'
      },
      {
        type: 'category',
        label: 'Overview',
        collapsed: false,
        items: ['userguide/overview', 'userguide/studio', 'userguide/architecture']
      },
      {
        type: 'category',
        label: 'Concepts',
        collapsed: false,
        items: ['userguide/workspace', 'userguide/job', 'userguide/endpoint', 'userguide/data', 'userguide/compute', 'userguide/model']
      }
    ],
  }
};
