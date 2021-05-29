#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QString>
#include <QtMath>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::calculate_keys()
{
    int p, g, a, b, A, B, Ka, Kb;
    // Возьмём простое число
    int len = 11;
    int nums[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
    p = nums[ rand()%len ];
    ui->P->setText(QString().setNum(p));
    g = nums[ rand()%len ];
    ui->G->setText(QString().setNum(g));

    // А выберет закрытый ключ и получает сгенерированный ключ
    a = 1 + rand()%5;
    ui->a->setText(QString().setNum(a));
    A = gen_keys(g, a, p);

    // B выберет закрытый ключ и получает сгенерированный ключ
    b = 1 + rand()%5;
    ui->b->setText(QString().setNum(b));
    B = gen_keys(g, b, p);

    // Генерация секретного ключа после обмена ключей
    Ka = gen_keys(B, a, p);
    ui->Ka->setText(QString().setNum(Ka));
    Kb = gen_keys(A, a, p);
    ui->Kb->setText(QString().setNum(Kb));
}

long int MainWindow::gen_keys(long int a, long int b, long int p)
{
    qreal valPow = qPow(a, b);
    long int valPowInt = static_cast<long int>(valPow);
    long int key = valPowInt % p;
    return key;
}
