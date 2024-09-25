document.addEventListener('DOMContentLoaded', function() {
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, {action: 'getProductInfo'}, function(response) {
      if (response) {
        displayProductInfo(response);
      }
    });
  });
});

function displayProductInfo(info) {
  const ingredientsList = document.getElementById('ingredients');
  const skinTypeElement = document.getElementById('skinType');

  ingredientsList.innerHTML = '';
  info.ingredients.forEach(ingredient => {
    const li = document.createElement('li');
    li.textContent = ingredient;
    ingredientsList.appendChild(li);
  });

  skinTypeElement.textContent = info.skinType;
}
