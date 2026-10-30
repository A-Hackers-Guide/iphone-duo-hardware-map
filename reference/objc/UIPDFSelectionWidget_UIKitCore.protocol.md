# `UIPDFSelectionWidget` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 3 properties, 15 instance methods, 0 class methods

## Properties

```
@property (T{CGPoint=dd},R,N) initialSelectionPointOnPage;
@property (T{CGPoint=dd},R,N) currentSelectionPointOnPage;
@property (T@"UIPDFPageView",N) pageView;
```

## Instance methods

```
-[UIPDFSelectionWidget hide];
-[UIPDFSelectionWidget setSelection:];
-[UIPDFSelectionWidget remove];
-[UIPDFSelectionWidget layout];
-[UIPDFSelectionWidget currentSelectionPointOnPage];
-[UIPDFSelectionWidget endTracking];
-[UIPDFSelectionWidget hitTest:fixedPoint:preceeds:];
-[UIPDFSelectionWidget initialSelectionPointOnPage];
-[UIPDFSelectionWidget pageView];
-[UIPDFSelectionWidget selectedPointFor:];
-[UIPDFSelectionWidget selectionRectangle];
-[UIPDFSelectionWidget setPageView:];
-[UIPDFSelectionWidget setSelectedGrabber:];
-[UIPDFSelectionWidget track:];
-[UIPDFSelectionWidget viewOffset];
```
