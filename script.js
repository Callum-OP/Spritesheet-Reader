const output = document.getElementById('output');
const input = document.getElementById('json');

// Listener to wait until a file has been entered, then read it when it has been entered
input.addEventListener('change', event => {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = function(e) {
    const content = e.target.result;
    const data = JSON.parse(content);
    output.innerHTML = ''; // Clear previous output
    readCoordinates(data); // Send json data to function
  };
  reader.readAsText(file);
});

// Function to read spritesheet coordinates, giving the start and end frames
function readCoordinates(data) {
  const animations = {};

  let frames = [];

  // Check the format of the data to see how it should be read then get the frames in each
  if (data.textures?.[0]?.frames) {
    // Texture-based (an example would be json from Texture Atlas Generator)
    frames = data.textures[0].frames.map(f => ({
      filename: f.filename,
      frame: f.frame
    }));
  } else if (data.frames) {
    // Frames-based (an example would be json from the free Texture Packer Online)
    frames = Object.entries(data.frames).map(([filename, frameData]) => ({
      filename,
      frame: frameData.frame
    }));
  }

  // Go through each frame in the file and get coordinates for each
  frames.forEach(({ filename, frame }) => {
    const match = filename.match(/^([A-Za-z]+)([A-Za-z]*)(\d+)?/);
    // Match any groups (frames with same name but different number)
    if (match) {
      const prefix = match[1] + match[2];
      const number = match[3] ? parseInt(match[3], 10) : 0;
      if (!animations[prefix]) animations[prefix] = [];
      animations[prefix].push({ number, frame });
    }
  });

  // Get the output element in html and clear current output
  const output = document.getElementById('output');
  output.innerHTML = '';

  // Display each group if frames showing the start and end coordinates for each
  Object.entries(animations).forEach(([anim, coords]) => {
    const sorted = coords.sort((a, b) => a.number - b.number);
    const start = sorted[0].frame;
    const end = sorted[sorted.length - 1].frame;
    const line = `${anim}XStart = ${start.x}; ${anim}YStart = ${start.y}; ${anim}XEnd = ${end.x}; ${anim}YEnd = ${end.y};`;
    const p = document.createElement('p');
    p.textContent = line;
    output.appendChild(p); // Print to html element
    console.log(line); // Print to console
  });
}
