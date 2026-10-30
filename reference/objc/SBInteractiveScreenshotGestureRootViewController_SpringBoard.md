# `SBInteractiveScreenshotGestureRootViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `BSInvalidatable`
- 42 instance variables, 8 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"SBWallpaperEffectView" _wallpaperEffectView;
@"_SBInteractiveScreenshotGestureBackdropView" _contentCapturingView;
@"SSChromePlaceholderViewController" _chromePlaceholderViewController;
@"BSUIOrientationTransformWrapperView" _chromePlaceholderOrientationWrapperView;
@"UIStatusBar" _chromePlaceholderStatusBar;
@"_SBInteractiveScreenshotGestureBackdropView" _contentBackdropView;
@"SBInteractiveScreenshotGestureCropsView" _cropsView;
@"SSFlashView" _flashView;
{CGPoint="x"d"y"d} _gesturePortraitAnchorPoint;
B _hasCrossedCommitThreshold;
B _hasPreparedInitialLayout;
@"UIVisualEffectView" _materialView;
@"UIViewFloatAnimatableProperty" _cancellationCommitProgressAnimatableProperty;
@"NSMutableArray" _cropLinesAlphaMultiPartAnimations;
@"UIViewFloatAnimatableProperty" _cropsTrackingDiscreteAnimationProgressAnimatableProperty;
@"UIViewFloatAnimatableProperty" _cropsProgressPresentationValueAnimatableProperty;
@"UIViewFloatAnimatableProperty" _cropsProgressSeparatedValuesAnimatableProperty;
@"UIViewFloatAnimatableProperty" _transformProgressAnimatableProperty;
@"UIViewFloatAnimatableProperty" _translationXAnimatableProperty;
@"UIViewFloatAnimatableProperty" _translationYAnimatableProperty;
@"_SBInteractiveScreenshotGestureReplicatorView" _replicatorView;
@"UIImageView" _screenshotImageView;
@"UIView" _screenshotContainerView;
@"SBInteractiveScreenshotSettings" _settings;
@"FBScene" _sourceScene;
@"UIView<UIScenePresentation>" _sourceScenePresentationView;
@"<UIScenePresenter>" _sourceScenePresenter;
@"UIView" _topContentContainerView;
@"SBFFluidBehaviorSettings" _trackingCropsAnimationSettings;
@"NSMutableArray" _gestureCommitProgressUpdates;
@"NSMutableArray" _gestureCommitProgressUpdateTimestamps;
@"NSObject<OS_dispatch_queue>" _accessQueue;
d _queue_cropsCornerContentPadding;
d _queue_cropsCornerLineWidth;
d _queue_contentCornerRadius;
d _queue_displayScale;
q _queue_gestureStyle;
q _queue_gestureTouchInterfaceOrientation;
B _queue_hasCommittedScreenshot;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _queue_portraitBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _queue_screenshotContentFrame;
@"<SBInteractiveScreenshotGestureRootViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBInteractiveScreenshotGestureRootViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TI,R,N) flashViewLayerContextID;
@property (TQ,R,N) flashViewLayerRenderID;
@property (Tq,N) gestureStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBInteractiveScreenshotGestureRootViewController supportedInterfaceOrientations];
-[SBInteractiveScreenshotGestureRootViewController viewDidLoad];
-[SBInteractiveScreenshotGestureRootViewController viewDidLayoutSubviews];
-[SBInteractiveScreenshotGestureRootViewController initWithWindowScene:];
-[SBInteractiveScreenshotGestureRootViewController invalidate];
-[SBInteractiveScreenshotGestureRootViewController _canShowWhileLocked];
-[SBInteractiveScreenshotGestureRootViewController setDelegate:];
-[SBInteractiveScreenshotGestureRootViewController delegate];
-[SBInteractiveScreenshotGestureRootViewController _edgeInsetsForChildViewController:insetsAreAbsolute:];
-[SBInteractiveScreenshotGestureRootViewController handlePanGestureRecognizerAction:];
-[SBInteractiveScreenshotGestureRootViewController _addGestureUpdateWithCommitProgress:timestamp:];
-[SBInteractiveScreenshotGestureRootViewController _anchoredTransformForAnchorPoint:bounds:center:transform:];
-[SBInteractiveScreenshotGestureRootViewController _cancellationCommitProgressAnimatablePropertyPresentationValueDidChange];
-[SBInteractiveScreenshotGestureRootViewController _contentScaleForCommitProgress:contentInsets:additionalContentTranslation:];
-[SBInteractiveScreenshotGestureRootViewController _contentTransformForCommitProgress:contentInsets:additionalContentTranslation:];
-[SBInteractiveScreenshotGestureRootViewController _createFlashViewWithFrame:];
-[SBInteractiveScreenshotGestureRootViewController _createScreenshotImageViewWithFrame:];
-[SBInteractiveScreenshotGestureRootViewController _currentCommitProgressVelocity];
-[SBInteractiveScreenshotGestureRootViewController _gestureCommitProgressUpdateVelocityOverTimeInterval:];
-[SBInteractiveScreenshotGestureRootViewController _getContentTranslation:scale:forCommitProgress:contentInsets:additionalContentTranslation:];
-[SBInteractiveScreenshotGestureRootViewController _getDistanceTraveled:fullDistance:commitProgress:forTranslationFromCorner:bounds:];
-[SBInteractiveScreenshotGestureRootViewController _injectCommitProgressVelocity:];
-[SBInteractiveScreenshotGestureRootViewController _inverseContentTransformForCommitProgress:contentInsets:additionalContentTranslation:];
-[SBInteractiveScreenshotGestureRootViewController _isGestureStyleDisabled:];
-[SBInteractiveScreenshotGestureRootViewController _isGestureStyleReducedMotion:];
-[SBInteractiveScreenshotGestureRootViewController _prepareViewHierarchyForCommittedScreenshot:gestureStyle:];
-[SBInteractiveScreenshotGestureRootViewController _updateContentTransformUsingPresentationValues:];
-[SBInteractiveScreenshotGestureRootViewController _updateCropLinesMultiPartAnimationForCropsProgress];
-[SBInteractiveScreenshotGestureRootViewController _updateWithUpdateMode:commitProgress:additionalContentTranslation:completion:];
-[SBInteractiveScreenshotGestureRootViewController _updateWithUpdateMode:contentAnimationSettings:commitProgress:additionalContentTranslation:completion:];
-[SBInteractiveScreenshotGestureRootViewController cancelInteractionWithStyle:settlingCompletionHandler:];
-[SBInteractiveScreenshotGestureRootViewController captureScreenshotWithInterfaceOrientation:completion:];
-[SBInteractiveScreenshotGestureRootViewController commitInteractionWithScreenshotImage:screenshotInterfaceOrientation:settlingCompletionHandler:flashCompletionHandler:];
-[SBInteractiveScreenshotGestureRootViewController flashViewLayerContextID];
-[SBInteractiveScreenshotGestureRootViewController flashViewLayerRenderID];
-[SBInteractiveScreenshotGestureRootViewController gestureStyle];
-[SBInteractiveScreenshotGestureRootViewController removePlaceholderChrome];
-[SBInteractiveScreenshotGestureRootViewController setGestureStyle:];
```
