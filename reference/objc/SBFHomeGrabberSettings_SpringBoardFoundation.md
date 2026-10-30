# `SBFHomeGrabberSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 39 instance variables, 39 properties, 81 instance methods, 1 class methods

## Instance variables

```
B _enabled;
B _removeViewOnHide;
B _resetAutoHideTimeOnRotation;
B _visualizeHitTestRect;
B _constrainHitTestRectToSafeAreaInset;
B _singleTapGatingEnabled;
q _initializationStyle;
q _edgeProtectOverride;
q _autoHideOverride;
d _autoHideTime;
d _autoHideTimeOnAppRequest;
d _delayForUnhideOnTouch;
d _delayForUnhideOnAppRequest;
d _hitTestOutsetTop;
d _hitTestOutsetSides;
d _hitTestOutsetDoubleTap;
d _bounceTranslation;
d _bounceReverseAnimationDelay;
@"SBFFluidBehaviorSettings" _bounceAnimationSettings;
@"SBFAnimationSettings" _hideAnimationSettings;
@"SBFAnimationSettings" _unhideAnimationSettings;
@"SBFAnimationSettings" _hideForHomeGestureOwnershipAnimationSettings;
@"SBFAnimationSettings" _unhideForHomeGestureOwnershipAnimationSettings;
@"SBFAnimationSettings" _thinToProminentAnimationSettings;
@"SBFAnimationSettings" _prominentToThinAnimationSettings;
@"SBFAnimationSettings" _forcedProminentToThinAnimationSettings;
@"SBFAnimationSettings" _lumaResponseAnimationSettings;
@"SBFAnimationSettings" _initialLumaResponseAnimationSettings;
@"SBFAnimationSettings" _rotationFadeOutAnimationSettings;
@"SBFAnimationSettings" _rotationFadeInAnimationSettings;
@"SBFFluidBehaviorSettings" _edgeProtectAnimationSettings;
d _coverSheetHomeAffordanceCursorTopEdgeInset;
d _coverSheetHomeAffordanceCursorBottomEdgeInset;
d _coverSheetHomeAffordanceCursorLeftEdgeInset;
d _coverSheetHomeAffordanceCursorRightEdgeInset;
d _coverSheetSuppressAnimationForPointerTopEdgeInset;
d _coverSheetSuppressAnimationForPointerBottomEdgeInset;
d _coverSheetSuppressAnimationForPointerLeftEdgeInset;
d _coverSheetSuppressAnimationForPointerRightEdgeInset;
```

## Properties

