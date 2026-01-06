// Data Loading Logic
let currentScenario = null;

async function loadScenario(scenarioName) {
  try {
    const fileName = `/data/${scenarioName.toLowerCase()}_scenario.json`;
    const response = await fetch(fileName);
    if (!response.ok) throw new Error(`Failed to fetch ${fileName}`);
    currentScenario = await response.json();
    console.log(`✅ Scenario Loaded: ${scenarioName}`, currentScenario);

    // Dispatch event so other components know data is ready
    window.dispatchEvent(new CustomEvent('scenario-ready', {
      detail: { name: scenarioName, data: currentScenario }
    }));
    return currentScenario;
  } catch (err) {
    console.error('❌ Data Initialization Error:', err);
  }
}

// Global exposure
window.switchScenario = loadScenario;
window.getCurrentScenario = () => currentScenario;

// Scanner Transition Logic
function triggerScanner(callback) {
  const beam = document.getElementById('scanner-beam');
  if (!beam) return;
  beam.style.animation = 'none';
  beam.offsetHeight; /* trigger reflow */
  beam.style.animation = 'scan-wipe 1s ease-in-out forwards';
}

// Post-Mission Report Modal
window.openReport = (videoTitle) => {
  const scenario = currentScenario;
  const accuracy = scenario ? (scenario.metadata.accuracy * 100).toFixed(1) + '%' : '83%';
  const neutralized = scenario ? scenario.metadata.cancer_cells : '200';
  const healthy = scenario ? scenario.metadata.healthy_cells : '400';

  const modal = document.getElementById('report-modal');
  if (modal) {
    document.getElementById('report-title').textContent = `MISSION REPORT: ${videoTitle}`;
    document.getElementById('report-neutralized').textContent = `${neutralized}/${neutralized} (CLEARED)`;
    document.getElementById('report-preserved').textContent = healthy;
    document.getElementById('report-accuracy').textContent = accuracy;
    modal.style.display = 'flex';
  } else {
    // Fallback for pages without the modal (like index.html if called)
    alert(`MISSION: ${videoTitle}\nACCURACY: ${accuracy}\nSTATUS: SUCCESS`);
  }
}

window.closeReport = () => {
    const modal = document.getElementById('report-modal');
    if (modal) modal.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', () => {
  // Load default scenario (Blood) for index/global state
  loadScenario('blood');
  triggerScanner();
});
