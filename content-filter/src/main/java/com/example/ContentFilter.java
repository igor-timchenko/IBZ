package com.example;

import java.io.*;
import java.nio.file.*;
import java.util.*;

public class ContentFilter {

    private static String outputPath = "./";
    private static String prefix = "";
    private static boolean appendMode = false;
    private static boolean fullStats = false;

    public static void main(String[] args) {
        List<String> files = new ArrayList<>();
        parseArguments(args, files);

        List<Integer> integers = new ArrayList<>();
        List<Double> floats = new ArrayList<>();
        List<String> strings = new ArrayList<>();

        for (String filePath : files) {
            try {
                processFile(filePath, integers, floats, strings);
            } catch (IOException e) {
                System.err.println("Ошибка при обработке файла " + filePath + ": " + e.getMessage());
            }
        }

        writeOutput(integers, floats, strings);
        printStatistics(integers, floats, strings);
    }

    private static void parseArguments(String[] args, List<String> files) {
        for (int i = 0; i < args.length; i++) {
            switch (args[i]) {
                case "-o":
                    if (++i < args.length) outputPath = args[i];
                    break;
                case "-p":
                    if (++i < args.length) prefix = args[i];
                    break;
                case "-a":
                    appendMode = true;
                    break;
                case "-s":
                    fullStats = false;
                    break;
                case "-f":
                    fullStats = true;
                    break;
                default:
                    files.add(args[i]);
            }
        }
    }

    private static void processFile(String filePath, List<Integer> integers, List<Double> floats, List<String> strings) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        for (String line : lines) {
            try {
                if (line.matches("-?\d+")) {
                    integers.add(Integer.parseInt(line));
                } else if (line.matches("-?\d+\.\d+")) {
                    floats.add(Double.parseDouble(line));
                } else {
                    strings.add(line);
                }
            } catch (NumberFormatException e) {
                System.err.println("Не удалось преобразовать строку: " + line);
            }
        }
    }

    private static void writeOutput(List<Integer> integers, List<Double> floats, List<String> strings) {
        if (!integers.isEmpty()) {
            writeToFile(outputPath + prefix + "integers.txt", integers.stream().map(String::valueOf).toList());
        }
        if (!floats.isEmpty()) {
            writeToFile(outputPath + prefix + "floats.txt", floats.stream().map(String::valueOf).toList());
        }
        if (!strings.isEmpty()) {
            writeToFile(outputPath + prefix + "strings.txt", strings);
        }
    }

    private static void writeToFile(String fileName, List<String> lines) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName, appendMode))) {
            for (String line : lines) {
                writer.write(line);
                writer.newLine();
            }
        } catch (IOException e) {
            System.err.println("Ошибка записи в файл " + fileName + ": " + e.getMessage());
        }
    }

    private static void printStatistics(List<Integer> integers, List<Double> floats, List<String> strings) {
        if (fullStats) {
            printFullStatistics(integers, "Целые числа");
            printFullStatistics(floats, "Вещественные числа");
            printFullStatistics(strings, "Строки");
        } else {
            System.out.println("Краткая статистика:");
            System.out.println("Целые числа: " + integers.size());
            System.out.println("Вещественные числа: " + floats.size());
            System.out.println("Строки: " + strings.size());
        }
    }

    private static void printFullStatistics(List<?> data, String type) {
        System.out.println("Полная статистика для " + type + ":");
        System.out.println("Количество: " + data.size());

        if (data instanceof List<?>) {
            if (data.get(0) instanceof Integer) {
                List<Integer> intData = (List<Integer>) data;
                System.out.println("Минимум: " + Collections.min(intData));
                System.out.println("Максимум: " + Collections.max(intData));
                System.out.println("Сумма: " + intData.stream().mapToInt(Integer::intValue).sum());
                System.out.println("Среднее: " + intData.stream().mapToInt(Integer::intValue).average().orElse(0));
            } else if (data.get(0) instanceof Double) {
                List<Double> floatData = (List<Double>) data;
                System.out.println("Минимум: " + Collections.min(floatData));
                System.out.println("Максимум: " + Collections.max(floatData));
                System.out.println("Сумма: " + floatData.stream().mapToDouble(Double::doubleValue).sum());
                System.out.println("Среднее: " + floatData.stream().mapToDouble(Double::doubleValue).average().orElse(0));
            } else if (data.get(0) instanceof String) {
                List<String> stringData = (List<String>) data;
                System.out.println("Самая короткая строка: " + Collections.min(stringData, Comparator.comparingInt(String::length)));
                System.out.println("Самая длинная строка: " + Collections.max(stringData, Comparator.comparingInt(String::length)));
            }
        }
    }
}
