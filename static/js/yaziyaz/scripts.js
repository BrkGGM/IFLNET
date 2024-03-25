area.value = localStorage.getItem('yazi');
    area.oninput = () => {
      localStorage.setItem('yazi', area.value)
    };