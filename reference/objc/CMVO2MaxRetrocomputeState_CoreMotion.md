# `CMVO2MaxRetrocomputeState`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
q _status;
@"NSDate" _startDate;
@"NSDate" _endDate;
@"NSNumber" _meanDelta;
```

## Properties

```
@property (Tq,R,N,V_status) status;
@property (T@"NSDate",R,&,N,V_startDate) startDate;
@property (T@"NSDate",R,&,N,V_endDate) endDate;
@property (T@"NSNumber",R,&,N,V_meanDelta) meanDelta;
```

## Class methods

```
+[CMVO2MaxRetrocomputeState supportsSecureCoding];
```

## Instance methods

```
-[CMVO2MaxRetrocomputeState startDate];
-[CMVO2MaxRetrocomputeState dealloc];
-[CMVO2MaxRetrocomputeState endDate];
-[CMVO2MaxRetrocomputeState status];
-[CMVO2MaxRetrocomputeState encodeWithCoder:];
-[CMVO2MaxRetrocomputeState description];
-[CMVO2MaxRetrocomputeState initWithCoder:];
-[CMVO2MaxRetrocomputeState copyWithZone:];
-[CMVO2MaxRetrocomputeState initWithStatus:startDate:endDate:meanDelta:];
-[CMVO2MaxRetrocomputeState meanDelta];
```
