# `CMDyskineticSymptomResult`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
f _percentUnlikely;
f _percentLikely;
@"NSDate" _startDate;
@"NSDate" _endDate;
```

## Properties

```
@property (T@"NSDate",R,C,N,V_startDate) startDate;
@property (T@"NSDate",R,C,N,V_endDate) endDate;
@property (Tf,R,N,V_percentUnlikely) percentUnlikely;
@property (Tf,R,N,V_percentLikely) percentLikely;
```

## Class methods

```
+[CMDyskineticSymptomResult supportsSecureCoding];
```

## Instance methods

```
-[CMDyskineticSymptomResult startDate];
-[CMDyskineticSymptomResult dealloc];
-[CMDyskineticSymptomResult endDate];
-[CMDyskineticSymptomResult encodeWithCoder:];
-[CMDyskineticSymptomResult description];
-[CMDyskineticSymptomResult initWithCoder:];
-[CMDyskineticSymptomResult copyWithZone:];
-[CMDyskineticSymptomResult percentUnlikely];
-[CMDyskineticSymptomResult initWithParkinsonsResult:];
-[CMDyskineticSymptomResult initWithStartDate:endDate:percentDyskinesiaUnlikely:percentDyskinesiaLikely:];
-[CMDyskineticSymptomResult percentLikely];
```
