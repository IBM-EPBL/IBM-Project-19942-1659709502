document.addEventListener("DOMContentLoaded", (event) => {
  if (
    document.querySelector("div#b>b").textContent ==
    "The Loan status is approved"
  ) {
    document.querySelector("div#pic>img").src = "./static/images/accepted";
  } else {
    document.querySelector("div#pic>img").src = "./static/images/rejected.jpeg";
  }
});