```
@property (Td,N,V_coverSheetHomeAffordanceCursorTopEdgeInset) coverSheetHomeAffordanceCursorTopEdgeInset;
@property (Td,N,V_coverSheetHomeAffordanceCursorBottomEdgeInset) coverSheetHomeAffordanceCursorBottomEdgeInset;
@property (Td,N,V_coverSheetHomeAffordanceCursorLeftEdgeInset) coverSheetHomeAffordanceCursorLeftEdgeInset;
@property (Td,N,V_coverSheetHomeAffordanceCursorRightEdgeInset) coverSheetHomeAffordanceCursorRightEdgeInset;
@property (Td,N,V_coverSheetSuppressAnimationForPointerTopEdgeInset) coverSheetSuppressAnimationForPointerTopEdgeInset;
@property (Td,N,V_coverSheetSuppressAnimationForPointerBottomEdgeInset) coverSheetSuppressAnimationForPointerBottomEdgeInset;
@property (Td,N,V_coverSheetSuppressAnimationForPointerLeftEdgeInset) coverSheetSuppressAnimationForPointerLeftEdgeInset;
@property (Td,N,V_coverSheetSuppressAnimationForPointerRightEdgeInset) coverSheetSuppressAnimationForPointerRightEdgeInset;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (Tq,N,V_initializationStyle) initializationStyle;
@property (TB,N,V_removeViewOnHide) removeViewOnHide;
@property (Tq,N,V_edgeProtectOverride) edgeProtectOverride;
@property (Tq,N,V_autoHideOverride) autoHideOverride;
@property (Td,N,V_autoHideTime) autoHideTime;
@property (Td,N,V_autoHideTimeOnAppRequest) autoHideTimeOnAppRequest;
@property (TB,N,V_resetAutoHideTimeOnRotation) resetAutoHideTimeOnRotation;
@property (Td,N,V_delayForUnhideOnTouch) delayForUnhideOnTouch;
@property (Td,N,V_delayForUnhideOnAppRequest) delayForUnhideOnAppRequest;
@property (TB,N,V_visualizeHitTestRect) visualizeHitTestRect;
@property (TB,N,V_constrainHitTestRectToSafeAreaInset) constrainHitTestRectToSafeAreaInset;
@property (Td,N,V_hitTestOutsetTop) hitTestOutsetTop;
@property (Td,N,V_hitTestOutsetSides) hitTestOutsetSides;
@property (Td,N,V_hitTestOutsetDoubleTap) hitTestOutsetDoubleTap;
@property (TB,N,GisSingleTapGatingEnabled,V_singleTapGatingEnabled) singleTapGatingEnabled;
@property (Td,N,V_bounceTranslation) bounceTranslation;
@property (Td,N,V_bounceReverseAnimationDelay) bounceReverseAnimationDelay;
@property (T@"SBFFluidBehaviorSettings",&,N,V_bounceAnimationSettings) bounceAnimationSettings;
@property (T@"SBFAnimationSettings",&,N,V_hideAnimationSettings) hideAnimationSettings;
@property (T@"SBFAnimationSettings",&,N,V_unhideAnimationSettings) unhideAnimationSettings;
@property (T@"SBFAnimationSettings",&,N,V_hideForHomeGestureOwnershipAnimationSettings) hideForHomeGestureOwnershipAnimationSettings;
@property (T@"SBFAnimationSettings",&,N,V_unhideForHomeGestureOwnershipAnimationSettings) unhideForHomeGestureOwnershipAnimationSettings;
@property (T@"SBFAnimationSettings",&,N,V_thinToProminentAnimationSettings) thinToProminentAnimationSettings;
@property (T@"SBFAnimationSettings",&,N,V_prominentToThinAnimationSettings) prominentToThinAnimationSettings;
@property (T@"SBFAnimationSettings",&,N,V_forcedProminentToThinAnimationSettings) forcedProminentToThinAnimationSettings;
@property (T@"SBFAnimationSettings",&,N,V_lumaResponseAnimationSettings) lumaResponseAnimationSettings;
@property (T@"SBFAnimationSettings",&,N,V_initialLumaResponseAnimationSettings) initialLumaResponseAnimationSettings;
@property (T@"SBFAnimationSettings",&,N,V_rotationFadeOutAnimationSettings) rotationFadeOutAnimationSettings;
@property (T@"SBFAnimationSettings",&,N,V_rotationFadeInAnimationSettings) rotationFadeInAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_edgeProtectAnimationSettings) edgeProtectAnimationSettings;
```

## Class methods

```
+[SBFHomeGrabberSettings settingsControllerModule];
```

## Instance methods

