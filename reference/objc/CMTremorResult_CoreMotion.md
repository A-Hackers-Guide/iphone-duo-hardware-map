# `CMTremorResult`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 15 instance methods, 1 class methods

## Instance variables

```
f _percentUnknown;
f _percentNone;
f _percentSlight;
f _percentMild;
f _percentModerate;
f _percentStrong;
@"NSDate" _startDate;
@"NSDate" _endDate;
```

## Properties

```
@property (T@"NSDate",R,C,N,V_startDate) startDate;
@property (T@"NSDate",R,C,N,V_endDate) endDate;
@property (Tf,R,N,V_percentUnknown) percentUnknown;
@property (Tf,R,N,V_percentNone) percentNone;
@property (Tf,R,N,V_percentSlight) percentSlight;
@property (Tf,R,N,V_percentMild) percentMild;
@property (Tf,R,N,V_percentModerate) percentModerate;
@property (Tf,R,N,V_percentStrong) percentStrong;
```

## Class methods

```
+[CMTremorResult supportsSecureCoding];
```

## Instance methods

```
-[CMTremorResult startDate];
-[CMTremorResult dealloc];
-[CMTremorResult endDate];
-[CMTremorResult encodeWithCoder:];
-[CMTremorResult description];
-[CMTremorResult initWithCoder:];
-[CMTremorResult copyWithZone:];
-[CMTremorResult percentModerate];
-[CMTremorResult initWithParkinsonsResult:];
-[CMTremorResult initWithStartDate:endDate:percentUnknown:percentNone:percentSlight:percentMild:percentModerate:percentStrong:];
-[CMTremorResult percentMild];
-[CMTremorResult percentNone];
-[CMTremorResult percentSlight];
-[CMTremorResult percentStrong];
-[CMTremorResult percentUnknown];
```
