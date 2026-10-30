# `CMVO2MaxClassification`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 6 instance methods, 2 class methods

## Instance variables

```
{unique_ptr<CLVO2MaxClassifier, std::default_delete<CLVO2MaxClassifier>>=""{?="__ptr_"^{CLVO2MaxClassifier}}} fVO2MaxClassifier;
```

## Class methods

```
+[CMVO2MaxClassification CLHKBiologicalSexFromBiologicalSex:];
+[CMVO2MaxClassification biologicalSexFromCLHKBiologicalSex:];
```

## Instance methods

```
-[CMVO2MaxClassification init];
-[CMVO2MaxClassification queryAllClassificationThresholdsWithHandler:];
-[CMVO2MaxClassification queryAllClassificationsWithHandler:];
-[CMVO2MaxClassification queryClassificationForBiologicalSex:age:handler:];
-[CMVO2MaxClassification classificationDataFromStruct:];
-[CMVO2MaxClassification queryClassificationForBiologicalSex:age:vo2Max:handler:];
```
