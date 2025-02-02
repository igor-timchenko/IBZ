package com.example.numberbaseconverter

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.EditText
import android.widget.Spinner
import android.widget.TextView

class MainActivity : AppCompatActivity() {

    private lateinit var inputNumber: EditText
    private lateinit var fromBaseSpinner: Spinner
    private lateinit var toBaseSpinner: Spinner
    private lateinit var convertButton: Button
    private lateinit var resultTextView: TextView

    private val bases = arrayOf(2, 8, 10, 16)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        inputNumber = findViewById(R.id.inputNumber)
        fromBaseSpinner = findViewById(R.id.fromBaseSpinner)
        toBaseSpinner = findViewById(R.id.toBaseSpinner)
        convertButton = findViewById(R.id.convertButton)
        resultTextView = findViewById(R.id.resultTextView)

        setupSpinners()

        convertButton.setOnClickListener {
            convertNumber()
        }
    }

    private fun setupSpinners() {
        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_item, bases)
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)

        fromBaseSpinner.adapter = adapter
        toBaseSpinner.adapter = adapter
    }

    private fun convertNumber() {
        val number = inputNumber.text.toString()
        val fromBase = fromBaseSpinner.selectedItem as Int
        val toBase = toBaseSpinner.selectedItem as Int

        try {
            val decimalValue = number.toInt(fromBase)
            val result = Integer.toString(decimalValue, toBase).toUpperCase()
            resultTextView.text = "Результат: $result"
          } catch (e: NumberFormatException) {
            resultTextView.text = "Ошибка ввода. Проверьте число."
        }
    }
}
