const cube = document.querySelector('.cube');
    document.querySelectorAll('navss a').forEach(link => {
      link.addEventListener('click', () => {
        const face = link.dataset.face;
        cube.className = 'cube show-' + face;
      });
    });
