# `CStat`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
I _activeDurMs;
I _ident;
I _idleDurMs;
I _sleepDurMs;
I _sleepEntryCount;
{?="activeDurMs"b1"ident"b1"idleDurMs"b1"sleepDurMs"b1"sleepEntryCount"b1} _has;
```

## Properties

```
@property (TB,N) hasIdent;
@property (TI,N,V_ident) ident;
@property (TB,N) hasSleepDurMs;
@property (TI,N,V_sleepDurMs) sleepDurMs;
@property (TB,N) hasIdleDurMs;
@property (TI,N,V_idleDurMs) idleDurMs;
@property (TB,N) hasActiveDurMs;
@property (TI,N,V_activeDurMs) activeDurMs;
@property (TB,N) hasSleepEntryCount;
@property (TI,N,V_sleepEntryCount) sleepEntryCount;
```

## Instance methods

```
-[CStat writeTo:];
-[CStat mergeFrom:];
-[CStat hash];
-[CStat copyTo:];
-[CStat description];
-[CStat readFrom:];
-[CStat copyWithZone:];
-[CStat isEqual:];
-[CStat dictionaryRepresentation];
-[CStat ident];
-[CStat setActiveDurMs:];
-[CStat sleepEntryCount];
-[CStat activeDurMs];
-[CStat hasActiveDurMs];
-[CStat hasIdent];
-[CStat hasIdleDurMs];
-[CStat hasSleepDurMs];
-[CStat hasSleepEntryCount];
-[CStat idleDurMs];
-[CStat setHasActiveDurMs:];
-[CStat setHasIdent:];
-[CStat setHasIdleDurMs:];
-[CStat setHasSleepDurMs:];
-[CStat setHasSleepEntryCount:];
-[CStat setIdent:];
-[CStat setIdleDurMs:];
-[CStat setSleepDurMs:];
-[CStat setSleepEntryCount:];
-[CStat sleepDurMs];
```
