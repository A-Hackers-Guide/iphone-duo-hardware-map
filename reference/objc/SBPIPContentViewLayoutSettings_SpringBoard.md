# `SBPIPContentViewLayoutSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"SBPIPContentViewLayoutContext" _context;
@"SBPIPContentViewLayoutMetrics" _platformMetrics;
@"SBPIPDefaults" _pipDefaults;
```

## Class methods

```
+[SBPIPContentViewLayoutSettings pipDefaults];
```

## Instance methods

```
-[SBPIPContentViewLayoutSettings defaultCornerRadius];
-[SBPIPContentViewLayoutSettings platformMetrics];
-[SBPIPContentViewLayoutSettings contentViewPadding];
-[SBPIPContentViewLayoutSettings setContentViewSize:];
-[SBPIPContentViewLayoutSettings _contentViewSizeForAspectRatio:currentSize:];
-[SBPIPContentViewLayoutSettings _maximumContentViewSizeForAspectRatio:maximumReferenceSize:];
-[SBPIPContentViewLayoutSettings _minimumContentViewSizeForAspectRatio:minimumReferenceSize:];
-[SBPIPContentViewLayoutSettings contentViewPaddingWhileStashed];
-[SBPIPContentViewLayoutSettings currentContentViewPosition];
-[SBPIPContentViewLayoutSettings currentContentViewSizeForAspectRatio:];
-[SBPIPContentViewLayoutSettings defaultContentViewSizeForAspectRatio:forSurfaceType:];
-[SBPIPContentViewLayoutSettings initWithPlatformMetrics:contentSize:];
-[SBPIPContentViewLayoutSettings maximumPossibleContentViewSizeForAspectRatio:];
-[SBPIPContentViewLayoutSettings maximumPreferredContentViewSizeForAspectRatio:];
-[SBPIPContentViewLayoutSettings minimumPossibleContentViewSizeForAspectRatio:];
-[SBPIPContentViewLayoutSettings minimumPreferredContentViewSizeForAspectRatio:];
-[SBPIPContentViewLayoutSettings minimumStashedTabSize];
-[SBPIPContentViewLayoutSettings setContentViewPosition:];
-[SBPIPContentViewLayoutSettings setMaximumSizeSpanForPreferredSizeTuning:];
-[SBPIPContentViewLayoutSettings setMinimumSizeSpanBetweenPreferredSizes:];
-[SBPIPContentViewLayoutSettings updateCurrentContentViewSize:];
-[SBPIPContentViewLayoutSettings updatePlatformMetrics:];
```
