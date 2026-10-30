# `AVScheduledParameterRamp`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 4 properties, 12 instance methods, 3 class methods

## Instance variables

```
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _timeRange;
```

## Properties

```
@property (T{?={?=qiIq}{?=qiIq}},R) timeRange;
@property (T@,R) startValue;
@property (T@,R) endValue;
@property (T@"NSArray",R,G_additionalFigRepresentationObjects) additionalFigRepresentationObjects;
```

## Class methods

```
+[AVScheduledParameterRamp defaultValue];
+[AVScheduledParameterRamp _defaultAdditionalFigRepresentationObjects];
+[AVScheduledParameterRamp scheduledParameterRampWithPropertyList:];
```

## Instance methods

```
-[AVScheduledParameterRamp initWithPropertyList:];
-[AVScheduledParameterRamp timeRange];
-[AVScheduledParameterRamp propertyList];
-[AVScheduledParameterRamp hash];
-[AVScheduledParameterRamp description];
-[AVScheduledParameterRamp copyWithZone:];
-[AVScheduledParameterRamp isEqual:];
-[AVScheduledParameterRamp _additionalFigRepresentationObjects];
-[AVScheduledParameterRamp endValue];
-[AVScheduledParameterRamp initWithTimeRange:];
-[AVScheduledParameterRamp scheduledParameterRampInterpolatedToTime:];
-[AVScheduledParameterRamp startValue];
```
