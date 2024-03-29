// Цей патерн передбачає, що ви маєте кілька сімейств продуктів,
// які знаходяться в окремих ієрархіях класів (Button/Checkbox).
// Продукти одного сімейства повинні мати спільний інтерфейс.
interface Button is
    method paint()

// Cімейства продуктів мають однакові варіації (macOS/Windows).
class WinButton implements Button is
    method paint() is
        // Відобразити кнопку в стилі Windows.

class MacButton implements Button is
    method paint() is
        // Відобразити кнопку в стилі macOS.


interface Checkbox is
    method paint()

class WinCheckbox implements Checkbox is
    method paint() is
        // Відобразити чекбокс в стилі Windows.

class MacCheckbox implements Checkbox is
    method paint() is
        // Відобразити чекбокс в стилі macOS.


// Абстрактна фабрика знає про всі абстрактні типи продуктів.
interface GUIFactory is
    method createButton():Button
    method createCheckbox():Checkbox


// Кожна конкретна фабрика знає лише про продукти своєї варіації
// і створює лише їх.
class WinFactory implements GUIFactory is
    method createButton():Button is
        return new WinButton()
    method createCheckbox():Checkbox is
        return new WinCheckbox()

// Незважаючи на те, що фабрики оперують конкретними класами,
// їхні методи повертають абстрактні типи продуктів. Завдяки
// цьому фабрики можна заміняти одну на іншу, не змінюючи
// клієнтського коду.
class MacFactory implements GUIFactory is
    method createButton():Button is
        return new MacButton()
    method createCheckbox():Checkbox is
        return new MacCheckbox()


// Для коду, який використовує фабрику, не важливо, з якою
// конкретно фабрикою він працює. Всі отримувачі продуктів
// працюють з ними через загальні інтерфейси.
class Application is
    private field factory: GUIFactory
    private field button: Button
    constructor Application(factory: GUIFactory) is
        this.factory = factory
    method createUI()
        this.button = factory.createButton()
    method paint()
        button.paint()


// Програма вибирає тип конкретної фабрики й створює її
// динамічно, виходячи з конфігурації або оточення.
class ApplicationConfigurator is
    method main() is
        config = readApplicationConfigFile()

        if (config.OS == "Windows") then
            factory = new WinFactory()
        else if (config.OS == "Mac") then
            factory = new MacFactory()
        else
            throw new Exception("Error! Unknown operating system.")

        Application app = new Application(factory)