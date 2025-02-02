import javax.swing.*
import java.awt.*
import java.awt.event.ActionEvent
import java.awt.event.ActionListener

class NumberSystemConverter : JFrame() {
    private val inputField = JTextField()
    private val fromBaseField = JTextField()
    private val toBaseField = JTextField()
    private val resultLabel = JLabel("Результат:")

    init {
        title = "Калькулятор перевода систем счисления"
        setSize(400, 300)
        defaultCloseOperation = EXIT_ON_CLOSE
        layout = GridLayout(5, 2)

        // Ввод числа
        add(JLabel("Введите число:"))
        add(inputField)

        // Система счисления (из)
        add(JLabel("Система счисления (из):"))
        add(fromBaseField)

        // Система счисления (в)
        add(JLabel("Система счисления (в):"))
        add(toBaseField)

        // Кнопка конвертации
        val convertButton = JButton("Конвертировать")
        convertButton.addActionListener(ConvertButtonListener())
        add(convertButton)

        // Метка для результата
        add(resultLabel)
    }

    private inner class ConvertButtonListener : ActionListener {
        override fun actionPerformed(e: ActionEvent) {
            val number = inputField.text
            val fromBase: Int
            val toBase: Int

            try {
                fromBase = fromBaseField.text.toInt()
                toBase = toBaseField.text.toInt()

                // Конвертация в десятичную систему
                val decimalNumber = number.toInt(fromBase)
                // Конвертация из десятичной системы в нужную
                val convertedNumber = decimalNumber.toString(toBase).uppercase()

                resultLabel.text = "Результат: $convertedNumber"
            } catch (ex: NumberFormatException) {
                JOptionPane.showMessageDialog(null, "Ошибка ввода. Проверьте число и системы счисления.", "Ошибка", JOptionPane.ERROR_MESSAGE)
            } catch (ex: IllegalArgumentException) {
                JOptionPane.showMessageDialog(null, "Неверная система счисления.", "Ошибка", JOptionPane.ERROR_MESSAGE)
            }
        }
    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            SwingUtilities.invokeLater {
                val converter = NumberSystemConverter()
                converter.isVisible = true
            }
        }
    }
}

fun String.toInt(base: Int): Int {
    return Integer.parseInt(this, base)
}

fun Int.toString(base: Int): String {
    return Integer.toString(this, base)
}
