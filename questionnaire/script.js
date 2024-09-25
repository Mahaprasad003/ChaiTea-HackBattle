document.getElementById("submit-btn").addEventListener("click", function() {
    let responses = {
      q1: document.querySelector('input[name="q1"]:checked')?.value,
      q2: document.querySelector('input[name="q2"]:checked')?.value,
      q3: document.querySelector('input[name="q3"]:checked')?.value,
      q4: document.querySelector('input[name="q4"]:checked')?.value
    };
  
    let skinType = "";
  
    if (responses.q1 === "oily" && responses.q2 === "often") {
      skinType = "Oily";
    } else if (responses.q1 === "dry" && responses.q2 === "rarely") {
      skinType = "Dry";
    } else {
      skinType = "Combination";
    }
  
    document.getElementById("result").innerHTML = "Your skin type is: " + skinType;
  });
  