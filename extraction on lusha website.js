function download(filename, text) {
    const element = document.createElement("a");
    element.setAttribute(
      "href",
      "data:text/plain;charset=utf-8," + encodeURIComponent(text)
    );
    element.setAttribute("download", filename);
    element.style.display = "none";
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  }
   function extractNamesAndNavigate() {
    const names = Array.from(
      document.querySelectorAll('a[href*="/business/"]')
    )
      .map((a) => a.textContent)
      .join("\n");
    const currentPage = parseInt(
      document.querySelector(".page-numbers.current").textContent
    );
    download(`names_page_${currentPage}.txt`, names);
  }
   extractNamesAndNavigate();