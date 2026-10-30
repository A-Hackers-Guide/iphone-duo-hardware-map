# `CEKSubjectIndicatorView`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 9 properties, 21 instance methods, 2 class methods

## Instance variables

```
B _inactive;
q _shape;
@"UIImageView" __topLeftCornerView;
@"UIImageView" __topRightCornerView;
@"UIImageView" __bottomLeftCornerView;
@"UIImageView" __bottomRightCornerView;
@"UIImageView" __fullSizeIndicatorView;
@"UIView" __containerView;
```

## Properties

```
@property (T@"UIImageView",R,N,V__topLeftCornerView) _topLeftCornerView;
@property (T@"UIImageView",R,N,V__topRightCornerView) _topRightCornerView;
@property (T@"UIImageView",R,N,V__bottomLeftCornerView) _bottomLeftCornerView;
@property (T@"UIImageView",R,N,V__bottomRightCornerView) _bottomRightCornerView;
@property (T@"UIImageView",R,N,V__fullSizeIndicatorView) _fullSizeIndicatorView;
@property (T@"UIView",R,N,V__containerView) _containerView;
@property (TB,N,GisInactive,V_inactive) inactive;
@property (Tq,N,V_shape) shape;
@property (TB,N,GisPulsing) pulsing;
```

## Class methods

```
+[CEKSubjectIndicatorView fixedSizeWithScale:windowSize:];
+[CEKSubjectIndicatorView _fixedSubjectIndicatorSizeForReferenceBounds:withScale:];
```

## Instance methods

```
-[CEKSubjectIndicatorView setShape:];
-[CEKSubjectIndicatorView setInactive:];
-[CEKSubjectIndicatorView intrinsicContentSize];
-[CEKSubjectIndicatorView shape];
-[CEKSubjectIndicatorView _bottomRightCornerView];
-[CEKSubjectIndicatorView layoutSubviews];
-[CEKSubjectIndicatorView _bottomLeftCornerView];
-[CEKSubjectIndicatorView sizeThatFits:];
-[CEKSubjectIndicatorView isPulsing];
-[CEKSubjectIndicatorView isInactive];
-[CEKSubjectIndicatorView _containerView];
-[CEKSubjectIndicatorView _topRightCornerView];
-[CEKSubjectIndicatorView setPulsing:];
-[CEKSubjectIndicatorView _topLeftCornerView];
-[CEKSubjectIndicatorView initWithFrame:];
-[CEKSubjectIndicatorView startScalingWithExpansionWidth:duration:repeatCount:];
-[CEKSubjectIndicatorView setHidden:animated:];
-[CEKSubjectIndicatorView setShape:animated:];
-[CEKSubjectIndicatorView startScalingWithExpansionWidth:duration:repeatCount:timingFunction:];
-[CEKSubjectIndicatorView stopScalingWithDuration:];
-[CEKSubjectIndicatorView _fullSizeIndicatorView];
```
