# `UIPageControlTimerProgress`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPageControlProgress`
- 9 instance variables, 7 properties, 27 instance methods, 0 class methods

## Instance variables

```
d _previousTime;
d _currentDuration;
d _currentDurationProgress;
{?="progressDidChange"b1"shouldAdvanceToPage"b1} _delegateImplements;
B _resetsToInitialPageAfterEnd;
B _enableTimer;
d _preferredDuration;
@"NSMutableDictionary" _customDurationByPage;
@"CADisplayLink" _displayLink;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_customDurationByPage) customDurationByPage;
@property (T@"CADisplayLink",&,N,V_displayLink) displayLink;
@property (TB,N,V_enableTimer) enableTimer;
@property (T@"<UIPageControlTimerProgressDelegate>",W,D,N) delegate;
@property (TB,N,V_resetsToInitialPageAfterEnd) resetsToInitialPageAfterEnd;
@property (TB,R,N,GisRunning) running;
@property (Td,N,V_preferredDuration) preferredDuration;
```

## Instance methods

```
-[UIPageControlTimerProgress isRunning];
-[UIPageControlTimerProgress displayLink];
-[UIPageControlTimerProgress setCurrentProgress:];
-[UIPageControlTimerProgress dealloc];
-[UIPageControlTimerProgress setDisplayLink:];
-[UIPageControlTimerProgress setPageControl:];
-[UIPageControlTimerProgress setDelegate:];
-[UIPageControlTimerProgress setEnableTimer:];
-[UIPageControlTimerProgress setResetsToInitialPageAfterEnd:];
-[UIPageControlTimerProgress _canInstallTimer];
-[UIPageControlTimerProgress _didChangeCurrentPage];
-[UIPageControlTimerProgress _displayLinkTicked:];
-[UIPageControlTimerProgress _pageControlDidMoveToWindow];
-[UIPageControlTimerProgress _progressVisibilityChanged:];
-[UIPageControlTimerProgress _shouldAdvanceToPage:];
-[UIPageControlTimerProgress _updateTimer];
-[UIPageControlTimerProgress customDurationByPage];
-[UIPageControlTimerProgress durationForPage:];
-[UIPageControlTimerProgress enableTimer];
-[UIPageControlTimerProgress initWithPreferredDuration:];
-[UIPageControlTimerProgress pauseTimer];
-[UIPageControlTimerProgress preferredDuration];
-[UIPageControlTimerProgress resetsToInitialPageAfterEnd];
-[UIPageControlTimerProgress resumeTimer];
-[UIPageControlTimerProgress setCustomDurationByPage:];
-[UIPageControlTimerProgress setDuration:forPage:];
-[UIPageControlTimerProgress setPreferredDuration:];
```
