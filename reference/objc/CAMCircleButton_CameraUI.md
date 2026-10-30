# `CAMCircleButton`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- 4 instance variables, 6 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"CAMSlashContainer" __slashView;
@"UIImageView" __imageView;
@"UIImageView" __backgroundView;
@"UIView" __materialEffectBackgroundView;
```

## Properties

```
@property (T@"CAMSlashContainer",&,N,S_setSlashView:,V__slashView) _slashView;
@property (T@"UIImageView",R,N,V__imageView) _imageView;
@property (T@"UIImageView",R,N,V__backgroundView) _backgroundView;
@property (T@"UIView",&,N,S_setMaterialEffectBackgroundView:,V__materialEffectBackgroundView) _materialEffectBackgroundView;
@property (Td,R,N) activeTintAlphaForCurrentState;
@property (Tq,N) orientation;
```

## Instance methods

```
-[CAMCircleButton setOrientation:animated:];
-[CAMCircleButton setOrientation:];
-[CAMCircleButton _imageView];
-[CAMCircleButton updateImage];
-[CAMCircleButton _setSlashView:];
-[CAMCircleButton orientation];
-[CAMCircleButton layoutSubviews];
-[CAMCircleButton _backgroundView];
-[CAMCircleButton _preferredContentSizeCategoryDidChange];
-[CAMCircleButton _slashView];
-[CAMCircleButton setHighlighted:];
-[CAMCircleButton _updateBackgroundImage];
-[CAMCircleButton initWithFrame:];
-[CAMCircleButton _createCircleImageForContentSize:];
-[CAMCircleButton _materialEffectBackgroundView];
-[CAMCircleButton _setMaterialEffectBackgroundView:];
-[CAMCircleButton activeTintAlphaForCurrentState];
-[CAMCircleButton imageNameForAXHUD];
-[CAMCircleButton imageNameForCurrentState];
-[CAMCircleButton shouldShowSlashForCurrentState];
-[CAMCircleButton shouldUseActiveTintForCurrentState];
-[CAMCircleButton updateSlashAnimated:];
-[CAMCircleButton updateTintColors];
-[CAMCircleButton useThinMaterialBackground];
```
