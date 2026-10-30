# `BWMovingWindowStats`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWMedianStats`
- 2 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
i _windowSize;
i _dataPointIndex;
```

## Properties

```
@property (Ti,R,N,V_windowSize) windowSize;
```

## Instance methods

```
-[BWMovingWindowStats addDataPointP:];
-[BWMovingWindowStats dealloc];
-[BWMovingWindowStats windowSize];
-[BWMovingWindowStats reset];
-[BWMovingWindowStats description];
-[BWMovingWindowStats copyWithZone:];
-[BWMovingWindowStats initWithWindowSize:];
```
