# `_UISceneHostingActivationStateHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `_UISceneHostingActivating`, `_UISceneRelationshipManagementHostComponentObserver`, `FBSceneComponent`
- 8 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"<_UIRemoteContentParent>" _parentEnvironment;
I _foregroundAssertionCount;
B _isCurrentlyPropagatingForeground;
@"_UISceneHostingActivationHandle" _activationHandle;
@"FBSSceneTransitionContext" _pendingTransitionContext;
I _activationSuppressionCount;
{?="_activationControllerImplementsIsMovingToParentScene"b1"_activationControllerImplementsActivationHandleUpdated"b1"_hasPendingActivation"b1} _flags;
@"<_UISceneHostingActivationControlling>" _activationController;
```

## Properties

```
@property (T@"<_UISceneHostingActivationControlling>",&,N,V_activationController) activationController;
@property (TB,R,N,GisActive) active;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneHostingActivationStateHostComponent activationSuppressionAssertionForReason:];
-[_UISceneHostingActivationStateHostComponent setForeground:];
-[_UISceneHostingActivationStateHostComponent sceneDidInvalidate:withContext:];
-[_UISceneHostingActivationStateHostComponent propagateForeground:];
-[_UISceneHostingActivationStateHostComponent setActivationController:];
-[_UISceneHostingActivationStateHostComponent sceneDidActivate:];
-[_UISceneHostingActivationStateHostComponent deactivate:];
-[_UISceneHostingActivationStateHostComponent setScene:];
-[_UISceneHostingActivationStateHostComponent activationController];
-[_UISceneHostingActivationStateHostComponent evaluateActivationState];
-[_UISceneHostingActivationStateHostComponent isActivationSuppressed];
-[_UISceneHostingActivationStateHostComponent foregroundAssertionForReason:];
-[_UISceneHostingActivationStateHostComponent _createTransitionContext];
-[_UISceneHostingActivationStateHostComponent _activate:];
-[_UISceneHostingActivationStateHostComponent _scene:isMovingToParent:];
-[_UISceneHostingActivationStateHostComponent evaluateActivationSuppression];
-[_UISceneHostingActivationStateHostComponent isActive];
-[_UISceneHostingActivationStateHostComponent activate:];
-[_UISceneHostingActivationStateHostComponent ui_sceneDidDeactivate:withContext:];
```
