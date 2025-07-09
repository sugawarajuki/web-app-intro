document.addEventListener('DOMContentLoaded', () => {
    const trainingList = document.getElementById('training-list');
    const addTrainingForm = document.getElementById('add-training-form');
    const exerciseInput = document.getElementById('exercise');
    const setsInput = document.getElementById('sets');
    const repsInput = document.getElementById('reps');
    const weightInput = document.getElementById('weight');
    const dateInput = document.getElementById('date');
    const notesInput = document.getElementById('notes');

    // 保存用配列
    let trainings = [];

    // 保存内容を表示
    function renderTrainings() {
        trainingList.innerHTML = '';
        trainings.forEach((item) => {
            const li = document.createElement('li');
            li.textContent = `種目: ${item.exercise}, セット数: ${item.sets}, 回数: ${item.reps}, 重量: ${item.weight}kg, 日付: ${item.date}, メモ: ${item.notes}`;
            trainingList.appendChild(li);
        });
    }

    // フォーム送信イベント
    addTrainingForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const exercise = exerciseInput.value.trim();
        const sets = setsInput.value;
        const reps = repsInput.value;
        const weight = weightInput.value;
        const date = dateInput.value;
        const notes = notesInput.value.trim();

        if (exercise && sets && reps && weight && date) {
            trainings.push({ exercise, sets, reps, weight, date, notes });
            renderTrainings();

            // 入力リセット
            exerciseInput.value = '';
            setsInput.value = '';
            repsInput.value = '';
            weightInput.value = '';
            dateInput.value = '';
            notesInput.value = '';
        }
    });

    // 初期表示
    renderTrainings();
});
