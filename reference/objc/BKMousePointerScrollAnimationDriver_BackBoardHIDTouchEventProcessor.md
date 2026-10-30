# `BKMousePointerScrollAnimationDriver`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKMousePointerAnimationDriver`
- 6 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _initialVelocity;
d _decelerationRate;
{CGPoint="x"d"y"d} _intermediate;
{CGPoint="x"d"y"d} _target;
d _elapsedTime;
{CGPoint="x"d"y"d} _currentTranslation;
```

## Instance methods

```
-[BKMousePointerScrollAnimationDriver isComplete];
-[BKMousePointerScrollAnimationDriver currentTranslation];
-[BKMousePointerScrollAnimationDriver applyForTime:];
-[BKMousePointerScrollAnimationDriver initWithRelativeTranslation:initialVelocity:decelerationRate:];
```
