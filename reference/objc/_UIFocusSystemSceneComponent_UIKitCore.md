# `_UIFocusSystemSceneComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFocusSystemDelegate`, `_UISceneComponentProviding`, `_UIWindowSceneComponentProviding`, `UIFocusItemContainer`
- 18 instance variables, 24 properties, 78 instance methods, 6 class methods

## Instance variables

```
@"UIResponder" _expectedFirstResponder;
@"NSMutableSet" _overrideFocusSystemEnablementIdentifiers;
{?="sceneIsValid"b1"wantsModernRing"b1"isUpdatingToNewFirstResponder"b1} _flags;
@"_UIFocusItemFrameReporter" _focusItemFrameReporter;
@"_UIFocusEventDelivery" _eventDelivery;
@"_UIFocusIntelligenceProvider" _intelligenceProvider;
@"UIScene" _scene;
@"_UIFocusEffectManager" _focusEffectManager;
@"UIFocusSystem" _focusSystem;
@"_UIFocusHardwareKeyboardObserver" _hardwareKeyboardObserver;
@"_UIFocusGameControllerObserver" _gameControllerObserver;
@"NSPointerArray" _preferredFocusEnvironmentOverride;
@"_UIFocusActiveSceneObserver" _activeSceneObserver;
@"_UIFocusSceneHostAssertionObserver" _sceneHostAssertionObserver;
@"_UIFocusSoundGenerator" _soundGenerator;
@"_UIFocusHapticFeedbackGenerator" _hapticFeedbackGenerator;
@"_UIFocusScrollManager" _scrollManager;
@"_UIFocusAnimationCoordinatorManager" _focusAnimationCoordinatorManager;
```

## Properties

```
@property (T@"UIFocusSystem",&,N,V_focusSystem) focusSystem;
@property (T@"_UIFocusHardwareKeyboardObserver",R,N,V_hardwareKeyboardObserver) hardwareKeyboardObserver;
@property (T@"_UIFocusGameControllerObserver",R,N,V_gameControllerObserver) gameControllerObserver;
@property (T@"_UIFocusEffectManager",R,N,G_focusEffectManager,V_focusEffectManager) focusEffectManager;
@property (T@"NSPointerArray",R,N,V_preferredFocusEnvironmentOverride) preferredFocusEnvironmentOverride;
@property (T@"_UIFocusItemFrameReporter",&,N,V_focusItemFrameReporter) _focusItemFrameReporter;
@property (T@"_UIFocusActiveSceneObserver",R,N,V_activeSceneObserver) activeSceneObserver;
@property (T@"_UIFocusSceneHostAssertionObserver",R,N,V_sceneHostAssertionObserver) sceneHostAssertionObserver;
@property (T@"_UIFocusSoundGenerator",&,N,V_soundGenerator) soundGenerator;
@property (T@"_UIFocusHapticFeedbackGenerator",&,N,V_hapticFeedbackGenerator) hapticFeedbackGenerator;
@property (T@"_UIFocusScrollManager",R,N,V_scrollManager) scrollManager;
@property (T@"_UIFocusEventDelivery",R,N,V_eventDelivery) _eventDelivery;
@property (T@"_UIFocusIntelligenceProvider",R,N,V_intelligenceProvider) _intelligenceProvider;
@property (T@"_UIFocusAnimationCoordinatorManager",R,N,V_focusAnimationCoordinatorManager) focusAnimationCoordinatorManager;
@property (T@"UIWindowScene",R,N,G_windowScene) windowScene;
@property (TB,R,N) isOverrideFocusSystemEnabled;
@property (TB,N,G_uiktest_allowsForwardingFocusMovementActions,S_uiktest_setAllowsForwardingFocusMovementActions:) allowsForwardingFocusMovementActions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (T@"UITraitCollection",?,R,N) _traitOverrides;
@property (T@"<UICoordinateSpace>",R,N) coordinateSpace;
```

## Class methods

```
+[_UIFocusSystemSceneComponent _supportsInvalidatingFocusCache];
+[_UIFocusSystemSceneComponent _screenForScene:];
+[_UIFocusSystemSceneComponent __applicationIsSpringBoard];
+[_UIFocusSystemSceneComponent sceneComponentForFocusSystem:];
+[_UIFocusSystemSceneComponent needsFocusSystem];
+[_UIFocusSystemSceneComponent sceneComponentForEnvironment:];
```

## Instance methods

