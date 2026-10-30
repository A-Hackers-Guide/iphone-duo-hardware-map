# `CAMHorizonLevelView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAMLevelViewModelChangeObserver`
- 6 instance variables, 10 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"CAMLevelViewModel" _viewModel;
@"<CAMHorizonLevelViewDelegate>" _delegate;
@"UIImageView" __horizonLineView;
@"UIImageView" __referenceLineLeft;
@"UIImageView" __referenceLineRight;
@"CAMFeedbackController" __feedbackController;
```

## Properties

```
@property (T@"UIImageView",&,N,V__horizonLineView) _horizonLineView;
@property (T@"UIImageView",&,N,V__referenceLineLeft) _referenceLineLeft;
@property (T@"UIImageView",&,N,V__referenceLineRight) _referenceLineRight;
@property (T@"CAMFeedbackController",R,N,V__feedbackController) _feedbackController;
@property (T@"CAMLevelViewModel",R,N,V_viewModel) viewModel;
@property (T@"<CAMHorizonLevelViewDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMHorizonLevelView _feedbackController];
-[CAMHorizonLevelView viewModel];
-[CAMHorizonLevelView initWithViewModel:];
-[CAMHorizonLevelView observable:didPublishChange:withContext:];
-[CAMHorizonLevelView layoutSubviews];
-[CAMHorizonLevelView setDelegate:];
-[CAMHorizonLevelView delegate];
-[CAMHorizonLevelView _createStrechableLineImage:lineHeight:shadowWidth:shadowHorizontalEdges:];
-[CAMHorizonLevelView _drawHorizonLineInContext:withBounds:color:];
-[CAMHorizonLevelView _horizonLineView];
-[CAMHorizonLevelView _layoutLineViewsWithMode:rotationAngle:];
-[CAMHorizonLevelView _referenceLineLeft];
-[CAMHorizonLevelView _referenceLineRight];
-[CAMHorizonLevelView _shadowWidth];
-[CAMHorizonLevelView _updateSubViewsAlphaWithAlpha:indicatorMode:rotationAngle:];
-[CAMHorizonLevelView set_horizonLineView:];
-[CAMHorizonLevelView set_referenceLineLeft:];
-[CAMHorizonLevelView set_referenceLineRight:];
```
