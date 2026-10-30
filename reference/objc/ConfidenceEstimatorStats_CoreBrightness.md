# `ConfidenceEstimatorStats`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _edgeMappingStrength;
@"NSMutableDictionary" _edgeMappingConfidence;
I _modelID;
@"CBHistogramBuilder2D" _outputsCE;
```

## Properties

```
@property (T@"CBHistogramBuilder2D",R,V_outputsCE) outputsCE;
```

## Instance methods

```
-[ConfidenceEstimatorStats submit];
-[ConfidenceEstimatorStats dealloc];
-[ConfidenceEstimatorStats collectStrength:andConfidence:];
-[ConfidenceEstimatorStats initWithModelID:];
-[ConfidenceEstimatorStats outputsCE];
```