```
-[_UIFocusSystemSceneComponent _windowScene];
-[_UIFocusSystemSceneComponent _focusItemFrameReporter];
-[_UIFocusSystemSceneComponent setOverrideFocusSystemEnabled:withIdentifier:];
-[_UIFocusSystemSceneComponent setSoundGenerator:];
-[_UIFocusSystemSceneComponent _windowHostingScene:didMoveFromScreen:toScreen:];
-[_UIFocusSystemSceneComponent _isSceneActive];
-[_UIFocusSystemSceneComponent _uiktest_forceSceneActive];
-[_UIFocusSystemSceneComponent coordinateSpace];
-[_UIFocusSystemSceneComponent _focusSystemExplicitlyDisabledForBehavior:];
-[_UIFocusSystemSceneComponent _firstResponderDidUpdateFromResponder:];
-[_UIFocusSystemSceneComponent _scene];
-[_UIFocusSystemSceneComponent _updateWantsModernRing];
-[_UIFocusSystemSceneComponent _updateFocusSystemCapabilities];
-[_UIFocusSystemSceneComponent _focusSystem:willMessageNewFocusNodes:];
-[_UIFocusSystemSceneComponent _windowHostingScene:willMoveFromScreen:toScreen:];
-[_UIFocusSystemSceneComponent _overridingPreferredFocusEnvironmentForFocusSystem:];
-[_UIFocusSystemSceneComponent focusItemsInRect:];
-[_UIFocusSystemSceneComponent _uiktest_setAllowsForwardingFocusMovementActions:];
-[_UIFocusSystemSceneComponent sceneHostAssertionObserver];
-[_UIFocusSystemSceneComponent soundGenerator];
-[_UIFocusSystemSceneComponent _focusSystem:shouldRestoreFocusInContext:];
-[_UIFocusSystemSceneComponent _focusSystem:didUpdateFocusInContext:];
-[_UIFocusSystemSceneComponent _traitOverrides];
-[_UIFocusSystemSceneComponent focusAnimationCoordinatorManager];
-[_UIFocusSystemSceneComponent _sceneWillInvalidate:];
-[_UIFocusSystemSceneComponent _focusSystem:didFinishUpdatingFocusInContext:];
-[_UIFocusSystemSceneComponent _eventDelivery];
-[_UIFocusSystemSceneComponent _validateFocusedItemForFirstResponder:];
-[_UIFocusSystemSceneComponent preferredFocusEnvironmentOverride];
-[_UIFocusSystemSceneComponent _updateDeviceCapabilityObserver];
-[_UIFocusSystemSceneComponent _focusBehaviorRespectingApplicationOverride:];
-[_UIFocusSystemSceneComponent pushPreferredFocusEnvironmentOverride:];
-[_UIFocusSystemSceneComponent _uiktest_allowsForwardingFocusMovementActions];
-[_UIFocusSystemSceneComponent _focusSystem:handleFailedMovementRequest:];
-[_UIFocusSystemSceneComponent initWithScene:];
-[_UIFocusSystemSceneComponent _clippingRectForFocusSystem:inCoordinateSpace:];
-[_UIFocusSystemSceneComponent _preferredFocusEnvironmentsForFocusSystem:];
-[_UIFocusSystemSceneComponent _shouldForwardFocusMovementRequest:];
-[_UIFocusSystemSceneComponent _focusSystem:isScrollingScrollableContainer:targetContentOffset:];
-[_UIFocusSystemSceneComponent _windowsForFocusSearch];
-[_UIFocusSystemSceneComponent setFocusSystem:];
-[_UIFocusSystemSceneComponent _notifyDidPerformFocusSystemInitialSetup];
-[_UIFocusSystemSceneComponent removePreferredFocusEnvironmentOverride:];
-[_UIFocusSystemSceneComponent _focusSystem:shouldReverseLayoutDirectionForEnvironment:];
-[_UIFocusSystemSceneComponent _topEnvironmentForFocusSystem:];
-[_UIFocusSystemSceneComponent _focusBehaviorDidChange:];
-[_UIFocusSystemSceneComponent focusSystem];
-[_UIFocusSystemSceneComponent _adjustFocusSystemAvailabilityUpdatingTraits:];
-[_UIFocusSystemSceneComponent setHapticFeedbackGenerator:];
-[_UIFocusSystemSceneComponent _focusSystem:willMessageOldFocusNodes:];
-[_UIFocusSystemSceneComponent _isFocusSystemActive];
-[_UIFocusSystemSceneComponent description];
-[_UIFocusSystemSceneComponent _requestFocusEffectUpdateToEnvironment:];
-[_UIFocusSystemSceneComponent hapticFeedbackGenerator];
-[_UIFocusSystemSceneComponent _focusSystem:didUpdateDeferralTarget:];
-[_UIFocusSystemSceneComponent _updateFocusEffectForItem:];
-[_UIFocusSystemSceneComponent gameControllerObserver];
-[_UIFocusSystemSceneComponent _setScene:];
-[_UIFocusSystemSceneComponent _shouldWaitForFocusMovementActionToEnableFocusSystem:];
-[_UIFocusSystemSceneComponent _setupFocusSystem];
-[_UIFocusSystemSceneComponent hardwareKeyboardObserver];
-[_UIFocusSystemSceneComponent _focusSystem:didCancelFocusUpdateInContext:];
-[_UIFocusSystemSceneComponent _tearDownFocusSystem];
-[_UIFocusSystemSceneComponent _focusSystem:shouldReverseLinearWrappingForEnvironment:];
-[_UIFocusSystemSceneComponent _resetFocusEventRecognizers];
-[_UIFocusSystemSceneComponent _adjustFocusSystemAvailability];
-[_UIFocusSystemSceneComponent _focusSystemEnabledStateDidChange:];
-[_UIFocusSystemSceneComponent scrollManager];
-[_UIFocusSystemSceneComponent _focusSystem:environment:didUpdateFocusInContext:];
-[_UIFocusSystemSceneComponent _focusSystem:willUpdateFocusInContext:];
-[_UIFocusSystemSceneComponent activeSceneObserver];
-[_UIFocusSystemSceneComponent isOverrideFocusSystemEnabled];
-[_UIFocusSystemSceneComponent _intelligenceProvider];
-[_UIFocusSystemSceneComponent _syncResponderWithFocusUpdateContext:];
-[_UIFocusSystemSceneComponent set_focusItemFrameReporter:];
-[_UIFocusSystemSceneComponent _focusEffectManager];
-[_UIFocusSystemSceneComponent _focusItemContainerForFocusSystem:];
-[_UIFocusSystemSceneComponent _updateFocusSystemState];
```
