# `UIPageControlProgress`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
{?="initialProgressForPage"b1"visibilityDidChange"b1} _delegateImplements;
B _progressVisible;
f _currentProgress;
@"<UIPageControlProgressDelegate>" _delegate;
@"UIPageControl" _pageControl;
```

## Properties

```
@property (T@"UIPageControl",W,N,V_pageControl) pageControl;
@property (T@"<UIPageControlProgressDelegate>",W,N,V_delegate) delegate;
@property (Tf,N,V_currentProgress) currentProgress;
@property (TB,R,N,GisProgressVisible,V_progressVisible) progressVisible;
```

## Instance methods

```
-[UIPageControlProgress setCurrentProgress:];
-[UIPageControlProgress init];
-[UIPageControlProgress setPageControl:];
-[UIPageControlProgress pageControl];
-[UIPageControlProgress setDelegate:];
-[UIPageControlProgress delegate];
-[UIPageControlProgress currentProgress];
-[UIPageControlProgress _didChangeCurrentPage];
-[UIPageControlProgress _initialProgressForPage:];
-[UIPageControlProgress _pageControlDidMoveToWindow];
-[UIPageControlProgress _progressVisibilityChanged:];
-[UIPageControlProgress isProgressVisible];
```
