# `MLNearestNeighborsLinearIndex`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLNearestNeighborsIndex`, `NSSecureCoding`
- 4 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} vData;
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} vDataL2Squared;
Q _numDataPoints;
Q _numDimensions;
```

## Properties

```
@property (TQ,N,V_numDataPoints) numDataPoints;
@property (TQ,N,V_numDimensions) numDimensions;
```

## Class methods

```
+[MLNearestNeighborsLinearIndex supportsSecureCoding];
```

## Instance methods

```
-[MLNearestNeighborsLinearIndex encodeWithCoder:];
-[MLNearestNeighborsLinearIndex initWithCoder:];
-[MLNearestNeighborsLinearIndex dataPointCount];
-[MLNearestNeighborsLinearIndex findNearestNeighbors:toIndex:];
-[MLNearestNeighborsLinearIndex findNearestNeighbors:toQueryPoint:];
-[MLNearestNeighborsLinearIndex initWithDataset:numberOfDimensions:];
-[MLNearestNeighborsLinearIndex numDataPoints];
-[MLNearestNeighborsLinearIndex numDimensions];
-[MLNearestNeighborsLinearIndex setNumDataPoints:];
-[MLNearestNeighborsLinearIndex setNumDimensions:];
-[MLNearestNeighborsLinearIndex updateWithData:error:];
```
