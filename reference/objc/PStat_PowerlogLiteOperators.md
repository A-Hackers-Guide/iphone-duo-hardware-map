# `PStat`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 29 instance methods, 0 class methods

## Instance variables

```
I _activeDurMs;
I _ident;
I _inactiveDurMs;
I _sleepBlockCount;
I _toActiveCount;
{?="activeDurMs"b1"ident"b1"inactiveDurMs"b1"sleepBlockCount"b1"toActiveCount"b1} _has;
```

## Properties

```
@property (TB,N) hasIdent;
@property (TI,N,V_ident) ident;
@property (TB,N) hasActiveDurMs;
@property (TI,N,V_activeDurMs) activeDurMs;
@property (TB,N) hasInactiveDurMs;
@property (TI,N,V_inactiveDurMs) inactiveDurMs;
@property (TB,N) hasToActiveCount;
@property (TI,N,V_toActiveCount) toActiveCount;
@property (TB,N) hasSleepBlockCount;
@property (TI,N,V_sleepBlockCount) sleepBlockCount;
```

## Instance methods

```
-[PStat writeTo:];
-[PStat mergeFrom:];
-[PStat hash];
-[PStat copyTo:];
-[PStat description];
-[PStat readFrom:];
-[PStat copyWithZone:];
-[PStat isEqual:];
-[PStat dictionaryRepresentation];
-[PStat ident];
-[PStat setActiveDurMs:];
-[PStat sleepBlockCount];
-[PStat activeDurMs];
-[PStat hasActiveDurMs];
-[PStat hasIdent];
-[PStat hasInactiveDurMs];
-[PStat hasSleepBlockCount];
-[PStat hasToActiveCount];
-[PStat inactiveDurMs];
-[PStat setHasActiveDurMs:];
-[PStat setHasIdent:];
-[PStat setHasInactiveDurMs:];
-[PStat setHasSleepBlockCount:];
-[PStat setHasToActiveCount:];
-[PStat setIdent:];
-[PStat setInactiveDurMs:];
-[PStat setSleepBlockCount:];
-[PStat setToActiveCount:];
-[PStat toActiveCount];
```
