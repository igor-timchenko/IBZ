package com.example.guessthenumber;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import java.util.Random;

public class MainActivity extends AppCompatActivity {

    private Spinner levelSpinner;
    private EditText guessEditText;
    private Button guessButton;
    private TextView messageTextView;

    private int maxNumber;
    private int randomNumber;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        levelSpinner = findViewById(R.id.levelSpinner);
        guessEditText = findViewById(R.id.guessEditText);
        guessButton = findViewById(R.id.guessButton);
        messageTextView = findViewById(R.id.messageTextView);

        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
                R.array.levels_array, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        levelSpinner.setAdapter(adapter);

        levelSpinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                switch (position) {
                    case 0:
                        maxNumber = 10;
                        break;
                    case 1:
                        maxNumber = 100;
                        break;
                    case 2:
                        maxNumber = 1000;
                        break;
                }
                 generateRandomNumber();
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
                maxNumber = 10; // Default level
                generateRandomNumber();
            }
        });

        guessButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                checkGuess();
            }
        });
    }

    private void generateRandomNumber() {
        Random random = new Random();
        randomNumber = random.nextInt(maxNumber) + 1; // Generate number between 1 and maxNumber
    }

    private void checkGuess() {
        String guessString = guessEditText.getText().toString();
        if (guessString.isEmpty()) {
            messageTextView.setText("Пожалуйста, введите число.");
            return;
        }

        int guess = Integer.parseInt(guessString);
        if (guess < 1 || guess > maxNumber) {
            messageTextView.setText("Введите число от 1 до " + maxNumber + ".");
            return;
        }

        if (guess < randomNumber) {
            messageTextView.setText("Загаданное число больше.");
        } else if (guess > randomNumber) {
            messageTextView.setText("Загаданное число меньше.");
        } else {
            messageTextView.setText("Поздравляем! Вы угадали число!");
            generateRandomNumber(); // Generate a new number after guessing correctly
        }
    }
}
