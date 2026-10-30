# `CAMLevelIndicatorView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAMLevelViewModelChangeObserver`
- 3 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"CAMLevelViewModel" _viewModel;
@"CAMLevelCrosshair" __goalCrosshair;
@"CAMLevelCrosshair" __userCrosshair;
```

## Properties

```
@property (T@"CAMLevelCrosshair",R,N,V__goalCrosshair) _goalCrosshair;
@property (T@"CAMLevelCrosshair",R,N,V__userCrosshair) _userCrosshair;
@property (T@"CAMLevelViewModel",R,N,V_viewModel) viewModel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMLevelIndicatorView viewModel];
-[CAMLevelIndicatorView initWithViewModel:];
-[CAMLevelIndicatorView observable:didPublishChange:withContext:];
-[CAMLevelIndicatorView layoutSubviews];
-[CAMLevelIndicatorView initWithCoder:];
-[CAMLevelIndicatorView initWithFrame:];
-[CAMLevelIndicatorView _commonCAMLevelIndicatorViewInitializationWithViewModel:];
-[CAMLevelIndicatorView _goalCrosshair];
-[CAMLevelIndicatorView _updateCrosshairAlphasWithAlpha:indicatorMode:];
-[CAMLevelIndicatorView _updateCrosshairHighlightWithOffset:];
-[CAMLevelIndicatorView _userCrosshair];
```
