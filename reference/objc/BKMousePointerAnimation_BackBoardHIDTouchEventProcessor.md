# `BKMousePointerAnimation`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _relativeTranslation;
{CGPoint="x"d"y"d} _destinationPoint;
q _targetFPS;
{CGPoint="x"d"y"d} _lastSentOriginRelativeOffset;
@"CADisplayLink" _displayLink;
@"BKMousePointerAnimationDriver" _animationDriver;
@? _applierBlock;
@? _completionBlock;
d _initialTimestamp;
```

## Properties

```
@property (T{CGPoint=dd},R,N,V_destinationPoint) destinationPoint;
```

## Instance methods

```
-[BKMousePointerAnimation isComplete];
-[BKMousePointerAnimation stop];
-[BKMousePointerAnimation start];
-[BKMousePointerAnimation displayLinkFired:];
-[BKMousePointerAnimation destinationPoint];
-[BKMousePointerAnimation initWithRelativeTranslation:destinationPoint:animationDriver:updateRate:applierBlock:completionBlock:];
```
