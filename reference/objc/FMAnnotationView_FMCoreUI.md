# `FMAnnotationView`

- Image: [`/System/Library/PrivateFrameworks/FMCoreUI.framework/FMCoreUI`](../userland/System__Library__PrivateFrameworks__FMCoreUI.framework__FMCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MKAnnotationView`
- 12 instance variables, 13 properties, 44 instance methods, 6 class methods

## Instance variables

```
B _shouldPreventLargeAnnotationState;
B _isDelayed;
B _isShowingLargeSelectedAnnotation;
B _hasPhotoImage;
@"CAShapeLayer" _smallRingLayer;
@"CAShapeLayer" _largeRingLayer;
@"CALayer" _smallCircleLayer;
@"CALayer" _largeCircleLayer;
@"CALayer" _locationOuterLayer;
@"CALayer" _locationInnerLayer;
@"CALayer" _smallPersonImageLayer;
@"CALayer" _largePersonImageLayer;
```

## Properties

```
@property (T@"CAShapeLayer",&,N,V_smallRingLayer) smallRingLayer;
@property (T@"CAShapeLayer",&,N,V_largeRingLayer) largeRingLayer;
@property (T@"CALayer",&,N,V_smallCircleLayer) smallCircleLayer;
@property (T@"CALayer",&,N,V_largeCircleLayer) largeCircleLayer;
@property (T@"CALayer",&,N,V_locationOuterLayer) locationOuterLayer;
@property (T@"CALayer",&,N,V_locationInnerLayer) locationInnerLayer;
@property (T@"CALayer",&,N,V_smallPersonImageLayer) smallPersonImageLayer;
@property (T@"CALayer",&,N,V_largePersonImageLayer) largePersonImageLayer;
@property (TB,N,V_isShowingLargeSelectedAnnotation) isShowingLargeSelectedAnnotation;
@property (TB,N,V_hasPhotoImage) hasPhotoImage;
@property (T@"<FMAnnotation><MKAnnotation>",&,D,N) annotation;
@property (TB,N,V_shouldPreventLargeAnnotationState) shouldPreventLargeAnnotationState;
@property (TB,N,V_isDelayed) isDelayed;
```

## Class methods

```
+[FMAnnotationView setImagePadding:];
+[FMAnnotationView _followsTerrain];
+[FMAnnotationView preloadAssets];
+[FMAnnotationView setLargeAnnotationBorderVisible:];
+[FMAnnotationView setShouldMaskLayer:];
+[FMAnnotationView setThickAnnotationBorder:];
```

## Instance methods

```
-[FMAnnotationView isDelayed];
-[FMAnnotationView dealloc];
-[FMAnnotationView hitTest:withEvent:];
-[FMAnnotationView setTintColor:];
-[FMAnnotationView prepareForReuse];
-[FMAnnotationView initWithCoder:];
-[FMAnnotationView traitCollectionDidChange:];
-[FMAnnotationView setSelected:animated:];
-[FMAnnotationView setAnnotation:];
-[FMAnnotationView initWithAnnotation:reuseIdentifier:];
-[FMAnnotationView setIsDelayed:];
-[FMAnnotationView removeColorInvertFilterToLayer:];
-[FMAnnotationView _selectionWasUpdated:];
-[FMAnnotationView _setupSpringActions];
-[FMAnnotationView _transitionToNewSize:];
-[FMAnnotationView _updateAnnotationStyle];
-[FMAnnotationView addColorInvertFilterToLayer:];
-[FMAnnotationView animateDelayedAnimation];
-[FMAnnotationView hasPhotoImage];
-[FMAnnotationView initWithAnnotation:reuseIdentifier:tintColor:];
-[FMAnnotationView invertColorStatusDidChange:];
-[FMAnnotationView isShowingLargeSelectedAnnotation];
-[FMAnnotationView largeCircleLayer];
-[FMAnnotationView largePersonImageLayer];
-[FMAnnotationView largeRingLayer];
-[FMAnnotationView locationInnerLayer];
-[FMAnnotationView locationOuterLayer];
-[FMAnnotationView setHasPhotoImage:];
-[FMAnnotationView setIsShowingLargeSelectedAnnotation:];
-[FMAnnotationView setLargeCircleLayer:];
-[FMAnnotationView setLargePersonImageLayer:];
-[FMAnnotationView setLargeRingLayer:];
-[FMAnnotationView setLocationInnerLayer:];
-[FMAnnotationView setLocationOuterLayer:];
-[FMAnnotationView setSelected:animated:delay:];
-[FMAnnotationView setShouldPreventLargeAnnotationState:];
-[FMAnnotationView setSmallCircleLayer:];
-[FMAnnotationView setSmallPersonImageLayer:];
-[FMAnnotationView setSmallRingLayer:];
-[FMAnnotationView shouldPreventLargeAnnotationState];
-[FMAnnotationView smallCircleLayer];
-[FMAnnotationView smallPersonImageLayer];
-[FMAnnotationView smallRingLayer];
-[FMAnnotationView updateStyleForAnnotation:];
```
