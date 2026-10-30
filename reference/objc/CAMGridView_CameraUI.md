# `CAMGridView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAMLevelViewModelChangeObserver`, `CEKAdditiveAnimatorDelegate`
- 2 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"CAMLevelViewModel" _levelViewModel;
@"CEKAdditiveAnimator" __animator;
```

## Properties

```
@property (T@"CEKAdditiveAnimator",&,N,V__animator) _animator;
@property (T@"CAMLevelViewModel",&,N,V_levelViewModel) levelViewModel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMGridView observable:didPublishChange:withContext:];
-[CAMGridView drawRect:];
-[CAMGridView _animator];
-[CAMGridView hitTest:withEvent:];
-[CAMGridView animator:didUpdateValuesForKeys:];
-[CAMGridView initWithFrame:];
-[CAMGridView _drawLinesWithInset:];
-[CAMGridView _getDeltasBetweenLines:widthDelta:];
-[CAMGridView _setAnimatorGridOffsetForViewModel:animated:];
-[CAMGridView levelViewModel];
-[CAMGridView setLevelViewModel:];
-[CAMGridView set_animator:];
```
