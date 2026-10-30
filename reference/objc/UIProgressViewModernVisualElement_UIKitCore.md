# `UIProgressViewModernVisualElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIProgressViewVisualElement`
- 10 instance variables, 1 properties, 26 instance methods, 4 class methods

## Instance variables

```
@"UIView" _contentView;
@"UIImageView" _trackView;
@"UIImageView" _progressView;
B _isAnimating;
@"NSArray" _trackColors;
@"NSArray" _progressColors;
@"UIVisualEffectView" _effectView;
@"UIView" _shadowView;
d _currentCornerRadius;
@"UIProgressView" _progressControlView;
```

## Properties

```
@property (T@"UIProgressView",W,N,V_progressControlView) progressControlView;
```

## Class methods

```
+[UIProgressViewModernVisualElement _tintedImageWithTraitCollection:forHeight:andColors:];
+[UIProgressViewModernVisualElement _tintedImageWithTraitCollection:forHeight:andColors:roundingRectCorners:];
+[UIProgressViewModernVisualElement intrinsicSizeWithinSize:control:];
+[UIProgressViewModernVisualElement usesLegacySubviewStructure];
```

## Instance methods

```
-[UIProgressViewModernVisualElement setTrackImage:];
-[UIProgressViewModernVisualElement removeLegacySubviewsForArchive:];
-[UIProgressViewModernVisualElement _dynamicUserInterfaceTraitDidChange];
-[UIProgressViewModernVisualElement _intrinsicSizeWithinSize:];
-[UIProgressViewModernVisualElement alignmentRectInsets];
-[UIProgressViewModernVisualElement setProgressTintColor:];
-[UIProgressViewModernVisualElement _updateCornerRadiusWithSize:];
-[UIProgressViewModernVisualElement setProgressImage:];
-[UIProgressViewModernVisualElement _setupShadow];
-[UIProgressViewModernVisualElement layoutSubviews];
-[UIProgressViewModernVisualElement setProgress:animated:duration:delay:options:];
-[UIProgressViewModernVisualElement _defaultTrackColorForCurrentStyle];
-[UIProgressViewModernVisualElement _updateImages];
-[UIProgressViewModernVisualElement _shadowOpacityForUserInterfaceStyle:];
-[UIProgressViewModernVisualElement tintColorDidChange];
-[UIProgressViewModernVisualElement setProgressViewStyle:];
-[UIProgressViewModernVisualElement setBarStyle:];
-[UIProgressViewModernVisualElement progressControlView];
-[UIProgressViewModernVisualElement _effectiveContentView];
-[UIProgressViewModernVisualElement _reducedTransparencyDidChange:];
-[UIProgressViewModernVisualElement setControlSize:];
-[UIProgressViewModernVisualElement _layoutShadow];
-[UIProgressViewModernVisualElement setProgressControlView:];
-[UIProgressViewModernVisualElement _roundedCornersForTrackForCurrentStyle];
-[UIProgressViewModernVisualElement _roundedCornersForProgressForCurrentStyle];
-[UIProgressViewModernVisualElement setTrackTintColor:];
```
