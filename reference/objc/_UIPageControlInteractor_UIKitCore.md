# `_UIPageControlInteractor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
d _scrubbingOffset;
d _lowerBound;
d _upperBound;
@"_UIHyperInteractor" _interactor;
```

## Properties

```
@property (T@"_UIHyperInteractor",&,N,V_interactor) interactor;
@property (Td,R,N) joggingDistance;
@property (Td,R,N) unconstrainedPosition;
@property (Td,R,N) boundedScrubPosition;
@property (Td,R,N) unboundedScrubPosition;
@property (Td,R,N) hyperConstrainedPosition;
```

## Instance methods

```
-[_UIPageControlInteractor commitTranslation];
-[_UIPageControlInteractor interactor];
-[_UIPageControlInteractor hyperConstrainedPosition];
-[_UIPageControlInteractor reduceScrubOffsetByOffset:];
-[_UIPageControlInteractor boundedScrubPosition];
-[_UIPageControlInteractor unconstrainedPosition];
-[_UIPageControlInteractor setInteractor:];
-[_UIPageControlInteractor updateRubberbandLowerBound:upperBound:];
-[_UIPageControlInteractor unboundedScrubPosition];
-[_UIPageControlInteractor setUnconstrainedPosition:offset:];
-[_UIPageControlInteractor initWithMaximumDistance:];
-[_UIPageControlInteractor reduceScrubOffsetByRatio:];
-[_UIPageControlInteractor updateScrubLowerBound:upperBound:];
-[_UIPageControlInteractor joggingDistance];
-[_UIPageControlInteractor setTranslation:velocity:];
```
