# `CBHistogramBuilder`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBHistogram`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _bins;
@"NSArray" _edges;
```

## Properties

```
@property (T@"NSMutableArray",R,V_bins) bins;
@property (T@"NSArray",R,V_edges) edges;
```

## Instance methods

```
-[CBHistogramBuilder edges];
-[CBHistogramBuilder dealloc];
-[CBHistogramBuilder reset];
-[CBHistogramBuilder initWithEdges:];
-[CBHistogramBuilder bins];
-[CBHistogramBuilder enumerateBinsUsingBlock:];
-[CBHistogramBuilder pushNumber:];
-[CBHistogramBuilder pushNumberWeighted:withWeight:];
```
