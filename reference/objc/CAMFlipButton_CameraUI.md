# `CAMFlipButton`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- Protocols: `CAMViewOrientable`
- 3 instance variables, 5 properties, 14 instance methods, 2 class methods

## Instance variables

```
{UIEdgeInsets=dddd} tappableEdgeInsets;
q layoutStyle;
_orientation;
```

## Properties

```
@property (T{CGSize=dd},N,R) intrinsicContentSize;
@property (TB,N) highlighted;
@property (T{UIEdgeInsets=dddd},N,VtappableEdgeInsets) tappableEdgeInsets;
@property (Tq,N,VlayoutStyle) layoutStyle;
@property (Tq,N) orientation;
```

## Class methods

```
+[CAMFlipButton flipButtonOverContent];
+[CAMFlipButton flipButtonWithLayoutStyle:];
```

## Instance methods

```
-[CAMFlipButton setLayoutStyle:];
-[CAMFlipButton setOrientation:animated:];
-[CAMFlipButton setOrientation:];
-[CAMFlipButton layoutStyle];
-[CAMFlipButton intrinsicContentSize];
-[CAMFlipButton isHighlighted];
-[CAMFlipButton orientation];
-[CAMFlipButton layoutSubviews];
-[CAMFlipButton tintColorDidChange];
-[CAMFlipButton setHighlighted:];
-[CAMFlipButton setTappableEdgeInsets:];
-[CAMFlipButton initWithCoder:];
-[CAMFlipButton tappableEdgeInsets];
-[CAMFlipButton initWithFrame:];
```
