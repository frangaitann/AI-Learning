<div align="center">
  <h2>LangChain</h2>
  <br>
  <p>Chain & Pipeline style system, a lineal running with more control, nice for big but solid data (No dyanmic data or dynamic execution)</p>
</div>

<div>
  <h2 align="center">Pros</h2>
  <br>
  <ul>
    <li>Allows human-in-the-midle-loops (Decisions that might be made by a supervisor human due to a difficult situation)</li>
    <li>More control over the running & the output</li>
    <li>Better & simplier structure than LangGraph</li>
    <li>Better for pre-agent or pre-model running scripts</li>
    <li>Not necessary to make our own embedding system for chat cache, it has it's own memorysaverfunc()</li>
    <li>Works Nicely with MCP Servers</li>
  </ul>
</div>

<div align="center">
  <h2>Cons</h2>
  <br>
  <ul>
    <li>No dynamic data or runflows (might semi-dynamic due to first iteration tool using)</li>
    <li>More difficult than OpenRouter API or others due to it's amplied structure</li>
    <li>Complex for debugging if making non-linear agent.</li>
  </ul>
</div>

<div align="center">
  <h2>Examples</h2>
  <br>
  <p>Data Manager that sends data to different runtimes using APIs with predictable data and no dynamic ever-different data.</p>
</div>