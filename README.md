# WebWeaver - 2D Game Engine

**WebWeaver** is a lightweight and high-performance 2D fighting game engine designed specifically for browser-based games. By leveraging cutting-edge web technologies like **WebAssembly (WASM)** and **WebGL/WebGL2**, WebWeaver ensures smooth and responsive gameplay experiences directly in the browser.

## Features

### 1. WASM-Powered Performance
WebWeaver harnesses the power of **WebAssembly** (WASM) to run high-performance code at near-native speed, ensuring that games run efficiently even on resource-constrained systems. WASM allows the engine to execute complex game logic and physics calculations with minimal overhead, providing an optimal experience without sacrificing performance.

### 2. High-Quality Graphics with WebGL/WebGL2
Utilizing **WebGL** and **WebGL2**, WebWeaver takes full advantage of the GPU for rendering, enabling visually stunning 2D graphics at high frame rates. This allows the engine to handle complex animations, particle effects, and shaders while maintaining smooth performance across different browsers and devices.

### 3. Cross-Platform and Browser-Based
As a browser-based engine, WebWeaver supports seamless cross-platform compatibility. Whether your players are on desktops, laptops, or mobile devices, your games will run smoothly in any modern browser without requiring any additional installations or plugins.

### 4. Optimized for 2D Fighting Games
WebWeaver is purpose-built for the fast-paced and action-packed nature of 2D fighting games. Its architecture is optimized for responsive input handling, low-latency networking, and frame-perfect precision, which are critical for competitive play.

### 5. Modular and Customizable
The engine is designed to be modular and easily customizable, allowing developers to modify or extend core functionalities to suit their unique game mechanics and features. The modularity enables the inclusion of custom shaders, animations, physics, or UI elements with minimal hassle.

## How It Works

- **WebAssembly (WASM)**: Provides high-speed execution of game logic and processing-heavy tasks by compiling Rust code into a binary format that runs efficiently in the browser. (Note that rust is used out of the box, but any programming language compiled to wasm will work)
  
- **WebGL/WebGL2**: Handles the rendering pipeline, providing hardware-accelerated 2D graphics to achieve smooth visuals and animations. WebGL2 offers additional features like improved shader support and higher precision for advanced visual effects.

- **JavaScript Integration**: The engine uses JavaScript for high-level game logic and communication with WASM modules. This combination ensures both ease of development and high performance.

## Contributors:

 - Marco A. Gomez - @dr-gomez