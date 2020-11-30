import UI.UI as UI


def to_prompt_sequence(part):
    prompt_sequence = []

    for key, value in part.properties.items():
        if isinstance(key, str):
            if isinstance(value, str):
                prompt_sequence.append(UI.ValuePrompt(key))
            elif isinstance(value, list):
                prompt_sequence.append(UI.ListPrompt(key, value))
            else:
                raise TypeError("Unsupporetd value type")
        elif isinstance(key, tuple):
            # TODO: not good
            first_list = []
            second_list = []

            for i in value:
                first_list.append(i[0])
                second_list.append(UI.ListPrompt(key[1], i[1]))

            prompt_sequence.append(UI.EmbeddedListPrompt(key[0], first_list, second_list))
        else:
            raise TypeError("Unsuported key type")

    # TODO: not good as well
    prompt_sequence.append(UI.ValuePrompt("Amount"))

    return prompt_sequence
