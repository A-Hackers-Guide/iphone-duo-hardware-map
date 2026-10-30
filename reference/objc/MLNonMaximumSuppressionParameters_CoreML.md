# `MLNonMaximumSuppressionParameters`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 29 instance methods, 0 class methods

## Instance variables

```
B _perClass;
i _suppressionMethod;
d _iouThreshold;
d _confidenceThreshold;
Q _minBoxes;
q _maxBoxes;
Q _numClasses;
@"NSString" _confidenceInputFeatureName;
@"NSString" _coordinatesInputFeatureName;
@"NSString" _iouThresholdInputFeatureName;
@"NSString" _confidenceThresholdInputFeatureName;
@"NSString" _confidenceOutputFeatureName;
@"NSString" _coordinatesOutputFeatureName;
@"NSArray" _labelNames;
```

## Properties

```
@property (Ti,V_suppressionMethod) suppressionMethod;
@property (Td,V_iouThreshold) iouThreshold;
@property (Td,V_confidenceThreshold) confidenceThreshold;
@property (TQ,V_minBoxes) minBoxes;
@property (Tq,V_maxBoxes) maxBoxes;
@property (TQ,V_numClasses) numClasses;
@property (TB,V_perClass) perClass;
@property (T@"NSString",&,V_confidenceInputFeatureName) confidenceInputFeatureName;
@property (T@"NSString",&,V_coordinatesInputFeatureName) coordinatesInputFeatureName;
@property (T@"NSString",&,V_iouThresholdInputFeatureName) iouThresholdInputFeatureName;
@property (T@"NSString",&,V_confidenceThresholdInputFeatureName) confidenceThresholdInputFeatureName;
@property (T@"NSString",&,V_confidenceOutputFeatureName) confidenceOutputFeatureName;
@property (T@"NSString",&,V_coordinatesOutputFeatureName) coordinatesOutputFeatureName;
@property (T@"NSArray",&,V_labelNames) labelNames;
```

## Instance methods

```
-[MLNonMaximumSuppressionParameters confidenceThreshold];
-[MLNonMaximumSuppressionParameters setConfidenceThreshold:];
-[MLNonMaximumSuppressionParameters setCoordinatesInputFeatureName:];
-[MLNonMaximumSuppressionParameters setConfidenceOutputFeatureName:];
-[MLNonMaximumSuppressionParameters confidenceInputFeatureName];
-[MLNonMaximumSuppressionParameters confidenceOutputFeatureName];
-[MLNonMaximumSuppressionParameters confidenceThresholdInputFeatureName];
-[MLNonMaximumSuppressionParameters coordinatesInputFeatureName];
-[MLNonMaximumSuppressionParameters coordinatesOutputFeatureName];
-[MLNonMaximumSuppressionParameters iouThreshold];
-[MLNonMaximumSuppressionParameters iouThresholdInputFeatureName];
-[MLNonMaximumSuppressionParameters labelNames];
-[MLNonMaximumSuppressionParameters maxBoxes];
-[MLNonMaximumSuppressionParameters minBoxes];
-[MLNonMaximumSuppressionParameters numClasses];
-[MLNonMaximumSuppressionParameters objectBoundingBoxOutputDescription];
-[MLNonMaximumSuppressionParameters perClass];
-[MLNonMaximumSuppressionParameters setConfidenceInputFeatureName:];
-[MLNonMaximumSuppressionParameters setConfidenceThresholdInputFeatureName:];
-[MLNonMaximumSuppressionParameters setCoordinatesOutputFeatureName:];
-[MLNonMaximumSuppressionParameters setIouThreshold:];
-[MLNonMaximumSuppressionParameters setIouThresholdInputFeatureName:];
-[MLNonMaximumSuppressionParameters setLabelNames:];
-[MLNonMaximumSuppressionParameters setMaxBoxes:];
-[MLNonMaximumSuppressionParameters setMinBoxes:];
-[MLNonMaximumSuppressionParameters setNumClasses:];
-[MLNonMaximumSuppressionParameters setPerClass:];
-[MLNonMaximumSuppressionParameters setSuppressionMethod:];
-[MLNonMaximumSuppressionParameters suppressionMethod];
```
