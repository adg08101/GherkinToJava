import re
import easygui


def txt_replace(text):
    if text.split()[0] in ["Given", "When", "And", "Then"]:
        quotes = '"'
        dots = '.'
        double_dots = ':'
        start_angular_brace = '<'
        end_angular_brace = '>'
        scape_quotes = '\\"'
        space = " "
        lower_separator = '_'
        temp_t = re.sub(r"""\"<\S*""", "{string}", text)
        temp_t = re.sub(r"""<\S*""", "{string}", temp_t)
        temp_t = temp_t.replace(quotes, scape_quotes)
        temp_t = temp_t.replace("Given", "@Given(" + quotes)
        temp_t = temp_t.replace("When", "@When(" + quotes)
        temp_t = temp_t.replace("And", "@And(" + quotes)
        temp_t = temp_t.replace("Then", "@Then(" + quotes)
        temp_t = temp_t.replace(" ", "", 1)
        temp_t = temp_t + quotes + ")"
        method_name = text.replace("Given ", "")
        method_name = method_name.replace("When ", "")
        method_name = method_name.replace("And ", "")
        method_name = method_name.replace("Then ", "")
        method_name = method_name.replace(quotes, "")
        method_name = method_name.replace(dots, "")
        method_name = method_name.replace(double_dots, "")
        method_name = method_name.replace(start_angular_brace, "")
        method_name = method_name.replace(end_angular_brace, "")
        method_name = str.lower(method_name)
        method_name = method_name.replace(space, lower_separator)
        temp_t += "\n" + "public void " + method_name + "("

        parameters = ""

        times = temp_t.count("{string}")

        if times > 0:
            for i in range(times):
                if i == 0:
                    parameters += "String str" + str(i)
                else:
                    parameters += ", String str" + str(i)

        temp_t += parameters + "){"
        temp_t += "\n" * 2 + "}" + "\n" * 2

        return temp_t
    else:
        return ""


def gherkin_to_java():
    text = easygui.codebox(msg='Gherkin Input',
                           title='Gherkin: to Java')

    text = text.split('\n')

    output = ""

    for i in text:
        output += txt_replace(str.strip(i.replace("#", "")))

    easygui.codebox(msg='Java Output',
                    title='Java: Final output',
                    text=output)


if __name__ == '__main__':
    gherkin_to_java()
