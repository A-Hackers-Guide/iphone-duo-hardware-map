# `AVScheduledFloatValueRamp`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVScheduledParameterRamp`
- 2 instance variables, 2 properties, 11 instance methods, 4 class methods

## Instance variables

```
f _startValue;
f _endValue;
```

## Properties

```
@property (Tf,R) startFloatValue;
@property (Tf,R) endFloatValue;
```

## Class methods

```
+[AVScheduledFloatValueRamp defaultValue];
+[AVScheduledFloatValueRamp boundsAdjustedFloatValue:];
+[AVScheduledFloatValueRamp defaultFloatValue];
+[AVScheduledFloatValueRamp scheduledFloatValueRampWithStartValue:endValue:timeRange:];
```

## Instance methods

```
-[AVScheduledFloatValueRamp initWithPropertyList:];
-[AVScheduledFloatValueRamp propertyList];
-[AVScheduledFloatValueRamp startFloatValue];
-[AVScheduledFloatValueRamp _interpolatedValueAtTime:];
-[AVScheduledFloatValueRamp _makeRampWithTruncatedTimeRange:endValue:];
-[AVScheduledFloatValueRamp _parameterRampMode];
-[AVScheduledFloatValueRamp endFloatValue];
-[AVScheduledFloatValueRamp endValue];
-[AVScheduledFloatValueRamp initWithStartValue:endValue:timeRange:];
-[AVScheduledFloatValueRamp scheduledParameterRampInterpolatedToTime:];
-[AVScheduledFloatValueRamp startValue];
```
