# `SRFaceMetricsExpression`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSCopying`, `NSSecureCoding`
- 2 instance variables, 6 properties, 13 instance methods, 4 class methods

## Instance variables

```
@"NSString" _identifier;
d _value;
```

## Properties

```
@property (T@"NSString",R,C,N) identifier;
@property (Td,R,N) value;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRFaceMetricsExpression supportsSecureCoding];
+[SRFaceMetricsExpression new];
+[SRFaceMetricsExpression partialFaceMetricsExpressionWithIdentifier:value:];
+[SRFaceMetricsExpression wholeFaceMetricsExpressionWithIdentifier:value:];
```

## Instance methods

```
-[SRFaceMetricsExpression identifier];
-[SRFaceMetricsExpression init];
-[SRFaceMetricsExpression dealloc];
-[SRFaceMetricsExpression value];
-[SRFaceMetricsExpression initWithIdentifier:value:];
-[SRFaceMetricsExpression encodeWithCoder:];
-[SRFaceMetricsExpression hash];
-[SRFaceMetricsExpression description];
-[SRFaceMetricsExpression initWithCoder:];
-[SRFaceMetricsExpression copyWithZone:];
-[SRFaceMetricsExpression isEqual:];
-[SRFaceMetricsExpression binarySampleRepresentation];
-[SRFaceMetricsExpression initWithBinarySampleRepresentation:metadata:timestamp:];
```
