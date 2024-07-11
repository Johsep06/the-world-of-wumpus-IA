const rangeInput = document.getElementById('size');
const rangeValue = document.getElementById('size-value');

function updateRangeValue() {
    rangeValue.textContent = rangeInput.value;
}

rangeInput.addEventListener('input', updateRangeValue);

updateRangeValue();