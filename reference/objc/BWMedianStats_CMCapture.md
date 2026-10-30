# `BWMedianStats`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStats`
- 2 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
q _maxNumberOfSamplesForMedianCalculation;
@"NSMutableArray" _samples;
```

## Properties

```
@property (Td,R,N) median;
```

## Instance methods

```
-[BWMedianStats addDataPointP:];
-[BWMedianStats median];
-[BWMedianStats dealloc];
-[BWMedianStats reset];
-[BWMedianStats initWithMaxNumberOfSamplesForMedianCalculation:];
-[BWMedianStats description];
-[BWMedianStats copyWithZone:];
```
