# `SBHardwareButtonHintDropletViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 7 instance variables, 2 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"DRPDropletContextView" _dropletContextView;
@"DRPDropletAnimationCoordinator" _animator;
@"NSTimer" _idleTimer;
@"CADisplayLink" _displayLink;
@"NSMutableDictionary" _buttonStates;
Q _keylineStyle;
@"<SBHardwareButtonHintDropletViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBHardwareButtonHintDropletViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,N,V_keylineStyle) keylineStyle;
```

## Instance methods

```
-[SBHardwareButtonHintDropletViewController _startIdleTimer];
-[SBHardwareButtonHintDropletViewController _existingOrNewDropletStateForButton:];
-[SBHardwareButtonHintDropletViewController init];
-[SBHardwareButtonHintDropletViewController supportedInterfaceOrientations];
-[SBHardwareButtonHintDropletViewController _dropletLayoutCallbackAssertionDidInvalidate:forCallback:forButton:];
-[SBHardwareButtonHintDropletViewController dealloc];
-[SBHardwareButtonHintDropletViewController _updateDisplayLink];
-[SBHardwareButtonHintDropletViewController activateHintDropletForButton:];
-[SBHardwareButtonHintDropletViewController _buttonGeometryInfo];
-[SBHardwareButtonHintDropletViewController viewDidLoad];
-[SBHardwareButtonHintDropletViewController _applyButtonState:animated:checkForIdle:];
-[SBHardwareButtonHintDropletViewController _applyButtonState:animated:];
-[SBHardwareButtonHintDropletViewController _displayLinkCallback:];
-[SBHardwareButtonHintDropletViewController setKeylineStyle:];
-[SBHardwareButtonHintDropletViewController _canShowWhileLocked];
-[SBHardwareButtonHintDropletViewController _activateButtonAssertionDidInvalidate:forButton:];
-[SBHardwareButtonHintDropletViewController setDelegate:];
-[SBHardwareButtonHintDropletViewController _configurationForButton:stage:];
-[SBHardwareButtonHintDropletViewController loadView];
-[SBHardwareButtonHintDropletViewController delegate];
-[SBHardwareButtonHintDropletViewController _applyStateForExistingButton:animated:checkForIdle:];
-[SBHardwareButtonHintDropletViewController keylineStyle];
-[SBHardwareButtonHintDropletViewController updateHintContentVisibility:forButton:animationSettings:];
-[SBHardwareButtonHintDropletViewController setDropletLayoutCallback:forButton:];
-[SBHardwareButtonHintDropletViewController _updateSnapshotVisibility];
-[SBHardwareButtonHintDropletViewController _associateHintViewAssertionDidInvalidate:forView:forButton:];
-[SBHardwareButtonHintDropletViewController associateHintView:withButton:];
```
