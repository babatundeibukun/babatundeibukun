document.addEventListener("DOMContentLoaded", () => {
  const params = new URLSearchParams(window.location.search);
  const projectId = params.get("id");

  const project = projects.find(p => p.id === projectId);
  if (project) {
    document.getElementById("project-title").textContent = project.title;
    document.getElementById("project-image").src = project.image;
    document.getElementById("project-description").textContent = project.description;

    const detailsList = document.getElementById("project-details");
    project.details.forEach(detail => {
      const li = document.createElement("li");
      li.textContent = detail;
      detailsList.appendChild(li);
    });

    // Add visit link dynamically
    const visitLink = document.getElementById("visit-link");
    visitLink.href = project.link || "#";
    visitLink.style.display = project.link ? "inline-block" : "none";
  } else {
    document.querySelector("main").innerHTML = `<h1>Project Not Found</h1>`;
  }
});
