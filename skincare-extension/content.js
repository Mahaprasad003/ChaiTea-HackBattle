function extractIngredients() {
  const ingredientSources = [
    () => {
      const productDescription = document.getElementById('productDescription');
      if (productDescription) {
        const text = productDescription.textContent;
        const match = text.match(/(?:Active )?Ingredients:(.+?)(?:\.|$)/i);
        return match ? match[1].trim() : null;
      }
      return null;
    },
    () => {
      const bulletPoints = document.querySelectorAll('#feature-bullets li');
      for (const bullet of bulletPoints) {
        if (bullet.textContent.toLowerCase().includes('ingredients')) {
          return bullet.textContent.replace(/^.*?:/i, '').trim();
        }
      }
      return null;
    },
    () => {
      const ingredientsSection = document.querySelector('.ingredients-section');
      return ingredientsSection ? ingredientsSection.textContent.trim() : null;
    },
    () => {
      const detailBullets = document.querySelectorAll('#detailBullets_feature_div li');
      for (const bullet of detailBullets) {
        if (bullet.textContent.toLowerCase().includes('ingredients')) {
          return bullet.querySelector('.a-list-item').textContent.split(':')[1].trim();
        }
      }
      return null;
    },
    () => {
      const productDetails = document.getElementById('productDetails_feature_div');
      if (productDetails) {
        const text = productDetails.textContent;
        const match = text.match(/(?:Active )?Ingredients:(.+?)(?:\n|$)/i);
        return match ? match[1].trim() : null;
      }
      return null;
    }
  ];

  for (const source of ingredientSources) {
    const ingredients = source();
    if (ingredients) {
      return ingredients.split(',').map(i => i.trim()).filter(i => i);
    }
  }

  return [];
}

function extractSkinType() {
  const productDescription = document.getElementById('productDescription');
  const bulletPoints = document.querySelectorAll('#feature-bullets li');
  const title = document.getElementById('productTitle');

  const textToSearch = [
    productDescription ? productDescription.textContent : '',
    ...Array.from(bulletPoints).map(bullet => bullet.textContent),
    title ? title.textContent : ''
  ].join(' ').toLowerCase();

  const skinTypes = ["normal", "oily", "dry", "sensitive", "combination"];
  return skinTypes.find(type => textToSearch.includes(type)) || 'Not specified';
}

function extractProductInfo() {
  const ingredients = extractIngredients();
  const skinType = extractSkinType();
  
  return { ingredients, skinType };
}

// Listen for messages from the popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'getProductInfo') {
    sendResponse(extractProductInfo());
  }
  return true;
});
