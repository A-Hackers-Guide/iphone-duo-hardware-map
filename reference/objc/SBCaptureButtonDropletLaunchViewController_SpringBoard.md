# `SBCaptureButtonDropletLaunchViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 14 instance variables, 0 properties, 22 instance methods, 0 class methods

## Instance variables

```
q _associatedButton;
@"SBWindowScene" _windowScene;
@"SBCaptureButtonSettings" _settings;
@"DRPDropletContextView" _dropletContext;
@"DRPDropletContainerView" _appDropletContainer;
@"DRPDropletAnimationCoordinator" _animator;
@"UIView" _contentView;
@"NSMutableDictionary" _toStageFloatAnimatableProperty;
@"NSMutableDictionary" _toStageCompletionBlock;
Q _stage;
B _animateNextStageTransition;
Q _expansionComponents;
Q _dropetIntelligentKeylineStage;
@"NSMutableArray" _pendingZoomUpCompletionBlocks;
```

## Instance methods

```
-[SBCaptureButtonDropletLaunchViewController supportedInterfaceOrientations];
-[SBCaptureButtonDropletLaunchViewController _buttonGeometryInfo];
-[SBCaptureButtonDropletLaunchViewController viewDidLoad];
-[SBCaptureButtonDropletLaunchViewController _canShowWhileLocked];
-[SBCaptureButtonDropletLaunchViewController loadView];
-[SBCaptureButtonDropletLaunchViewController viewWillLayoutSubviews];
-[SBCaptureButtonDropletLaunchViewController _applyViewConfigurationForCurrentStage];
-[SBCaptureButtonDropletLaunchViewController _configurationForStage:];
-[SBCaptureButtonDropletLaunchViewController _defaultConfigurationForStage:];
-[SBCaptureButtonDropletLaunchViewController _setStage:animated:milestones:];
-[SBCaptureButtonDropletLaunchViewController _zoomUpAnimationCompleted:];
-[SBCaptureButtonDropletLaunchViewController animateDropletFromButtonWithMilestones:];
-[SBCaptureButtonDropletLaunchViewController animatingDroplet];
-[SBCaptureButtonDropletLaunchViewController animatingDropletContext];
-[SBCaptureButtonDropletLaunchViewController appendDropletZoomUpCompletionBlock:];
-[SBCaptureButtonDropletLaunchViewController expandDropletKeylineToIntelligentKeylineStage:];
-[SBCaptureButtonDropletLaunchViewController expandHintingDropletByAddingComponents:];
-[SBCaptureButtonDropletLaunchViewController initWithButtonOrigin:windowScene:];
-[SBCaptureButtonDropletLaunchViewController lendAnimatingDropletViewToExternalOwner];
-[SBCaptureButtonDropletLaunchViewController preludeAnimationRectPresentationValue];
-[SBCaptureButtonDropletLaunchViewController preludeAnimationVelocity];
-[SBCaptureButtonDropletLaunchViewController resetToOffscreenAnimated:milestones:];
```
