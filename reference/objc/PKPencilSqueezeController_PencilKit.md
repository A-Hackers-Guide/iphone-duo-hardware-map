# `PKPencilSqueezeController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIPencilInteractionDelegatePrivate`, `UIPopoverPresentationControllerDelegate`, `UIGestureRecognizerDelegate`, `PKPencilSqueezeAnalyticsControllerDelegate`, `PKImageWandOnboardingControllerDelegate`
- 35 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"UIView" _containerView;
@"PKSqueezePaletteView" _paletteView;
{CGSize="width"d"height"d} _paletteViewSize;
@"NSLayoutConstraint" _paletteViewCenterXConstraint;
@"NSLayoutConstraint" _paletteViewCenterYConstraint;
@"UIHoverGestureRecognizer" _hoverGestureRecognizer;
@"UILayoutGuide" _contentLayoutGuide;
@"NSLayoutConstraint" _contentLayoutGuideWidthConstraint;
@"NSLayoutConstraint" _contentLayoutGuideHeightConstraint;
@"PKPencilSqueezeControllerPaletteViewDelegateProxy" _paletteViewDelegateProxy;
@"PKHoverSettings" _hoverSettings;
@"PKUIPencilInteractionObserver" _pencilInteractionObserver;
@"PKAutoRefineSettingsObserver" _autoRefineSettingsObserver;
@"PKPencilSqueezeContainerViewOverlay" _containerViewOverlay;
@"PKPencilInteraction" _pencilInteraction;
B _paletteViewVisibleBeforeSqueezeBegan;
B _squeezeBeganOnPalette;
B _didCancelShowToolPicker;
B _isHidingPaletteAfterDelay;
d _hidePaletteDelay;
@"PKSqueezePaletteViewPresentationHandle" _paletteViewPresentationHandle;
B _hovering;
{CGPoint="x"d"y"d} _hoverLocation;
d _azimuth;
@"PKPencilSqueezeUserDefaults" _userDefaults;
d _lastHoverLocationSavedTimestamp;
@"PKImageWandOnboardingController" _imageWandOnboardingController;
@"NSUndoManager" _cachedUndoManager;
B _isUndoRedoInvoked;
B _paletteViewVisible;
B __isUndoRedoPalette;
@"<PKPencilSqueezeControllerDelegate>" _delegate;
@"UIViewController" _rootViewController;
@"PKTextEffectsWindowObserver" _textEffectsWindowObserver;
@"PKPencilSqueezeAnalyticsController" __analyticsController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPencilSqueezeController _firstResponderDidChange:];
-[PKPencilSqueezeController adaptivePresentationStyleForPresentationController:traitCollection:];
-[PKPencilSqueezeController adaptivePresentationStyleForPresentationController:];
-[PKPencilSqueezeController _handleKeyboardWillHideNotification:];
-[PKPencilSqueezeController pencilInteraction:didReceiveSqueeze:];
-[PKPencilSqueezeController pencilInteraction:didReceiveTap:];
-[PKPencilSqueezeController _changeWasDone:];
-[PKPencilSqueezeController _changeWasRedone:];
-[PKPencilSqueezeController _changeWasUndone:];
-[PKPencilSqueezeController _handleSceneDidEnterBackgroundNotification:];
-[PKPencilSqueezeController _handleSceneWillEnterForegroundNotification:];
-[PKPencilSqueezeController _handleKeyboardWillShowNotification:];
-[PKPencilSqueezeController _handleHandwritingEducationPaneSettingsDidChange:];
-[PKPencilSqueezeController imageWandOnboardingControllerDidHideView:];
-[PKPencilSqueezeController pencilSqueezeAnalyticsControllerHoverSettings:];
-[PKPencilSqueezeController pencilSqueezeAnalyticsControllerHoverZOffset:];
-[PKPencilSqueezeController pencilSqueezeAnalyticsControllerIsHovering:];
```