```
-[SBFHomeGrabberSettings setProminentToThinAnimationSettings:];
-[SBFHomeGrabberSettings setHideAnimationSettings:];
-[SBFHomeGrabberSettings rotationFadeInAnimationSettings];
-[SBFHomeGrabberSettings hideAnimationSettings];
-[SBFHomeGrabberSettings setCoverSheetSuppressAnimationForPointerRightEdgeInset:];
-[SBFHomeGrabberSettings setAutoHideOverride:];
-[SBFHomeGrabberSettings setAutoHideTimeOnAppRequest:];
-[SBFHomeGrabberSettings hitTestOutsetSides];
-[SBFHomeGrabberSettings setBounceTranslation:];
-[SBFHomeGrabberSettings isSingleTapGatingEnabled];
-[SBFHomeGrabberSettings setRotationFadeInAnimationSettings:];
-[SBFHomeGrabberSettings setCoverSheetHomeAffordanceCursorRightEdgeInset:];
-[SBFHomeGrabberSettings setThinToProminentAnimationSettings:];
-[SBFHomeGrabberSettings setHitTestOutsetDoubleTap:];
-[SBFHomeGrabberSettings setForcedProminentToThinAnimationSettings:];
-[SBFHomeGrabberSettings coverSheetHomeAffordanceCursorEdgeInsets];
-[SBFHomeGrabberSettings bounceAnimationSettings];
-[SBFHomeGrabberSettings setDelayForUnhideOnTouch:];
-[SBFHomeGrabberSettings setCoverSheetHomeAffordanceCursorLeftEdgeInset:];
-[SBFHomeGrabberSettings hideForHomeGestureOwnershipAnimationSettings];
-[SBFHomeGrabberSettings setResetAutoHideTimeOnRotation:];
-[SBFHomeGrabberSettings coverSheetHomeAffordanceCursorTopEdgeInset];
-[SBFHomeGrabberSettings setCoverSheetSuppressAnimationForPointerTopEdgeInset:];
-[SBFHomeGrabberSettings prominentToThinAnimationSettings];
-[SBFHomeGrabberSettings setEdgeProtectOverride:];
-[SBFHomeGrabberSettings setUnhideAnimationSettings:];
-[SBFHomeGrabberSettings resetAutoHideTimeOnRotation];
-[SBFHomeGrabberSettings setCoverSheetHomeAffordanceCursorBottomEdgeInset:];
-[SBFHomeGrabberSettings initializationStyle];
-[SBFHomeGrabberSettings setBounceAnimationSettings:];
-[SBFHomeGrabberSettings setConstrainHitTestRectToSafeAreaInset:];
-[SBFHomeGrabberSettings setInitializationStyle:];
-[SBFHomeGrabberSettings initialLumaResponseAnimationSettings];
-[SBFHomeGrabberSettings coverSheetHomeAffordanceCursorBottomEdgeInset];
-[SBFHomeGrabberSettings isEnabled];
-[SBFHomeGrabberSettings setCoverSheetHomeAffordanceCursorTopEdgeInset:];
-[SBFHomeGrabberSettings coverSheetSuppressAnimationForPointerRightEdgeInset];
-[SBFHomeGrabberSettings lumaResponseAnimationSettings];
-[SBFHomeGrabberSettings setLumaResponseAnimationSettings:];
-[SBFHomeGrabberSettings setBounceReverseAnimationDelay:];
-[SBFHomeGrabberSettings unhideForHomeGestureOwnershipAnimationSettings];
-[SBFHomeGrabberSettings hitTestOutsetTop];
-[SBFHomeGrabberSettings setDefaultValues];
-[SBFHomeGrabberSettings autoHideOverride];
-[SBFHomeGrabberSettings setEnabled:];
-[SBFHomeGrabberSettings coverSheetSuppressAnimationForPointerTopEdgeInset];
-[SBFHomeGrabberSettings constrainHitTestRectToSafeAreaInset];
-[SBFHomeGrabberSettings setSingleTapGatingEnabled:];
-[SBFHomeGrabberSettings setCoverSheetSuppressAnimationForPointerBottomEdgeInset:];
-[SBFHomeGrabberSettings coverSheetSuppressAnimationForPointerLeftEdgeInset];
-[SBFHomeGrabberSettings setVisualizeHitTestRect:];
-[SBFHomeGrabberSettings unhideAnimationSettings];
-[SBFHomeGrabberSettings delayForUnhideOnAppRequest];
-[SBFHomeGrabberSettings autoHideTimeOnAppRequest];
-[SBFHomeGrabberSettings autoHideTime];
-[SBFHomeGrabberSettings hitTestOutsetDoubleTap];
-[SBFHomeGrabberSettings bounceReverseAnimationDelay];
-[SBFHomeGrabberSettings edgeProtectOverride];
-[SBFHomeGrabberSettings setUnhideForHomeGestureOwnershipAnimationSettings:];
-[SBFHomeGrabberSettings thinToProminentAnimationSettings];
-[SBFHomeGrabberSettings coverSheetSuppressAnimationForPointerBottomEdgeInset];
-[SBFHomeGrabberSettings edgeProtectAnimationSettings];
-[SBFHomeGrabberSettings setHitTestOutsetTop:];
-[SBFHomeGrabberSettings setInitialLumaResponseAnimationSettings:];
-[SBFHomeGrabberSettings removeViewOnHide];
-[SBFHomeGrabberSettings visualizeHitTestRect];
-[SBFHomeGrabberSettings setHitTestOutsetSides:];
-[SBFHomeGrabberSettings setEdgeProtectAnimationSettings:];
-[SBFHomeGrabberSettings bounceTranslation];
-[SBFHomeGrabberSettings coverSheetSuppressAnimationForPointerInsets];
-[SBFHomeGrabberSettings rotationFadeOutAnimationSettings];
-[SBFHomeGrabberSettings delayForUnhideOnTouch];
-[SBFHomeGrabberSettings setCoverSheetSuppressAnimationForPointerLeftEdgeInset:];
-[SBFHomeGrabberSettings setRemoveViewOnHide:];
-[SBFHomeGrabberSettings forcedProminentToThinAnimationSettings];
-[SBFHomeGrabberSettings coverSheetHomeAffordanceCursorLeftEdgeInset];
-[SBFHomeGrabberSettings setHideForHomeGestureOwnershipAnimationSettings:];
-[SBFHomeGrabberSettings setAutoHideTime:];
-[SBFHomeGrabberSettings setRotationFadeOutAnimationSettings:];
-[SBFHomeGrabberSettings coverSheetHomeAffordanceCursorRightEdgeInset];
-[SBFHomeGrabberSettings setDelayForUnhideOnAppRequest:];
```
