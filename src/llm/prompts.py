INTERVIEW_QUESTIONS = {
    1: {
        "llm_temperature": False,
        "input_variables": ["raw_interview"],
        "previous_answers": False,
        "text_template": """
            Пожалуйста, внимательно прочтите предоставленное вам интервью и следуйте приведенным ниже пошаговым инструкциям: <interview>{raw_interview}</interview>

            Пошаговые инструкции:
            1. Используйте только информацию, предоставленную в интервью, не придумывайте ничего самостоятельно.
            2. Выделите ключевые фразы, словосочетания или предложения, которые отражают важные идеи, концепции или опыт (поместите ответ в тег <keywords>).
            3. Присвойте каждому выделенному сегменту короткие ярлыки, используя описательные фразы или слова, которые обобщают основную идею. Иначе говоря, проведите начальное кодирование(открытое кодирование, initial coding) предоставленного интервью (поместите ответ в тег <codes>). 
        """
    },
    2: {
        "llm_temperature": False,
        "input_variables": ["raw_interview", "previous_answers"],
        "previous_answers": True,
        "text_template": """
            Пожалуйста, внимательно прочтите предоставленное вам интервью и следуйте приведенным ниже пошаговым инструкциям: <interview>{raw_interview}</interview>

            Пошаговые инструкции:
            1. Используйте только информацию, предоставленную в интервью, не придумывайте ничего самостоятельно.
            2. Просмотрите тематические коды из предыдущих ответов: <interview_code>{previous_answers}</interview_code>, и найдите среди них сходства или взаимосвязи (поместите ответ в тег <code_connections>).
            3. Сгруппируйте связанные тематические коды в более широкие категории или основные темы, которые охватывают ключевые аспекты, обсуждавшиеся в интервью (поместите ответ в тег <code_groups>).
            4. Определите любые подтемы в рамках каждой основной темы для более детального понимания (поместите ответ в тег <code_groups_subtopics>).
            """
    },
    3: {
        "llm_temperature": False,
        "input_variables": ["raw_interview"],
        "previous_answers": False,
        "text_template": """
            Пожалуйста, внимательно прочтите предоставленное вам интервью и следуйте приведенным ниже пошаговым инструкциям: <interview>{raw_interview}</interview>

            Пошаговые инструкции:
            1. Используйте только информацию, предоставленную вам в интервью, не придумывайте ничего самостоятельно.
            2. Составьте список всех конкретных проблем, упомянутых респондентами .
            3. Подсчитайте, сколько раз упоминалась каждая проблема.
            4. Поместите окончательный ответ в тег <problems>.

            """
    },
    4: {
        "llm_temperature": False,
        "input_variables": ["raw_interview", "previous_answers"],
        "previous_answers": True,
        "text_template": """
            Пожалуйста, внимательно прочтите предоставленное вам интервью и следуйте приведенным ниже пошаговым инструкциям: <interview>{raw_interview}</interview>

            Пошаговые инструкции:
            1. Используйте только информацию, предоставленную вам в интервью, не придумывайте ничего самостоятельно.
            2. Просмотрите список проблем <interview_problems>{previous_answers}</interview_problems> и найдите среди них сходства или взаимосвязи (поместите ответ в тег <problem_connections>).
            3. Сгруппируйте связанные проблемы в более широкие типы проблем, которые охватывают различные упомянутые проблемы в интервью (поместите ответ в тег <problem_groups>).

            """
    },
    5: {
        "llm_temperature": 0.5,
        "input_variables": ["raw_interview", "previous_answers"],
        "previous_answers": True,
        "text_template": """
            Пожалуйста, внимательно прочтите предоставленное вам интервью и категории проблем, которые были выявлены при первичном анализе данного интервью:
            <interview>{raw_interview}</interview> and <interview_problems>{previous_answers}</interview_problems>

            Пошаговые инструкции:
            1. Используйте только информацию, предоставленную вам в интервью и в выявленных категориях проблем, не придумывайте ничего самостоятельно.
            2. Проанализируйте темы и частоту возникновения проблем и их категории (поместите ответ в тег <reflections>)
            3. Проанализируйте, что говорят об опыте, взглядах или трудностях респондента результаты предыдущего шага содержащиеся в разделе <reflections> ... </reflections> (поместите ответ в тег <results>).
            4. Обратите внимание на любые неожиданные закономерности, связи или контрасты в данных. Поделитесь этими наблюдениями (поместите ответ в тег <unexpected>).
            5. Разработайте предварительные объяснения или гипотезы о том, почему возникли определенные темы или проблемы и как они могут быть связаны друг с другом или с более широкими контекстуальными факторами (поместите ответ в тег <hypothesis>).
            6. Рассмотрите альтернативные объяснения и контрпримеры, чтобы прояснить гипотезы сформированные вами в результатах предыдущего шага <hypothesis> ... </hypothesis> (поместите ответ в тег <alternatives>).
            7. Укажите области, в которых могут потребоваться дополнительные исследования или анализ для подтверждения ваших идей из раздела <alternatives> ... </alternatives>. (поместите ответ в тег <additionals>). 

   
            """
    }
}

SUMMARY_QUESTIONS = {
    1: {
        "llm_temperature": 0.3,
        "input_variables": ["raw_interview"],
        "previous_answers": False,
        "text_template": """
            Ваша задача – внимательно прочитать предоставленные вам заметки с итогами интервью, проанализировать их и обобщить каждый раздел (подвести общие итоги).  
            Все интервью имеют одинаковую структуру, вот ее пример: <example>
              - Ключевые фразы интервью: ...
              - Кодирование интервью: ...
              - Взаимосвязи кодов: ...
              - Группировка кодов: ...
              - Проблемы обозначенные в интервью: ...
              - Взаимосвязи обозначенных проблем: ... 
              - Группировка обозначенных проблем: ...
              - Проблемы и частота их появления: ...
              - Анализ проблем: ...
              - Неожиданные закономерности в ответах: ...
              - Гипотезы возникновения проблем: ... 
              - Альтернативные объяснения проблем: ... 
              - Дополнительные исследования: ... </example>

            Пошаговые инструкции:
            1. Используйте только информацию, предоставленную вам в интервью и в выявленных категориях проблем, не придумывайте ничего самостоятельно.       
            2. Для раздела "Ключевые фразы интервью:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <keywords>).
            3. Для раздела "Кодирование интервью:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <codes>).
            4. Для раздела "Взаимосвязи кодов:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <code_connections>).
            5. Для раздела "Группировка кодов:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <code_groups>).
            6. Для раздела "Проблемы обозначенные в интервью:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <problems>).
            7. Для раздела "Взаимосвязи обозначенных проблем:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <problem_connections>).
            8. Для раздела "Группировка обозначенных проблем:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <problem_groups>).
            9. Для раздела "Проблемы и частота их появления:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <reflections>).
            10. Для раздела "Анализ проблем:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <results>).
            11. Для раздела "Неожиданные закономерности в ответах:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <unexpected>).
            12. Для раздела "Гипотезы возникновения проблем:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <hypothesis>).
            13. Для раздела "Альтернативные объяснения проблем:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <alternatives>).
            14. Для раздела "Дополнительные исследования:" сделайте резюме всех интервью этого раздела (поместите ответ в тег <additionals>).
            

        Данные для анализа: <interview>{raw_interview}</interview>
        """
    },
}



