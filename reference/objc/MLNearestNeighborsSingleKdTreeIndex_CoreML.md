# `MLNearestNeighborsSingleKdTreeIndex`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLNearestNeighborsIndex`, `NSSecureCoding`
- 5 instance variables, 3 properties, 17 instance methods, 1 class methods

## Instance variables

```
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} vData;
{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} vIndices;
Q _numDimensions;
Q _leafSize;
@"_KDNode" _root;
```

## Properties

```
@property (TQ,N,V_numDimensions) numDimensions;
@property (TQ,N,V_leafSize) leafSize;
@property (T@"_KDNode",&,N,V_root) root;
```

## Class methods

```
+[MLNearestNeighborsSingleKdTreeIndex supportsSecureCoding];
```

## Instance methods

```
-[MLNearestNeighborsSingleKdTreeIndex root];
-[MLNearestNeighborsSingleKdTreeIndex encodeWithCoder:];
-[MLNearestNeighborsSingleKdTreeIndex initWithCoder:];
-[MLNearestNeighborsSingleKdTreeIndex setRoot:];
-[MLNearestNeighborsSingleKdTreeIndex calculateDistancesForNodesBetweenLeft:andRight:toQueryPoint:];
-[MLNearestNeighborsSingleKdTreeIndex constructTree];
-[MLNearestNeighborsSingleKdTreeIndex constructTreeForPointsBoundedBy:startingIndex:count:];
-[MLNearestNeighborsSingleKdTreeIndex dataPointCount];
-[MLNearestNeighborsSingleKdTreeIndex findK:nearestNeighbors:toQueryPoint:inTree:];
-[MLNearestNeighborsSingleKdTreeIndex findNearestNeighbors:toIndex:];
-[MLNearestNeighborsSingleKdTreeIndex findNearestNeighbors:toQueryPoint:];
-[MLNearestNeighborsSingleKdTreeIndex initWithDataset:numberOfDimensions:leafSize:error:];
-[MLNearestNeighborsSingleKdTreeIndex leafSize];
-[MLNearestNeighborsSingleKdTreeIndex numDimensions];
-[MLNearestNeighborsSingleKdTreeIndex setLeafSize:];
-[MLNearestNeighborsSingleKdTreeIndex setNumDimensions:];
-[MLNearestNeighborsSingleKdTreeIndex updateWithData:error:];
```
