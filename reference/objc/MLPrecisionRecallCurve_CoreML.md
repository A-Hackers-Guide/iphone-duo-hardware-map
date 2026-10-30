# `MLPrecisionRecallCurve`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _precisionValues;
@"NSArray" _precisionConfidenceThresholds;
@"NSArray" _recallValues;
@"NSArray" _recallConfidenceThresholds;
```

## Properties

```
@property (T@"NSArray",R,N,V_precisionValues) precisionValues;
@property (T@"NSArray",R,N,V_precisionConfidenceThresholds) precisionConfidenceThresholds;
@property (T@"NSArray",R,N,V_recallValues) recallValues;
@property (T@"NSArray",R,N,V_recallConfidenceThresholds) recallConfidenceThresholds;
```

## Class methods

```
+[MLPrecisionRecallCurve supportsSecureCoding];
```

## Instance methods

```
-[MLPrecisionRecallCurve encodeWithCoder:];
-[MLPrecisionRecallCurve initWithCoder:];
-[MLPrecisionRecallCurve precisionValues];
-[MLPrecisionRecallCurve initWithPrecisionValues:precisionConfidenceThresholds:recallValues:recallConfidenceThresholds:];
-[MLPrecisionRecallCurve precisionConfidenceThresholds];
-[MLPrecisionRecallCurve recallConfidenceThresholds];
-[MLPrecisionRecallCurve recallValues];
```
