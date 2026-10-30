# `CAMBurstIndicatorView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 4 properties, 18 instance methods, 1 class methods

## Instance variables

```
q _layoutStyle;
@"UIView" __backgroundView;
@"UILabel" __countLabel;
q __numberOfPhotos;
```

## Properties

```
@property (T@"UIView",R,N,V__backgroundView) _backgroundView;
@property (T@"UILabel",R,N,V__countLabel) _countLabel;
@property (Tq,R,N,V__numberOfPhotos) _numberOfPhotos;
@property (Tq,N,V_layoutStyle) layoutStyle;
```

## Class methods

```
+[CAMBurstIndicatorView _counterNumberFormatter];
```

## Instance methods

```
-[CAMBurstIndicatorView setLayoutStyle:];
-[CAMBurstIndicatorView layoutStyle];
-[CAMBurstIndicatorView intrinsicContentSize];
-[CAMBurstIndicatorView initWithLayoutStyle:];
-[CAMBurstIndicatorView reset];
-[CAMBurstIndicatorView layoutSubviews];
-[CAMBurstIndicatorView _backgroundView];
-[CAMBurstIndicatorView _performCaptureAnimation];
-[CAMBurstIndicatorView initWithCoder:];
-[CAMBurstIndicatorView _preferredContentSizeCategoryChanged];
-[CAMBurstIndicatorView initWithFrame:];
-[CAMBurstIndicatorView _updateAttributes];
-[CAMBurstIndicatorView _updateCountLabelWithNumberOfPhotos];
-[CAMBurstIndicatorView _numberOfPhotos];
-[CAMBurstIndicatorView _commonCAMAvalancheIndicatorViewInitializationWithLayoutStyle:];
-[CAMBurstIndicatorView _countLabel];
-[CAMBurstIndicatorView finishIncrementingWithCompletionHandler:];
-[CAMBurstIndicatorView incrementWithCaptureAnimation:];
```
