# `SRAudioLevel`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 10 instance methods, 2 class methods

## Instance variables

```
d _loudness;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _timeRange;
```

## Properties

```
@property (T{?={?=qiIq}{?=qiIq}},R,N,V_timeRange) timeRange;
@property (Td,R,N,V_loudness) loudness;
```

## Class methods

```
+[SRAudioLevel supportsSecureCoding];
+[SRAudioLevel new];
```

## Instance methods

```
-[SRAudioLevel timeRange];
-[SRAudioLevel init];
-[SRAudioLevel encodeWithCoder:];
-[SRAudioLevel hash];
-[SRAudioLevel description];
-[SRAudioLevel initWithCoder:];
-[SRAudioLevel copyWithZone:];
-[SRAudioLevel isEqual:];
-[SRAudioLevel loudness];
-[SRAudioLevel initWithTimeRange:loudness:];
```
