# `AVFloat64Range`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 2 properties, 8 instance methods, 2 class methods

## Instance variables

```
d _minimum;
d _maximum;
```

## Properties

```
@property (Td,R,N,V_minimum) minimum;
@property (Td,R,N,V_maximum) maximum;
```

## Class methods

```
+[AVFloat64Range float64RangeWithAudioValueRange:];
+[AVFloat64Range float64RangeWithMinimum:maximum:];
```

## Instance methods

```
-[AVFloat64Range minimum];
-[AVFloat64Range maximum];
-[AVFloat64Range hash];
-[AVFloat64Range description];
-[AVFloat64Range copyWithZone:];
-[AVFloat64Range isEqual:];
-[AVFloat64Range initWithAudioValueRange:];
-[AVFloat64Range initWithMinimum:maximum:];
```
