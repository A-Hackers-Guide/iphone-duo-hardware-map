# `CMVO2MaxPriorData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 13 instance methods, 2 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
d fPriorValue;
q fPlatformSource;
d fMeanMaxMets;
```

## Properties

```
@property (TQ,R,N) recordId;
@property (T@"NSDate",R,N) startDate;
@property (Tq,R,N) platformSource;
@property (Td,R,N) meanMaxMets;
@property (Td,R,N) priorValue;
```

## Class methods

```
+[CMVO2MaxPriorData supportsSecureCoding];
+[CMVO2MaxPriorData VO2MaxPriorFromCMVO2MaxPriorData:];
```

## Instance methods

```
-[CMVO2MaxPriorData startDate];
-[CMVO2MaxPriorData recordId];
-[CMVO2MaxPriorData dealloc];
-[CMVO2MaxPriorData priorValue];
-[CMVO2MaxPriorData encodeWithCoder:];
-[CMVO2MaxPriorData description];
-[CMVO2MaxPriorData initWithCoder:];
-[CMVO2MaxPriorData copyWithZone:];
-[CMVO2MaxPriorData isEqual:];
-[CMVO2MaxPriorData initWithSample:];
-[CMVO2MaxPriorData initWithRecordId:startDate:priorValue:platformSource:meanMaxMets:];
-[CMVO2MaxPriorData meanMaxMets];
-[CMVO2MaxPriorData platformSource];
```
