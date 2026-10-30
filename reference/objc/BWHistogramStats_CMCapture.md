# `BWHistogramStats`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStats`
- 5 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
^d _bins;
^Q _counts;
^d _areas;
Q _binsCount;
d _estimatedMedian;
```

## Properties

```
@property (T@"NSDictionary",R,N) histogramAsDictionary;
@property (Td,R,N,V_estimatedMedian) estimatedMedian;
```

## Instance methods

```
-[BWHistogramStats addDataPointP:];
-[BWHistogramStats dealloc];
-[BWHistogramStats reset];
-[BWHistogramStats histogramAsDictionary];
-[BWHistogramStats estimatedMedian];
-[BWHistogramStats getEstimatedQuantiles:n:];
-[BWHistogramStats initWithBins:];
```
