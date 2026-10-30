# `Histogram`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _bins;
I _index;
{?="index"b1} _has;
```

## Properties

```
@property (TB,N) hasIndex;
@property (TI,N,V_index) index;
@property (T@"NSMutableArray",&,N,V_bins) bins;
```

## Class methods

```
+[Histogram binType];
```

## Instance methods

```
-[Histogram writeTo:];
-[Histogram mergeFrom:];
-[Histogram index];
-[Histogram setIndex:];
-[Histogram hash];
-[Histogram copyTo:];
-[Histogram setHasIndex:];
-[Histogram description];
-[Histogram readFrom:];
-[Histogram copyWithZone:];
-[Histogram isEqual:];
-[Histogram hasIndex];
-[Histogram dictionaryRepresentation];
-[Histogram bins];
-[Histogram setBins:];
-[Histogram addBin:];
-[Histogram binAtIndex:];
-[Histogram binsCount];
-[Histogram clearBins];
```
