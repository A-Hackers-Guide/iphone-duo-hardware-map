# `UIWindowSceneActivationInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction_Internal`, `UIGestureRecognizerDelegate`, `_UIWindowSceneActivator_Internal`, `UIInteraction`
- 8 instance variables, 13 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@? _configurationProvider;
@? _errorHandler;
@"UIWindowSceneActivationConfiguration" _activeConfiguration;
@"_UIWindowSceneActivationEffect" _activeEffect;
@"_UIWindowSceneActivationAnimator" _animator;
@"UIPinchGestureRecognizer" _pinchGR;
@"_UIDoubleTapInteraction" _doubleTapInteraction;
```

## Properties

```
@property (T@?,C,N,V_configurationProvider) configurationProvider;
@property (T@?,C,N,V_errorHandler) errorHandler;
@property (T@"UIWindowSceneActivationConfiguration",&,N,V_activeConfiguration) activeConfiguration;
@property (T@"_UIWindowSceneActivationEffect",&,N,V_activeEffect) activeEffect;
@property (T@"_UIWindowSceneActivationAnimator",&,N,V_animator) animator;
@property (T@"UIPinchGestureRecognizer",&,N,V_pinchGR) pinchGR;
@property (T@"_UIDoubleTapInteraction",&,N,V_doubleTapInteraction) doubleTapInteraction;
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIWindowSceneActivationInteraction activeConfiguration];
-[UIWindowSceneActivationInteraction setAnimator:];
-[UIWindowSceneActivationInteraction animator];
-[UIWindowSceneActivationInteraction doubleTapInteraction];
-[UIWindowSceneActivationInteraction _supportsAssociation];
-[UIWindowSceneActivationInteraction view];
-[UIWindowSceneActivationInteraction setActiveConfiguration:];
-[UIWindowSceneActivationInteraction _targetedPreviewForContinuingEffectWithPreview:];
-[UIWindowSceneActivationInteraction configurationProvider];
-[UIWindowSceneActivationInteraction willMoveToView:];
-[UIWindowSceneActivationInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[UIWindowSceneActivationInteraction setDoubleTapInteraction:];
-[UIWindowSceneActivationInteraction setErrorHandler:];
-[UIWindowSceneActivationInteraction _viewTraitCollectionDidChange:];
-[UIWindowSceneActivationInteraction didMoveToView:];
-[UIWindowSceneActivationInteraction errorHandler];
-[UIWindowSceneActivationInteraction pinchGR];
-[UIWindowSceneActivationInteraction _animateExpansionWithVelocity:];
-[UIWindowSceneActivationInteraction _canAnimateSceneActivationWithConfiguration:];
-[UIWindowSceneActivationInteraction _cancelInteraction];
-[UIWindowSceneActivationInteraction _endEffectWithVelocity:forActiveConfigurationWithCompletionStatus:];
-[UIWindowSceneActivationInteraction _handlePinchGesture:];
-[UIWindowSceneActivationInteraction _prepareEffectForActiveConfigurationAtLocation:completion:];
-[UIWindowSceneActivationInteraction _prepareSceneActivationConfiguration:];
-[UIWindowSceneActivationInteraction _prewarmAnimationWithCompletion:];
-[UIWindowSceneActivationInteraction _requestConfigurationForLocation:];
-[UIWindowSceneActivationInteraction _requestSceneActivationWithConfiguration:animated:sender:errorHandler:];
-[UIWindowSceneActivationInteraction _shouldActivateForEndingPinch:];
-[UIWindowSceneActivationInteraction _uninstallSceneActivationGestures];
-[UIWindowSceneActivationInteraction _updateSceneActivationGestures];
-[UIWindowSceneActivationInteraction activeEffect];
-[UIWindowSceneActivationInteraction initWithConfigurationProvider:errorHandler:];
-[UIWindowSceneActivationInteraction setActiveEffect:];
-[UIWindowSceneActivationInteraction setConfigurationProvider:];
-[UIWindowSceneActivationInteraction setPinchGR:];
```
