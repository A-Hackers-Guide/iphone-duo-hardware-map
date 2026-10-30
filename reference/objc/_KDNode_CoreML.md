# `_KDNode`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 9 instance variables, 9 properties, 24 instance methods, 1 class methods

## Instance variables

```
B _isLeaf;
f _splitValue;
Q _splitDimension;
Q _splitIndex;
Q _startingIndex;
Q _count;
@"_KDNode" _leftChild;
@"_KDNode" _rightChild;
{_KDBoundingBox="_intervals"{vector<_KDInterval, std::allocator<_KDInterval>>="__begin_"^{_KDInterval}"__end_"^{_KDInterval}""{?="__cap_"^{_KDInterval}}}"_numDimensions"Q} _boundingBox;
```

## Properties

```
@property (TQ,N,V_splitDimension) splitDimension;
@property (TQ,N,V_splitIndex) splitIndex;
@property (Tf,N,V_splitValue) splitValue;
@property (TQ,N,V_startingIndex) startingIndex;
@property (TQ,N,V_count) count;
@property (T@"_KDNode",&,N,V_leftChild) leftChild;
@property (T@"_KDNode",&,N,V_rightChild) rightChild;
@property (T{_KDBoundingBox={vector<_KDInterval, std::allocator<_KDInterval>>=^{_KDInterval}^{_KDInterval}{?=^{_KDInterval}}}Q},N,V_boundingBox) boundingBox;
@property (TB,N,V_isLeaf) isLeaf;
```

## Class methods

```
+[_KDNode supportsSecureCoding];
```

## Instance methods

```
-[_KDNode setBoundingBox:];
-[_KDNode setCount:];
-[_KDNode count];
-[_KDNode boundingBox];
-[_KDNode splitIndex];
-[_KDNode encodeWithCoder:];
-[_KDNode initWithCoder:];
-[_KDNode print];
-[_KDNode isLeaf];
-[_KDNode assignSplitsForData:indices:numDimensions:];
-[_KDNode findMin:andMax:alongDimension:data:indices:numDimensions:];
-[_KDNode leftChild];
-[_KDNode partitionDataPoints:indices:numDimensions:];
-[_KDNode rightChild];
-[_KDNode setIsLeaf:];
-[_KDNode setLeftChild:];
-[_KDNode setRightChild:];
-[_KDNode setSplitDimension:];
-[_KDNode setSplitIndex:];
-[_KDNode setSplitValue:];
-[_KDNode setStartingIndex:];
-[_KDNode splitDimension];
-[_KDNode splitValue];
-[_KDNode startingIndex];
```
