# `SBHomeScreenBackdropView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHomeScreenBackdropViewBase`
- 7 instance variables, 1 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"MTMaterialView" _materialView;
@"UIImage" _blurredContentSnapshotImage;
@"UIImageView" _blurredContentSnapshotImageView;
Q _materialViewAnimationCount;
B _waitingForBackdropViewToRender;
@"UIViewFloatAnimatableProperty" _backdropFloatAnimatableProperty;
@"NSString" _materialRecipeName;
```

## Properties

```
@property (T@"NSString",C,N,V_materialRecipeName) materialRecipeName;
```

## Instance methods

```
-[SBHomeScreenBackdropView endRequiringBackdropViewForReason:];
-[SBHomeScreenBackdropView beginRequiringLiveBackdropViewForReason:];
-[SBHomeScreenBackdropView endRequiringLiveBackdropViewForReason:];
-[SBHomeScreenBackdropView beginRequiringBackdropViewForReason:];
-[SBHomeScreenBackdropView cancelInProcessAnimations];
-[SBHomeScreenBackdropView _updateBackdropViewIfNeeded];
-[SBHomeScreenBackdropView isOpaque];
-[SBHomeScreenBackdropView _invalidateBackdropSnapshot];
-[SBHomeScreenBackdropView _updateBackdropViewIfNeededInvalidatingSnapshot:];
-[SBHomeScreenBackdropView homeScreenBlurredContentSnapshotImage];
-[SBHomeScreenBackdropView setBlurProgress:behaviorMode:completion:];
-[SBHomeScreenBackdropView blurProgress];
-[SBHomeScreenBackdropView setMaterialRecipeName:];
-[SBHomeScreenBackdropView initWithFrame:materialRecipe:scaleAdjustment:];
-[SBHomeScreenBackdropView _setupBackdropViewWithRecipe:scaleAdjustment:];
-[SBHomeScreenBackdropView _resetHomeScreenBlurredContentSnapshotImage];
-[SBHomeScreenBackdropView _configureBackdropAnimatableProperty];
-[SBHomeScreenBackdropView materialRecipeName];
-[SBHomeScreenBackdropView initWithFrame:];
```
