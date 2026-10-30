# `UIScrollTestParameters`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 10 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSString" _testName;
q _iterations;
d _delta;
d _length;
Q _axis;
@? _extraResultsBlock;
d _startOffset;
@"CADisplayLink" _displayLink;
@? _completionBlock;
```

## Properties

```
@property (Td,N,V_startOffset) startOffset;
@property (Td,R,N) endOffset;
@property (T@"CADisplayLink",&,N,V_displayLink) displayLink;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (T@"NSString",C,N,V_testName) testName;
@property (Tq,N,V_iterations) iterations;
@property (Td,N,V_delta) delta;
@property (Td,N,V_length) length;
@property (TQ,N,V_axis) axis;
@property (T@?,C,N,V_extraResultsBlock) extraResultsBlock;
```

## Instance methods

```
-[UIScrollTestParameters displayLink];
-[UIScrollTestParameters axis];
-[UIScrollTestParameters setCompletionBlock:];
-[UIScrollTestParameters completionBlock];
-[UIScrollTestParameters setAxis:];
-[UIScrollTestParameters init];
-[UIScrollTestParameters iterations];
-[UIScrollTestParameters dealloc];
-[UIScrollTestParameters setIterations:];
-[UIScrollTestParameters length];
-[UIScrollTestParameters setDisplayLink:];
-[UIScrollTestParameters startOffset];
-[UIScrollTestParameters copyWithZone:];
-[UIScrollTestParameters setLength:];
-[UIScrollTestParameters setStartOffset:];
-[UIScrollTestParameters delta];
-[UIScrollTestParameters endOffset];
-[UIScrollTestParameters extraResultsBlock];
-[UIScrollTestParameters setDelta:];
-[UIScrollTestParameters setExtraResultsBlock:];
-[UIScrollTestParameters setTestName:];
-[UIScrollTestParameters testName];
```
