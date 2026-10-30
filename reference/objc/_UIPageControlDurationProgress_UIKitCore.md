# `_UIPageControlDurationProgress`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPageControlTimerProgress`
- 1 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
{?="shouldAdvanceToPageSPI"b1} _delegateImplements;
```

## Properties

```
@property (T@"<_UIPageControlDurationProgressDelegate>",W,D,N) delegate;
@property (Td,N) pageDuration;
@property (TB,N) resetsToInitialPageAtEnd;
```

## Instance methods

```
-[_UIPageControlDurationProgress pause];
-[_UIPageControlDurationProgress setDelegate:];
-[_UIPageControlDurationProgress resume];
-[_UIPageControlDurationProgress _shouldAdvanceToPage:];
-[_UIPageControlDurationProgress initWithPageDuration:];
-[_UIPageControlDurationProgress pageDuration];
-[_UIPageControlDurationProgress pageDurationForPage:];
-[_UIPageControlDurationProgress resetsToInitialPageAtEnd];
-[_UIPageControlDurationProgress setCustomPageDuration:forPage:];
-[_UIPageControlDurationProgress setPageDuration:];
-[_UIPageControlDurationProgress setResetsToInitialPageAtEnd:];
```
