document.addEventListener('DOMContentLoaded', () => {
    const starContainer = document.createElement('div');
    starContainer.classList.add('stars');
    document.body.appendChild(starContainer);

    function createStar() {
        const star = document.createElement('div');
        star.classList.add('star');

        // Устанавливаем случайные размеры и позицию
        const size = Math.random() * 3 + 1; // Размер звезды от 1 до 4px
        star.style.width = size + 'px';
        star.style.height = size + 'px';
        star.style.position = 'absolute';
        star.style.top = Math.random() * window.innerHeight + 'px'; // Случайная позиция по вертикали
        star.style.left = Math.random() * window.innerWidth + 'px'; // Случайная позиция по горизонтали
        star.style.backgroundColor = '#fff';
        star.style.borderRadius = '50%';
        star.style.opacity = 0; // Начнем с полной прозрачности

        // Задержка перед появлением и исчезновением
        const delay = Math.random() * 2 + 1; // Случайная задержка перед анимацией

        // Плавное появление и исчезновение
        star.style.animation = `fadeInOut ${delay}s ease-in-out infinite`;

        // Добавляем звезду в контейнер
        starContainer.appendChild(star);

        // Через несколько секунд удаляем звезду
        setTimeout(() => {
            star.remove();
        }, delay * 1000); // Удаляем звезду после завершения анимации
    }

    setInterval(createStar, 25);
});

// Добавляем стили для анимации в head
const style = document.createElement('style');
style.innerHTML = `
    @keyframes fadeInOut {
        0% {
            opacity: 0;
            transform: scale(0);
        }
        50% {
            opacity: 1;
            transform: scale(1);
        }
        100% {
            opacity: 0;
            transform: scale(0);
        }
    }
`;
document.head.appendChild(style);