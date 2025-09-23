const form = document.getElementById("summary-form");
const output = document.getElementById("output");

form.addEventListener("submit", async function(e) {
  e.preventDefault();
  output.innerHTML = "";

  const formData = new FormData(form);
  const response = await fetch("/stream", { method: "POST", body: formData });
  const reader = response.body.getReader();
  const decoder = new TextDecoder("utf-8");

  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });
    const blocks = buffer.split(/\n{2,}/);
    buffer = blocks.pop();

    blocks.forEach(block => {
      const trimmed = block.trim();
      if (trimmed) output.innerHTML += marked.parse(trimmed);
    });

    output.scrollTop = output.scrollHeight;
  }

  if (buffer.trim()) {
    output.innerHTML += marked.parse(buffer.trim());
  }
});
