/********************************************************************************
** Form generated from reading UI file 'BulkDetectionKw8690.ui'
**
** Created by: Qt User Interface Compiler version 4.8.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef BULKDETECTIONKW8690_H
#define BULKDETECTIONKW8690_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QRadioButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QTextEdit>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_BulkDetectionWindow
{
public:
    QDialogButtonBox *BulkDetectBtnBox;
    QWidget *horizontalLayoutWidget;
    QHBoxLayout *noiseHL;
    QLabel *NoiseLbl;
    QSpacerItem *horizontalSpacer_3;
    QRadioButton *allNoiseRB;
    QCheckBox *noiseRemRawCB;
    QCheckBox *noiseRemCB;
    QSpacerItem *horizontalSpacer_2;
    QWidget *horizontalLayoutWidget_2;
    QHBoxLayout *featuresHL;
    QWidget *horizontalLayoutWidget_3;
    QHBoxLayout *preprocHL;
    QWidget *horizontalLayoutWidget_4;
    QHBoxLayout *enhancementHL;
    QWidget *horizontalLayoutWidget_5;
    QHBoxLayout *classifiersHL;
    QPushButton *trainDirBrowseB;
    QTextEdit *trainPathT;
    QLabel *trainDirLbl;
    QTextEdit *detectPathT;
    QPushButton *detectDirBrowseB;
    QLabel *detectDirLbl;
    QCheckBox *updateGDocsCB;
    QPushButton *detectFileBrowseB;
    QPushButton *trainFileBrowseB;
    QCheckBox *likelihoodCB;
    QCheckBox *fisherCB;
    QRadioButton *allClassifiersRB;
    QCheckBox *KNNCB;
    QCheckBox *leastSquaresCB;
    QLabel *classifiersLbl;
    QLabel *enhancementLbl;
    QCheckBox *PCACB;
    QCheckBox *LDACB;
    QRadioButton *allEnhancementRB;
    QCheckBox *NoneCB;
    QCheckBox *lMBhMBmCB;
    QCheckBox *lMBhMBCB;
    QCheckBox *lMhBmCB;
    QRadioButton *allFeaturesRB;
    QLabel *featuresLbl;
    QCheckBox *lMhBCB;
    QCheckBox *meanCB;
    QLabel *preprocessingLbl;
    QCheckBox *butterCB;
    QRadioButton *allPreprocessingRB;
    QCheckBox *idealCB;
    QCheckBox *NoFilterCB;

    void setupUi(QDialog *BulkDetectionWindow)
    {
        if (BulkDetectionWindow->objectName().isEmpty())
            BulkDetectionWindow->setObjectName(QString::fromUtf8("BulkDetectionWindow"));
        BulkDetectionWindow->resize(1215, 745);
        BulkDetectBtnBox = new QDialogButtonBox(BulkDetectionWindow);
        BulkDetectBtnBox->setObjectName(QString::fromUtf8("BulkDetectBtnBox"));
        BulkDetectBtnBox->setGeometry(QRect(550, 580, 451, 111));
        BulkDetectBtnBox->setOrientation(Qt::Horizontal);
        BulkDetectBtnBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);
        horizontalLayoutWidget = new QWidget(BulkDetectionWindow);
        horizontalLayoutWidget->setObjectName(QString::fromUtf8("horizontalLayoutWidget"));
        horizontalLayoutWidget->setGeometry(QRect(20, 70, 771, 51));
        noiseHL = new QHBoxLayout(horizontalLayoutWidget);
        noiseHL->setObjectName(QString::fromUtf8("noiseHL"));
        noiseHL->setContentsMargins(0, 0, 0, 0);
        NoiseLbl = new QLabel(horizontalLayoutWidget);
        NoiseLbl->setObjectName(QString::fromUtf8("NoiseLbl"));

        noiseHL->addWidget(NoiseLbl);

        horizontalSpacer_3 = new QSpacerItem(57, 20, QSizePolicy::Fixed, QSizePolicy::Minimum);

        noiseHL->addItem(horizontalSpacer_3);

        allNoiseRB = new QRadioButton(horizontalLayoutWidget);
        allNoiseRB->setObjectName(QString::fromUtf8("allNoiseRB"));

        noiseHL->addWidget(allNoiseRB);

        noiseRemRawCB = new QCheckBox(horizontalLayoutWidget);
        noiseRemRawCB->setObjectName(QString::fromUtf8("noiseRemRawCB"));
        noiseRemRawCB->setChecked(false);

        noiseHL->addWidget(noiseRemRawCB);

        noiseRemCB = new QCheckBox(horizontalLayoutWidget);
        noiseRemCB->setObjectName(QString::fromUtf8("noiseRemCB"));

        noiseHL->addWidget(noiseRemCB);

        horizontalSpacer_2 = new QSpacerItem(142, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        noiseHL->addItem(horizontalSpacer_2);

        horizontalLayoutWidget_2 = new QWidget(BulkDetectionWindow);
        horizontalLayoutWidget_2->setObjectName(QString::fromUtf8("horizontalLayoutWidget_2"));
        horizontalLayoutWidget_2->setGeometry(QRect(20, 180, 955, 45));
        featuresHL = new QHBoxLayout(horizontalLayoutWidget_2);
        featuresHL->setObjectName(QString::fromUtf8("featuresHL"));
        featuresHL->setContentsMargins(0, 0, 0, 0);
        horizontalLayoutWidget_3 = new QWidget(BulkDetectionWindow);
        horizontalLayoutWidget_3->setObjectName(QString::fromUtf8("horizontalLayoutWidget_3"));
        horizontalLayoutWidget_3->setGeometry(QRect(20, 130, 771, 45));
        preprocHL = new QHBoxLayout(horizontalLayoutWidget_3);
        preprocHL->setObjectName(QString::fromUtf8("preprocHL"));
        preprocHL->setContentsMargins(0, 0, 0, 0);
        horizontalLayoutWidget_4 = new QWidget(BulkDetectionWindow);
        horizontalLayoutWidget_4->setObjectName(QString::fromUtf8("horizontalLayoutWidget_4"));
        horizontalLayoutWidget_4->setGeometry(QRect(30, 240, 771, 45));
        enhancementHL = new QHBoxLayout(horizontalLayoutWidget_4);
        enhancementHL->setObjectName(QString::fromUtf8("enhancementHL"));
        enhancementHL->setContentsMargins(0, 0, 0, 0);
        horizontalLayoutWidget_5 = new QWidget(BulkDetectionWindow);
        horizontalLayoutWidget_5->setObjectName(QString::fromUtf8("horizontalLayoutWidget_5"));
        horizontalLayoutWidget_5->setGeometry(QRect(20, 300, 771, 45));
        classifiersHL = new QHBoxLayout(horizontalLayoutWidget_5);
        classifiersHL->setObjectName(QString::fromUtf8("classifiersHL"));
        classifiersHL->setContentsMargins(0, 0, 0, 0);
        trainDirBrowseB = new QPushButton(BulkDetectionWindow);
        trainDirBrowseB->setObjectName(QString::fromUtf8("trainDirBrowseB"));
        trainDirBrowseB->setGeometry(QRect(370, 410, 171, 51));
        trainPathT = new QTextEdit(BulkDetectionWindow);
        trainPathT->setObjectName(QString::fromUtf8("trainPathT"));
        trainPathT->setGeometry(QRect(30, 410, 321, 41));
        trainPathT->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        trainPathT->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        trainDirLbl = new QLabel(BulkDetectionWindow);
        trainDirLbl->setObjectName(QString::fromUtf8("trainDirLbl"));
        trainDirLbl->setGeometry(QRect(30, 360, 361, 31));
        detectPathT = new QTextEdit(BulkDetectionWindow);
        detectPathT->setObjectName(QString::fromUtf8("detectPathT"));
        detectPathT->setGeometry(QRect(32, 523, 311, 41));
        detectPathT->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        detectPathT->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        detectDirBrowseB = new QPushButton(BulkDetectionWindow);
        detectDirBrowseB->setObjectName(QString::fromUtf8("detectDirBrowseB"));
        detectDirBrowseB->setGeometry(QRect(350, 520, 181, 51));
        detectDirLbl = new QLabel(BulkDetectionWindow);
        detectDirLbl->setObjectName(QString::fromUtf8("detectDirLbl"));
        detectDirLbl->setGeometry(QRect(30, 460, 471, 51));
        updateGDocsCB = new QCheckBox(BulkDetectionWindow);
        updateGDocsCB->setObjectName(QString::fromUtf8("updateGDocsCB"));
        updateGDocsCB->setGeometry(QRect(580, 461, 361, 41));
        detectFileBrowseB = new QPushButton(BulkDetectionWindow);
        detectFileBrowseB->setObjectName(QString::fromUtf8("detectFileBrowseB"));
        detectFileBrowseB->setGeometry(QRect(540, 520, 161, 51));
        trainFileBrowseB = new QPushButton(BulkDetectionWindow);
        trainFileBrowseB->setObjectName(QString::fromUtf8("trainFileBrowseB"));
        trainFileBrowseB->setGeometry(QRect(550, 410, 191, 51));
        likelihoodCB = new QCheckBox(BulkDetectionWindow);
        likelihoodCB->setObjectName(QString::fromUtf8("likelihoodCB"));
        likelihoodCB->setGeometry(QRect(479, 300, 159, 43));
        fisherCB = new QCheckBox(BulkDetectionWindow);
        fisherCB->setObjectName(QString::fromUtf8("fisherCB"));
        fisherCB->setGeometry(QRect(271, 300, 106, 43));
        allClassifiersRB = new QRadioButton(BulkDetectionWindow);
        allClassifiersRB->setObjectName(QString::fromUtf8("allClassifiersRB"));
        allClassifiersRB->setGeometry(QRect(202, 300, 63, 43));
        KNNCB = new QCheckBox(BulkDetectionWindow);
        KNNCB->setObjectName(QString::fromUtf8("KNNCB"));
        KNNCB->setGeometry(QRect(383, 300, 90, 43));
        leastSquaresCB = new QCheckBox(BulkDetectionWindow);
        leastSquaresCB->setObjectName(QString::fromUtf8("leastSquaresCB"));
        leastSquaresCB->setGeometry(QRect(644, 300, 130, 43));
        classifiersLbl = new QLabel(BulkDetectionWindow);
        classifiersLbl->setObjectName(QString::fromUtf8("classifiersLbl"));
        classifiersLbl->setGeometry(QRect(26, 300, 137, 43));
        enhancementLbl = new QLabel(BulkDetectionWindow);
        enhancementLbl->setObjectName(QString::fromUtf8("enhancementLbl"));
        enhancementLbl->setGeometry(QRect(30, 240, 114, 43));
        PCACB = new QCheckBox(BulkDetectionWindow);
        PCACB->setObjectName(QString::fromUtf8("PCACB"));
        PCACB->setGeometry(QRect(263, 240, 82, 43));
        LDACB = new QCheckBox(BulkDetectionWindow);
        LDACB->setObjectName(QString::fromUtf8("LDACB"));
        LDACB->setGeometry(QRect(351, 240, 83, 43));
        allEnhancementRB = new QRadioButton(BulkDetectionWindow);
        allEnhancementRB->setObjectName(QString::fromUtf8("allEnhancementRB"));
        allEnhancementRB->setGeometry(QRect(194, 240, 63, 43));
        NoneCB = new QCheckBox(BulkDetectionWindow);
        NoneCB->setObjectName(QString::fromUtf8("NoneCB"));
        NoneCB->setGeometry(QRect(440, 240, 99, 43));
        lMBhMBmCB = new QCheckBox(BulkDetectionWindow);
        lMBhMBmCB->setObjectName(QString::fromUtf8("lMBhMBmCB"));
        lMBhMBmCB->setGeometry(QRect(810, 180, 170, 43));
        lMBhMBCB = new QCheckBox(BulkDetectionWindow);
        lMBhMBCB->setObjectName(QString::fromUtf8("lMBhMBCB"));
        lMBhMBCB->setGeometry(QRect(659, 180, 145, 43));
        lMhBmCB = new QCheckBox(BulkDetectionWindow);
        lMhBmCB->setObjectName(QString::fromUtf8("lMhBmCB"));
        lMhBmCB->setGeometry(QRect(481, 180, 172, 43));
        allFeaturesRB = new QRadioButton(BulkDetectionWindow);
        allFeaturesRB->setObjectName(QString::fromUtf8("allFeaturesRB"));
        allFeaturesRB->setGeometry(QRect(199, 180, 63, 43));
        featuresLbl = new QLabel(BulkDetectionWindow);
        featuresLbl->setObjectName(QString::fromUtf8("featuresLbl"));
        featuresLbl->setGeometry(QRect(33, 180, 118, 43));
        lMhBCB = new QCheckBox(BulkDetectionWindow);
        lMhBCB->setObjectName(QString::fromUtf8("lMhBCB"));
        lMhBCB->setGeometry(QRect(373, 180, 102, 43));
        meanCB = new QCheckBox(BulkDetectionWindow);
        meanCB->setObjectName(QString::fromUtf8("meanCB"));
        meanCB->setGeometry(QRect(268, 180, 99, 43));
        preprocessingLbl = new QLabel(BulkDetectionWindow);
        preprocessingLbl->setObjectName(QString::fromUtf8("preprocessingLbl"));
        preprocessingLbl->setGeometry(QRect(30, 130, 107, 43));
        butterCB = new QCheckBox(BulkDetectionWindow);
        butterCB->setObjectName(QString::fromUtf8("butterCB"));
        butterCB->setGeometry(QRect(259, 130, 110, 43));
        butterCB->setCheckable(true);
        butterCB->setChecked(false);
        butterCB->setTristate(false);
        allPreprocessingRB = new QRadioButton(BulkDetectionWindow);
        allPreprocessingRB->setObjectName(QString::fromUtf8("allPreprocessingRB"));
        allPreprocessingRB->setGeometry(QRect(190, 130, 63, 43));
        allPreprocessingRB->setChecked(false);
        idealCB = new QCheckBox(BulkDetectionWindow);
        idealCB->setObjectName(QString::fromUtf8("idealCB"));
        idealCB->setGeometry(QRect(375, 130, 91, 43));
        idealCB->setCheckable(true);
        idealCB->setChecked(false);
        idealCB->setTristate(false);
        NoFilterCB = new QCheckBox(BulkDetectionWindow);
        NoFilterCB->setObjectName(QString::fromUtf8("NoFilterCB"));
        NoFilterCB->setGeometry(QRect(470, 130, 111, 43));
        BulkDetectBtnBox->raise();
        horizontalLayoutWidget->raise();
        horizontalLayoutWidget_2->raise();
        horizontalLayoutWidget_3->raise();
        horizontalLayoutWidget_4->raise();
        horizontalLayoutWidget_5->raise();
        trainDirBrowseB->raise();
        trainPathT->raise();
        trainDirLbl->raise();
        detectPathT->raise();
        detectDirBrowseB->raise();
        detectDirLbl->raise();
        updateGDocsCB->raise();
        detectFileBrowseB->raise();
        trainFileBrowseB->raise();
        likelihoodCB->raise();
        fisherCB->raise();
        allClassifiersRB->raise();
        KNNCB->raise();
        leastSquaresCB->raise();
        classifiersLbl->raise();
        enhancementLbl->raise();
        PCACB->raise();
        LDACB->raise();
        allEnhancementRB->raise();
        NoneCB->raise();
        lMBhMBmCB->raise();
        lMBhMBCB->raise();
        lMhBmCB->raise();
        allFeaturesRB->raise();
        featuresLbl->raise();
        lMhBCB->raise();
        meanCB->raise();
        lMhBmCB->raise();
        lMBhMBmCB->raise();
        lMBhMBCB->raise();
        lMhBmCB->raise();
        allFeaturesRB->raise();
        featuresLbl->raise();
        lMhBCB->raise();
        meanCB->raise();
        preprocessingLbl->raise();
        butterCB->raise();
        allPreprocessingRB->raise();
        idealCB->raise();
        NoFilterCB->raise();

        retranslateUi(BulkDetectionWindow);

        QMetaObject::connectSlotsByName(BulkDetectionWindow);
    } // setupUi

    void retranslateUi(QDialog *BulkDetectionWindow)
    {
        BulkDetectionWindow->setWindowTitle(QApplication::translate("BulkDetectionWindow", "Bulk Detection", 0, QApplication::UnicodeUTF8));
        NoiseLbl->setText(QApplication::translate("BulkDetectionWindow", "Noise:", 0, QApplication::UnicodeUTF8));
        allNoiseRB->setText(QApplication::translate("BulkDetectionWindow", "All", 0, QApplication::UnicodeUTF8));
        noiseRemRawCB->setText(QApplication::translate("BulkDetectionWindow", "Raw", 0, QApplication::UnicodeUTF8));
        noiseRemCB->setText(QApplication::translate("BulkDetectionWindow", "Remove", 0, QApplication::UnicodeUTF8));
        trainDirBrowseB->setText(QApplication::translate("BulkDetectionWindow", "Browse Dir", 0, QApplication::UnicodeUTF8));
        trainDirLbl->setText(QApplication::translate("BulkDetectionWindow", "Train Files Path", 0, QApplication::UnicodeUTF8));
        detectDirBrowseB->setText(QApplication::translate("BulkDetectionWindow", "Browse Dir", 0, QApplication::UnicodeUTF8));
        detectDirLbl->setText(QApplication::translate("BulkDetectionWindow", "Detect Files Path", 0, QApplication::UnicodeUTF8));
        updateGDocsCB->setText(QApplication::translate("BulkDetectionWindow", "Update GDocs", 0, QApplication::UnicodeUTF8));
        detectFileBrowseB->setText(QApplication::translate("BulkDetectionWindow", "Browse File", 0, QApplication::UnicodeUTF8));
        trainFileBrowseB->setText(QApplication::translate("BulkDetectionWindow", "Browse File", 0, QApplication::UnicodeUTF8));
        likelihoodCB->setText(QApplication::translate("BulkDetectionWindow", "Likelihood", 0, QApplication::UnicodeUTF8));
        fisherCB->setText(QApplication::translate("BulkDetectionWindow", "Fisher", 0, QApplication::UnicodeUTF8));
        allClassifiersRB->setText(QApplication::translate("BulkDetectionWindow", "All", 0, QApplication::UnicodeUTF8));
        KNNCB->setText(QApplication::translate("BulkDetectionWindow", "KNN", 0, QApplication::UnicodeUTF8));
        leastSquaresCB->setText(QApplication::translate("BulkDetectionWindow", "LeastSq", 0, QApplication::UnicodeUTF8));
        classifiersLbl->setText(QApplication::translate("BulkDetectionWindow", "Classifiers:", 0, QApplication::UnicodeUTF8));
        enhancementLbl->setText(QApplication::translate("BulkDetectionWindow", "Enhance:", 0, QApplication::UnicodeUTF8));
        PCACB->setText(QApplication::translate("BulkDetectionWindow", "PCA", 0, QApplication::UnicodeUTF8));
        LDACB->setText(QApplication::translate("BulkDetectionWindow", "LDA", 0, QApplication::UnicodeUTF8));
        allEnhancementRB->setText(QApplication::translate("BulkDetectionWindow", "All", 0, QApplication::UnicodeUTF8));
        NoneCB->setText(QApplication::translate("BulkDetectionWindow", "None", 0, QApplication::UnicodeUTF8));
        lMBhMBmCB->setText(QApplication::translate("BulkDetectionWindow", "LMBhMBm", 0, QApplication::UnicodeUTF8));
        lMBhMBCB->setText(QApplication::translate("BulkDetectionWindow", "LMBhMB", 0, QApplication::UnicodeUTF8));
        lMhBmCB->setText(QApplication::translate("BulkDetectionWindow", "LMhBmean", 0, QApplication::UnicodeUTF8));
        allFeaturesRB->setText(QApplication::translate("BulkDetectionWindow", "All", 0, QApplication::UnicodeUTF8));
        featuresLbl->setText(QApplication::translate("BulkDetectionWindow", "Features:", 0, QApplication::UnicodeUTF8));
        lMhBCB->setText(QApplication::translate("BulkDetectionWindow", "LMhB", 0, QApplication::UnicodeUTF8));
        meanCB->setText(QApplication::translate("BulkDetectionWindow", "Mean", 0, QApplication::UnicodeUTF8));
        preprocessingLbl->setText(QApplication::translate("BulkDetectionWindow", "Preproc:", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        butterCB->setToolTip(QString());
#endif // QT_NO_TOOLTIP
        butterCB->setText(QApplication::translate("BulkDetectionWindow", "Butter", 0, QApplication::UnicodeUTF8));
        allPreprocessingRB->setText(QApplication::translate("BulkDetectionWindow", "All", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_TOOLTIP
        idealCB->setToolTip(QString());
#endif // QT_NO_TOOLTIP
        idealCB->setText(QApplication::translate("BulkDetectionWindow", "Ideal", 0, QApplication::UnicodeUTF8));
        NoFilterCB->setText(QApplication::translate("BulkDetectionWindow", "None", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class BulkDetectionWindow: public Ui_BulkDetectionWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // BULKDETECTIONKW8690_H
