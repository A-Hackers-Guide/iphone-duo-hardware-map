# `SBHSearchPresenting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 6 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"<SBHSearchPresenterDelegate>",W,N) searchPresenterDelegate;
@property (TB,R,N,GisPresenting) presenting;
@property (Tq,R,N) presentationState;
@property (Td,R,N) presentationProgress;
@property (Td,R,N) presentationOffset;
@property (T{SBHSearchInteractivePresentationMetrics=dddd},N) interactivePresentationMetrics;
```

## Instance methods

```
-[SBHSearchPresenting presentationState];
-[SBHSearchPresenting scrollViewWillBeginDragging:];
-[SBHSearchPresenting layout];
-[SBHSearchPresenting scrollViewWillEndDragging:withVelocity:];
-[SBHSearchPresenting scrollViewDidScroll:];
-[SBHSearchPresenting isPresenting];
-[SBHSearchPresenting addSearchPresenterObserver:];
-[SBHSearchPresenting dismissSearchAnimated:];
-[SBHSearchPresenting interactivePresentationMetrics];
-[SBHSearchPresenting presentSearchAnimated:];
-[SBHSearchPresenting presentationOffset];
-[SBHSearchPresenting removeSearchPresenterObserver:];
-[SBHSearchPresenting presentationProgress];
-[SBHSearchPresenting searchPresenterDelegate];
-[SBHSearchPresenting setInteractivePresentationMetrics:];
-[SBHSearchPresenting setSearchPresenterDelegate:];
```
