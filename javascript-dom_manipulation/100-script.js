document.addEventListener('DOMContentLoaded', function () {
  const addBtn = document.querySelector('#add_item');
  const removeBtn = document.querySelector('#remove_item');
  const clearBtn = document.querySelector('#clear_list');
  const list = document.querySelector('.my_list');

  // Add item
  addBtn.addEventListener('click', function () {
    const li = document.createElement('li');
    li.textContent = 'Item';
    list.appendChild(li);
  });

  // Remove last item
  removeBtn.addEventListener('click', function () {
    if (list.lastElementChild) {
      list.removeChild(list.lastElementChild);
    }
  });

  // Clear all items
  clearBtn.addEventListener('click', function () {
    list.innerHTML = '';
  });
});
