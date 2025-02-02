import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class NumberSystemConverter extends JFrame {
    private JTextField inputField;
    private JTextField fromBaseField;
    private JTextField toBaseField;
    private JLabel resultLabel;

    public NumberSystemConverter() {
        setTitle("Калькулятор перевода систем счисления");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(5, 2));

        // Ввод числа
        add(new JLabel("Введите число:"));
        inputField = new JTextField();
        add(inputField);

        // Система счисления (из)
        add(new JLabel("Система счисления (из):"));
        fromBaseField = new JTextField();
        add(fromBaseField);

        // Система счисления (в)
        add(new JLabel("Система счисления (в):"));
        toBaseField = new JTextField();
        add(toBaseField);

        // Кнопка конвертации
        JButton convertButton = new JButton("Конвертировать");
        convertButton.addActionListener(new ConvertButtonListener());
        add(convertButton);

        // Метка для результата
        resultLabel = new JLabel("Результат:");
        add(resultLabel);
    }

    private class ConvertButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String number = inputField.getText();
            int fromBase;
            int toBase;

            try {
                fromBase = Integer.parseInt(fromBaseField.getText());
                toBase = Integer.parseInt(toBaseField.getText());

                // Конвертация в десятичную систему
                int decimalNumber = Integer.parseInt(number, fromBase);
                // Конвертация из десятичной системы в нужную
                String convertedNumber = Integer.toString(decimalNumber, toBase).toUpperCase();

                resultLabel.setText("Результат: " + convertedNumber);
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(null, "Ошибка ввода. Проверьте число и системы счисления.", "Ошибка", JOptionPane.ERROR_MESSAGE);
            } catch (IllegalArgumentException ex) {
                JOptionPane.showMessageDialog(null, "Неверная система счисления.", "Ошибка", JOptionPane.ERROR_MESSAGE);
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            NumberSystemConverter converter = new NumberSystemConverter();
            converter.setVisible(true);
        });
    }
}
