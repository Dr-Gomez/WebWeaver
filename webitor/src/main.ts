import "./style.css";
import typescriptLogo from "./typescript.svg";
import Compiler from "./compiler.ts";

document.querySelector<HTMLDivElement>("#app")!.innerHTML = `
  <div>
    <h1 id="title">Webitor</h1>
    <textarea id="code" placeholder="Paste your code here: "></textarea>
    <button id="copy">Translate my code</button>
  </div>
`;

const compiler = new Compiler();
