# `CEKCinematicSubjectIndicatorView`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAAnimationDelegate`
- 12 instance variables, 16 properties, 25 instance methods, 2 class methods

## Instance variables

```
B __crosshairsVisible;
i __activeAnimationToActiveRoundedRectCount;
q _shape;
@"UIImageView" __topLeftCornerView;
@"UIImageView" __topRightCornerView;
@"UIImageView" __bottomLeftCornerView;
@"UIImageView" __bottomRightCornerView;
@"UIImageView" __topCrosshairView;
@"UIImageView" __leftCrosshairView;
@"UIImageView" __bottomCrosshairView;
@"UIImageView" __rightCrosshairView;
@"UIView" __containerView;
```

## Properties

```
@property (T@"UIImageView",R,N,V__topLeftCornerView) _topLeftCornerView;
@property (T@"UIImageView",R,N,V__topRightCornerView) _topRightCornerView;
@property (T@"UIImageView",R,N,V__bottomLeftCornerView) _bottomLeftCornerView;
@property (T@"UIImageView",R,N,V__bottomRightCornerView) _bottomRightCornerView;
@property (T@"UIImageView",R,N,V__topCrosshairView) _topCrosshairView;
@property (T@"UIImageView",R,N,V__leftCrosshairView) _leftCrosshairView;
@property (T@"UIImageView",R,N,V__bottomCrosshairView) _bottomCrosshairView;
@property (T@"UIImageView",R,N,V__rightCrosshairView) _rightCrosshairView;
@property (T@"UIView",R,N,V__containerView) _containerView;
@property (TB,N,V__crosshairsVisible) _crosshairsVisible;
@property (Ti,N,V__activeAnimationToActiveRoundedRectCount) _activeAnimationToActiveRoundedRectCount;
@property (Tq,N,V_shape) shape;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CEKCinematicSubjectIndicatorView minimumSuggestedBounds];
+[CEKCinematicSubjectIndicatorView _cornerImageWithResizableCapInsetsNamed:];
```

## Instance methods

```
-[CEKCinematicSubjectIndicatorView _updateVisibility];
-[CEKCinematicSubjectIndicatorView setShape:];
-[CEKCinematicSubjectIndicatorView shape];
-[CEKCinematicSubjectIndicatorView _bottomRightCornerView];
-[CEKCinematicSubjectIndicatorView layoutSubviews];
-[CEKCinematicSubjectIndicatorView _bottomLeftCornerView];
-[CEKCinematicSubjectIndicatorView _containerView];
-[CEKCinematicSubjectIndicatorView _topRightCornerView];
-[CEKCinematicSubjectIndicatorView _topLeftCornerView];
-[CEKCinematicSubjectIndicatorView initWithFrame:];
-[CEKCinematicSubjectIndicatorView setShape:animated:];
-[CEKCinematicSubjectIndicatorView setShape:shouldUseCrosshairForAnimation:animated:];
-[CEKCinematicSubjectIndicatorView _activeAnimationToActiveRoundedRectCount];
-[CEKCinematicSubjectIndicatorView _bottomCrosshairView];
-[CEKCinematicSubjectIndicatorView _crosshairsVisible];
-[CEKCinematicSubjectIndicatorView _leftCrosshairView];
-[CEKCinematicSubjectIndicatorView _performAnimationToActiveCorners];
-[CEKCinematicSubjectIndicatorView _performAnimationToActiveRoundedRect];
-[CEKCinematicSubjectIndicatorView _rightCrosshairView];
-[CEKCinematicSubjectIndicatorView _topCrosshairView];
-[CEKCinematicSubjectIndicatorView _updateCornerImageViewsForThickness:duration:delay:];
-[CEKCinematicSubjectIndicatorView _updateCornerViews];
-[CEKCinematicSubjectIndicatorView _updateCrossHairViewsWithHeight:];
-[CEKCinematicSubjectIndicatorView set_activeAnimationToActiveRoundedRectCount:];
-[CEKCinematicSubjectIndicatorView set_crosshairsVisible:];
```
