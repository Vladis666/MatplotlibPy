from graphviz import Digraph

# Створюємо граф для діаграми декомпозиції
decomposition_diagram = Digraph('Декомпозиція', filename='decomposition_diagram', format='png')

# Додаємо рівні ієрархії
decomposition_diagram.node('System', 'Система Курсів Валют')

# Додаємо модулі системи
decomposition_diagram.node('Data Collection', 'Модуль збору даних')
decomposition_diagram.node('Database', 'База даних (SQLite)')
decomposition_diagram.node('Analysis', 'Модуль аналізу даних')
decomposition_diagram.node('Visualization', 'Модуль візуалізації')

# Взаємозв'язки між модулями
decomposition_diagram.edge('System', 'Data Collection', label='Збір даних з API НБУ')
decomposition_diagram.edge('Data Collection', 'Database', label='Збереження даних')
decomposition_diagram.edge('Database', 'Analysis', label='Обробка даних')
decomposition_diagram.edge('Analysis', 'Visualization', label='Побудова графіків')

# Візуалізуємо та зберігаємо діаграму
decomposition_diagram.render('decomposition_diagram')
