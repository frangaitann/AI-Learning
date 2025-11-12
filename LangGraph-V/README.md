<div align="center">
  <h2>LangGraph</h2>
  <br>
  <p>The more complex structure, used for very unpredictable input or unpredictable data working, where Model takes input, works with it across many iterations (Not just 1 like in LangChain & OpenRouter) and it returns the output when it determines that is the expected answer. Works with Nodes & Edges instead of Chains of process. The main difference between ´´Graph and ´´Chain is that Chain is better for more linear runnings like simple RAG systems where the process must be the same or similar each run, while Graph works better for not-known situations (Where a Bot can be called for A the first time but for Z the second time, where A ≠ Z.)</p>
</div>

<div>
  <h2 align="center">Pros</h2>
  <br>
  <ul>
    <li>Full dynamic data working.</li>
    <li>More customizable running, best option for MoE systems manager, working-with MCP servers agents and multiple tools at the same time</li>
    <li>Returns the expected output (it "detects" if the output is correct, if it's not it iterates over a tool again until it reaches the expected output)</li>
    <li>Doesn't need changes if we change the LLM model, just model="new_model_name"</li>
  </ul>
</div>

<div align="center">
  <h2>Cons</h2>
  <br>
  <ul>
    <li>More complex structure</li>
    <li>Not easy for beginners</li>
    <li>Needs to understand about neural networks working</li>
    <li>Needs to understand LangChain first, it uses some of it's content for working</li>
    <li>Linear RAG works the same as in LangChain & needs more coding, understanding & Hardware computing (Not noticeable but exists)</li>
  </ul>
</div>

<div align="center">
  <h2>Examples</h2>
  <br>
  <p>A MoE manager agent / A Contact Support ChatBot AI with multiple options & uses / MultiModal self-made agent</p>
</div>