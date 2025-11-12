<div align="center">
  <h2>OpenRouter (Simple APIs)</h2>
  <br>
  <p>Rigid pipeline, 0 dynamic running due to being the most simple, full control over running & output, better for simple chatbots, introduction to AI development or SLM without too complex external tools</p>
</div>

<div>
  <h2 align="center">Pros</h2>
  <br>
  <ul>
    <li>Full control over running & output.</li>
    <li>The best for simple structures, totally better than LangChain & LangGraph</li>
    <li>Nice for simple chatbots or SLM</li>
    <li>Doesn't need changes if we change the LLM model, just model="new_model_name"</li>
  </ul>
</div>

<div align="center">
  <h2>Cons</h2>
  <br>
  <ul>
    <li>0 Dynamic data, it's impossible to handle with multiple iterations situation with just 1 agent</li>
    <li>Doesn't works with MCP Servers</li>
    <li>New middleware that could fail on running</li>
    <li>Needs your own chat cache system & chat embedding system (for avoiding waste of tokens or non coherence due to too much tokens)</li>
    <li>Can't decide for pre-agent/model running scripts</li>
    <li>RAG can be made but with too much limitations & difficult debug and integration</li>
    <li>tools can be added but they're too limited and are more difficult to add than on LangChain or LangGraph (Needs to be defined in a raw JSON)</li>
  </ul>
</div>

<div align="center">
  <h2>Examples</h2>
  <br>
  <p>A simple chatbot for a mobile app. / A very simple SLM for a MoE system</p>
</div>