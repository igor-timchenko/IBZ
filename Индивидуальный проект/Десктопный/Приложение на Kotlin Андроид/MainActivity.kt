package com.example.guessthenumber

import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.EditText
import android.widget.Spinner
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import java.util.*

class MainActivity : AppCompatActivity() {

    private lateinit var levelSpinner: Spinner
    private lateinit var guessEditText: EditText
    private lateinit var guessButton: Button
    private lateinit var messageTextView: TextView

    private var maxNumber = 10
    private var randomNumber = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        levelSpinner = findViewById(R.id.levelSpinner)
        guessEditText = findViewById(R.id.guessEditText)
        guessButton = findViewById(R.id.guessButton)
        messageTextView = findViewById(R.id.messageTextView)

        val adapter = ArrayAdapter.createFromResource(
            this,
            R.array.levels_array,
            android.R.layout.simple_spinner_item
        )
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        levelSpinner.adapter = adapter

        levelSpinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(parent: AdapterView<*>, view: View, position: Int, id: Long) {
                maxNumber = when (position) {
                    0 -> 10 // Легкий уровень
                    1 -> 100 // Средний уровень
                    2 -> 1000 // Сложный уровень
                    else -> 10
                }
                generateRandomNumber()
            }

            override fun onNothingSelected(parent: AdapterView<*>) {
              maxNumber = 10 // Уровень по умолчанию
                generateRandomNumber()
            }
        }

        guessButton.setOnClickListener {
            checkGuess()
        }
    }

    private fun generateRandomNumber() {
        randomNumber = Random().nextInt(maxNumber) + 1 // Генерируем число от 1 до maxNumber
    }

    private fun checkGuess() {
        val guessString = guessEditText.text.toString()
        
        if (guessString.isEmpty()) {
            messageTextView.text = "Пожалуйста, введите число."
            return
        }

        val guess = guessString.toInt()
        
        if (guess < 1 || guess > maxNumber) {
            messageTextView.text = "Введите число от 1 до $maxNumber."
            return
        }

        when {
            guess < randomNumber -> messageTextView.text = "Загаданное число больше."
            guess > randomNumber -> messageTextView.text = "Загаданное число меньше."
            else -> {
                messageTextView.text = "Поздравляем! Вы угадали число!"
                generateRandomNumber() // Генерируем новое число после правильного ответа
            }
        }
    }
}
