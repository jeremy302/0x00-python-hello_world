$(
  () => {
    const ul = $('ul');
    $('DIV#add_item').on('click', () => ul.append('<li>item</li>'));
    $('DIV#remove_item').on('click', () => {
      const children = ul.children();
      if (children.length) { children[children.length - 1].remove(); }
    }
    );
    $('DIV#clear_list').on('click', () => ul.children().remove());
  }
);
