# `BKMousePointerAnimationDriver`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _relativeTranslation;
{CGPoint="x"d"y"d} _currentTranslation;
```

## Properties

```
@property (T{CGPoint=dd},R,N,V_relativeTranslation) relativeTranslation;
@property (T{CGPoint=dd},R,N,V_currentTranslation) currentTranslation;
@property (TB,R,N,GisComplete) complete;
```

## Instance methods

```
-[BKMousePointerAnimationDriver isComplete];
-[BKMousePointerAnimationDriver currentTranslation];
-[BKMousePointerAnimationDriver applyForTime:];
-[BKMousePointerAnimationDriver initWithRelativeTranslation:];
-[BKMousePointerAnimationDriver relativeTranslation];
```
