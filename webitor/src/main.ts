import "./style.css";

document.querySelector<HTMLDivElement>("#app")!.innerHTML = `
  <div>
    <h1 id="title">Webitor</h1>
    <textarea id="code" placeholder="Paste your code here: "></textarea>
    <button id="copy">Translate my code</button>
  </div>
`;
