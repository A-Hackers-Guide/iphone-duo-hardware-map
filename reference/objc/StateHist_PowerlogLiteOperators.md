# `StateHist`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _bins;
I _state;
{?="state"b1} _has;
```

## Properties

```
@property (TB,N) hasState;
@property (TI,N,V_state) state;
@property (T@"NSMutableArray",&,N,V_bins) bins;
```

## Class methods

```
+[StateHist binType];
```

## Instance methods

```
-[StateHist writeTo:];
-[StateHist setState:];
-[StateHist mergeFrom:];
-[StateHist hasState];
-[StateHist hash];
-[StateHist copyTo:];
-[StateHist description];
-[StateHist readFrom:];
-[StateHist copyWithZone:];
-[StateHist setHasState:];
-[StateHist isEqual:];
-[StateHist state];
-[StateHist dictionaryRepresentation];
-[StateHist bins];
-[StateHist setBins:];
-[StateHist addBin:];
-[StateHist binAtIndex:];
-[StateHist binsCount];
-[StateHist clearBins];
```
