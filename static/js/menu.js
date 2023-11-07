

document.addEventListener('DOMContentLoaded', function () {
    const dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach(dropdown => {
        const dropdownContent = dropdown.querySelector('.dropdown-content1');

        dropdown.addEventListener('mouseover', () => {
            dropdownContent.style.display = 'block';
        });

        dropdown.addEventListener('mouseout', () => {
            dropdownContent.style.display = 'none';
        });
    });
});

