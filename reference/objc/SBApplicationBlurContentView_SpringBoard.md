# `SBApplicationBlurContentView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 14 instance variables, 3 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSString" _bundleIdentifier;
Q _state;
@"NSMutableDictionary" _mapStateToCompletionBlocks;
{CGSize="width"d"height"d} _targetViewOriginalSize;
@"UIView" _targetViewToBlur;
@"UIView" _unblurredRealSnapshotView;
@"UIView" _unblurredCopySnapshotView;
@"UIView" _liveBlurView;
@"SBSceneViewAppIconView" _iconView;
@"UIView" _blurredSnapshotView;
@"SBApplicationBlurSnapshotGenerationContainerView" _snapshotGenerationContainerView;
@"UIView" _blurView;
d _iconViewScale;
d _blurDelay;
```

## Properties

```
@property (T@"SBSceneViewAppIconView",R,N,V_iconView) iconView;
@property (Td,N,V_iconViewScale) iconViewScale;
@property (Td,N,V_blurDelay) blurDelay;
```

## Instance methods

```
-[SBApplicationBlurContentView didMoveToWindow];
-[SBApplicationBlurContentView _setState:];
-[SBApplicationBlurContentView iconView];
-[SBApplicationBlurContentView dealloc];
-[SBApplicationBlurContentView layoutSubviews];
-[SBApplicationBlurContentView initWithCoder:];
-[SBApplicationBlurContentView initWithFrame:];
-[SBApplicationBlurContentView _addCompletionBlock:forState:];
-[SBApplicationBlurContentView _doAnimationToBlurredSnapshotWithFactory:completion:];
-[SBApplicationBlurContentView _doBlurGenerationWithCompletion:];
-[SBApplicationBlurContentView _fireCompletionBlocksForState:];
-[SBApplicationBlurContentView animateToBlurredSnapshotWithFactory:completion:];
-[SBApplicationBlurContentView blurDelay];
-[SBApplicationBlurContentView generateAndAnimateToBlurredSnapshotWithAnimationFactory:completion:];
-[SBApplicationBlurContentView generateBlurredSnapshotWithCompletion:];
-[SBApplicationBlurContentView iconViewScale];
-[SBApplicationBlurContentView initWithFrame:bundleIdentifier:icon:targetViewToBlur:initialIconScale:];
-[SBApplicationBlurContentView initWithFrame:bundleIdentifier:targetViewToBlur:];
-[SBApplicationBlurContentView initWithFrame:bundleIdentifier:targetViewToBlur:initialIconScale:];
-[SBApplicationBlurContentView setBlurDelay:];
-[SBApplicationBlurContentView setIconViewScale:];
```
