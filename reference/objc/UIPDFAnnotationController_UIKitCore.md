# `UIPDFAnnotationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`
- 13 instance variables, 12 properties, 65 instance methods, 3 class methods

## Instance variables

```
@"UIPDFPageView" _pageView;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{CGPoint="x"d"y"d} _startPoint;
B _moving;
@"UIPDFMarkupAnnotation" _currentAnnotation;
{?="location"q"length"q} _initialRange;
B _tracking;
@"CALayer" _drawingSurface;
@"<NSObject><UIPDFAnnotationControllerDelegate>" _delegate;
{CGSize="width"d"height"d} _cachedMarginNoteSize;
B makeUnderlineAnnotation;
B _allowEditing;
@"UIColor" _currentColor;
```

## Properties

```
@property (T@"UIPDFPageView",R,N,V_pageView) pageView;
@property (T@"UIPDFAnnotation",&,N,V_currentAnnotation) currentAnnotation;
@property (TB,N,V_allowEditing) allowEditing;
@property (T@"UIColor",N,V_currentColor) currentColor;
@property (TB,N,VmakeUnderlineAnnotation) makeUnderlineAnnotation;
@property (T@"CALayer",N,V_drawingSurface) drawingSurface;
@property (T@"<NSObject><UIPDFAnnotationControllerDelegate>",N,V_delegate) delegate;
@property (TB,R,N,V_tracking) tracking;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPDFAnnotationController newAnnotation:type:];
+[UIPDFAnnotationController newMaskImage:size:];
+[UIPDFAnnotationController pageHasAnnotations:];
```

## Instance methods

```
-[UIPDFAnnotationController setNeedsDisplay];
-[UIPDFAnnotationController tracking];
-[UIPDFAnnotationController init];
-[UIPDFAnnotationController dealloc];
-[UIPDFAnnotationController setView:];
-[UIPDFAnnotationController setDelegate:];
-[UIPDFAnnotationController gestureRecognizerShouldBegin:];
-[UIPDFAnnotationController delegate];
-[UIPDFAnnotationController lock];
-[UIPDFAnnotationController unlock];
-[UIPDFAnnotationController addAnnotation:];
-[UIPDFAnnotationController annotationBriefPressRecognized:];
-[UIPDFAnnotationController _addAnnotationViewFor:];
-[UIPDFAnnotationController _addLinkAnnotationViewFor:];
-[UIPDFAnnotationController _addRecognizers:];
-[UIPDFAnnotationController _initialRange:];
-[UIPDFAnnotationController _linkAnnotationViewAt:];
-[UIPDFAnnotationController addDrawingSurface:view:];
-[UIPDFAnnotationController addLinkAnnotationViews];
-[UIPDFAnnotationController allowEditing];
-[UIPDFAnnotationController annotatePageSelection];
-[UIPDFAnnotationController annotationAt:];
-[UIPDFAnnotationController annotationLongPressRecognized:];
-[UIPDFAnnotationController annotationSingleTapRecognized:];
-[UIPDFAnnotationController annotationTapRecognized:];
-[UIPDFAnnotationController convertPoint:toSurfaceLayer:];
-[UIPDFAnnotationController convertRect:toSurfaceLayer:];
-[UIPDFAnnotationController copyAttributesOf:to:];
-[UIPDFAnnotationController currentAnnotation];
-[UIPDFAnnotationController currentColor];
-[UIPDFAnnotationController didEndTrackingAtPoint:];
-[UIPDFAnnotationController doubleTapRecognized:];
-[UIPDFAnnotationController drawAnnotations:];
-[UIPDFAnnotationController drawingSurface];
-[UIPDFAnnotationController endTrackingAtPoint:];
-[UIPDFAnnotationController hostViewDidScroll];
-[UIPDFAnnotationController initWithPageView:];
-[UIPDFAnnotationController intersects:with:];
-[UIPDFAnnotationController isLinkAnnotationAt:];
-[UIPDFAnnotationController isSelection:equalTo:];
-[UIPDFAnnotationController layoutAnnotationViews:];
-[UIPDFAnnotationController linkAnnotationAt:];
-[UIPDFAnnotationController linkAnnotationShouldBegin:];
-[UIPDFAnnotationController linkPressRecognized:];
-[UIPDFAnnotationController madeInstantAnnotation];
-[UIPDFAnnotationController makeUnderlineAnnotation];
-[UIPDFAnnotationController marginNoteImage:];
-[UIPDFAnnotationController marginNoteImageSize];
-[UIPDFAnnotationController mergeSelectionOfAnnotation:];
-[UIPDFAnnotationController newHighlightMaskImageFor:];
-[UIPDFAnnotationController pageView];
-[UIPDFAnnotationController resetBeingPressedForRecognizer:withDelegate:withAnnotation:];
-[UIPDFAnnotationController setAllowEditing:];
-[UIPDFAnnotationController setCurrentAnnotation:];
-[UIPDFAnnotationController setCurrentColor:];
-[UIPDFAnnotationController setDrawingSurface:];
-[UIPDFAnnotationController setMakeUnderlineAnnotation:];
-[UIPDFAnnotationController setSurfacePosition:];
-[UIPDFAnnotationController startTracking:];
-[UIPDFAnnotationController trackMoved:];
-[UIPDFAnnotationController tracking:];
-[UIPDFAnnotationController underlineImageFor:];
-[UIPDFAnnotationController willDoSomethingWithTap:];
-[UIPDFAnnotationController willHandleTouchGestureAtPoint:];
-[UIPDFAnnotationController willTrackAtPoint:];
```
