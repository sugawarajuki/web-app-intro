document.addEventListener('DOMContentLoaded', () => {
    const trainingList = document.getElementById('training-list');
    const addTrainingForm = document.getElementById('add-training-form');
    const exerciseInput = document.getElementById('exercise');
    const setsInput = document.getElementById('sets');
    const repsInput = document.getElementById('reps');

    // 保存用配列
    let trainings = [];

    // 保存内容を表示
    function renderTrainings() {
        trainingList.innerHTML = '';
        trainings.forEach((item, idx) => {
            const li = document.createElement('li');
            li.textContent = `種目: ${item.exercise}, セット数: ${item.sets}, 回数: ${item.reps}`;
            trainingList.appendChild(li);
        });
    }

    // フォーム送信イベント
    addTrainingForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const exercise = exerciseInput.value.trim();
        const sets = setsInput.value;
        const reps = repsInput.value;

        if (exercise && sets && reps) {
            trainings.push({ exercise, sets, reps });
            renderTrainings();
            exerciseInput.value = '';
            setsInput.value = '';
            repsInput.value = '';
        }
    });

    renderTrainings();
});