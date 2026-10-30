# `BWStats`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
d _multiplier;
@"NSString" _unitDesignator;
q _numberOfSamples;
d _min;
d _max;
d _sumX;
d _sumXX;
```

## Properties

```
@property (Td,N,V_multiplier) multiplier;
@property (T@"NSString",C,N,V_unitDesignator) unitDesignator;
@property (Tq,R,N,V_numberOfSamples) numberOfSamples;
@property (Td,R,N) min;
@property (Td,R,N) max;
@property (Td,R,N) average;
@property (Td,R,N) standardDeviation;
```

## Instance methods

```
-[BWStats min];
-[BWStats addDataPointP:];
-[BWStats debugDescription];
-[BWStats unitDesignator];
-[BWStats init];
-[BWStats dealloc];
-[BWStats setMultiplier:];
-[BWStats multiplier];
-[BWStats reset];
-[BWStats numberOfSamples];
-[BWStats addDataPoint:];
-[BWStats max];
-[BWStats description];
-[BWStats standardDeviation];
-[BWStats copyWithZone:];
-[BWStats setUnitDesignator:];
-[BWStats initWithStats:];
-[BWStats average];
```
