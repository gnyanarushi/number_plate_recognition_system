document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.getElementById("file-upload");
  const previewImg = document.getElementById("preview-img");
  const fileName = document.getElementById("file-name");

  if (!fileInput) return;

  fileInput.addEventListener("change", function (e) {
    const file = e.target.files && e.target.files[0];
    if (!file) {
      fileName.textContent = "No file chosen";
      previewImg.style.display = "none";
      previewImg.src = "";
      return;
    }

    fileName.textContent = file.name;

    if (!file.type.startsWith("image/")) {
      previewImg.style.display = "none";
      previewImg.src = "";
      return;
    }

    const reader = new FileReader();
    reader.onload = function (ev) {
      previewImg.src = ev.target.result;
      previewImg.style.display = "inline-block";
    };
    reader.readAsDataURL(file);
  });
});
