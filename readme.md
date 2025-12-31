# Interactive Math Blog

## Motivation
Blogs are boring. Things have changed we are close to AGI but, still the blogs are from ancient days with no quality of life improvement. So, I have made this repository as a framework or guideliness to create a new way of interactive blog. 

Specially for mathematics blog, it would be great if you could tweak the variable of a formula and see the result. It will help you see and test the edge cases. This was my main motivation.

## About the Project
This project uses modular architecture to help you create interactive blog instantly and here are its cool features;
- Supports markdown formatting, `dash` doesn't let you do so but I made this possible.
- Utility classes for styling that covers most of the portion so, you can make the site look cool. 
- Utility classes that are similar to that of TailWind CSS to help you catchup easier.
- You can create interactive sections in between with visualization through plotly.

## Tools Used
1. `dash` provides the Python to React feature,
2. `plotly` helps me to build interactive Graphs easily.

## Example Blog
I have created an example blog of visualizing LLM to let you know the truepotential of the interactive blog.

### Why GPT-2?
1. Simple architecture for understanding,
2. 124M parameter model that can run easily without the need of dedicated GPU,
3. First of its kind so, a good start to know where thing started.

### Scripts
### 3d Token Embeddings
To visualize the embeddings space of tokens, I used GPT-2 embedding matrix to create a lookup dictionary such that whenever user enters a token they can compare the similarlity in the vector space.

Here, to visualize the things better we have also converted the 768 dimensional vector space into 3-d space using PCA. This is to create a 3d plot using plotly and show that to the user.