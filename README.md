# DOCUMENT TAGGER

## PROBLEM STATEMENT
Process through the text document, parse and tag the sections of the document. Each section of the
document should be tagged with a section header with the lookup of tags available. Enclose the
section text with start and end tags of the respective normalized header. Tag only the sections that
are available in the tags lookup. Additional tags need not be tagged.
Note: Parsed document should be a valid XML.

## SAMPLE LOOKUP
```
Description=Description
HISTORY OF PRESENT ILLNESS=HPI
```

## SAMPLE INPUT
```
Description: The patient complaining of abdominal pain, has a long-standing history of diabetes treated with Micronase
daily.
HISTORY OF PRESENT ILLNESS: The patient is a 45-year-old male complaining of abdominal pain. The patient also has a
long-standing history of diabetes which is treated with Micronase daily.
PAST MEDICAL HISTORY: There is no significant past medical history noted today.
PHYSICAL EXAMINATION:
HEENT: Patient denies ear abnormalities, nose abnormalities and throat abnormalities.
Cardio: Patient has history of elevated cholesterol, but does not have ASHD, hypertension and PVD.
GU: Patient has history of Urinary tract disorder, but does not have Bladder disorder and Kidney disorder.
Endocrine: Patient has history of diabetes, but does not have hormonal irregularities and thyroid abnormalities.
Dermatology: Patient denies allergic reactions, rashes and skin lesions.
MEDS: Micronase 2.5 mg Tab PO QAM #30. Bactrim 400/80 Tab PO BID #30.
SOCIAL HISTORY: No known history of drug or alcohol abuse. Work, diet, and exercise patterns are within normal limits.
FAMILY HISTORY: No significant family history.
REVIEW OF SYSTEMS: Non-contributory.
Vital Signs: Height = 72 in. Weight =184 lbs. Upright BP = 120/80 mmHg. Pulse = 80 bpm. Resp =12 pm. Patient is afebrile.
Neck: The neck is supple. There is no jugular venous distension. The thyroid is nontender, or normal size and conto.
Lungs: Lung expansion and excursions are symmetric. The lungs are clear to auscultation and percussion.
Cardio: There is a regular rhythm. SI and S2 are normal. No abnormal heart sounds are detected. Blood pressure is equal
bilaterally.
ASSESSMENT: Diabetes type II uncontrolled. Acute cystitis.
PLAN: Endocrinology Consult, complete CBC.
RX: Micronase 2.5 mg Tab PO QAM #30, Bactrim 400/80 Tab PO BID #30.
```

## SAMPLE OUTPUT
```
<mChart>
<Description><header>Description: </header>The patient complaining of abdominal pain, has a long-standing history of
diabetes treated with Micronase daily.
(Medical Transcription Sample Report) </Description>
<HPI><header>HISTORY OF PRESENT ILLNESS:</header> The patient is a 45-year-old male complaining of abdominal pain.
The patient also has a long-standing history of diabetes which is treated with Micronase daily. </HPI>
<PastMedicalHistory><header>PAST MEDICAL HISTORY:</header> There is no significant past medical history noted today.
</PastMedicalHistory>
<PhysicalExam><header>PHYSICAL EXAMINATION:</header>
HEENT: Patient denies ear abnormalities, nose abnormalities and throat abnormalities.
Cardio: Patient has history of elevated cholesterol, but does not have ASHD, hypertension and PVD.
GU: Patient has history of Urinary tract disorder, but does not have Bladder disorder and Kidney disorder.
Endocrine: Patient has history of diabetes, but does not have hormonal irregularities and thyroid abnormalities.
Dermatology: Patient denies allergic reactions, rashes and skin lesions. </PhysicalExam>
<Medication><header>MEDS:</header> Micronase 2.5 mg Tab PO QAM #30. Bactrim 400/80 Tab PO BID #30.
</Medication>
<SocialHistory><header>SOCIAL HISTORY:</header> No known history of drug or alcohol abuse. Work, diet, and exercise
patterns are within normal limits. </SocialHistory>
<FamilyHistory><header>FAMILY HISTORY: </header>No significant family history. </FamilyHistory>
<ROS><header>REVIEW OF SYSTEMS:</header> Non-contributory.
Vital Signs: Height = 72 in. Weight =184 lbs. Upright BP = 120/80 mmHg. Pulse = 80 bpm. Resp =12 pm. Patient is afebrile.
Neck: The neck is supple. There is no jugular venous distension. The thyroid is nontender, or normal size and conto.
Lungs: Lung expansion and excursions are symmetric. The lungs are clear to auscultation and percussion.
Cardio: There is a regular rhythm. SI and S2 are normal. No abnormal heart sounds are detected. Blood pressure is equal
bilaterally.</ROS>
<Assessment><header>ASSESSMENT:</header> Diabetes type II uncontrolled. Acute cystitis. </Assessment>
<Plan><header>PLAN:</header> Endocrinology Consult, complete CBC. </Plan>
<Description><header>RX:</header> Micronase 2.5 mg Tab PO QAM #30, Bactrim 400/80 Tab PO BID #30. </Description>
</mChart>
```
 ## DOCUMENT SOURCE REFERENCE URL
 <https://www.mtsamples.com/site/pages/browse.asp?type=98-General%20Medicine>
