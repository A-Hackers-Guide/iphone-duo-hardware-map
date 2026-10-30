# `BKMousePointerCAAnimationDriver`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKMousePointerAnimationDriver`
- 6 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"BSAnimationSettings" _animationSettings;
d _duration;
d _elapsedTime;
@"CABasicAnimation" _animation;
@"NSMutableDictionary" _valueDictionary;
{CGPoint="x"d"y"d} _currentTranslation;
```

## Instance methods

```
-[BKMousePointerCAAnimationDriver isComplete];
-[BKMousePointerCAAnimationDriver currentTranslation];
-[BKMousePointerCAAnimationDriver applyForTime:];
-[BKMousePointerCAAnimationDriver initWithRelativeTranslation:animationSettings:];
```
