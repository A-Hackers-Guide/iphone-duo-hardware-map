# `SBKeyboardFocusService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_SBKeyboardServiceConnectionListenerDelegate`
- 8 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<SBKeyboardFocusControlling>" _keyboardFocusController;
@"<_SBSceneResolving>" _sceneResolver;
@"<_SBKeyboardServiceConnectionListening>" _serviceConnectionListener;
@"NSHashTable" _focusRequestedScenes;
@"NSMapTable" _lock_additionalDeferringRulesByClient;
@"NSMapTable" _lock_externalSceneIdentitiesByClient;
@"NSObject<OS_dispatch_queue>" _serviceQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
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
-[SBKeyboardFocusService clientDidConnect:];
-[SBKeyboardFocusService _lock_updateExternalSceneIdentities];
-[SBKeyboardFocusService client:deferAdditionalEnvironments:whenSceneHasKeyboardFocus:pid:];
-[SBKeyboardFocusService client:removeKeyboardFocusFromSceneIdentity:pid:];
-[SBKeyboardFocusService client:requestKeyboardFocusForSceneIdentity:pid:completion:];
-[SBKeyboardFocusService client:setExternalSceneIdentities:];
-[SBKeyboardFocusService client:stopApplyingAdditionalDeferringRulesWhenSceneHasKeyboardFocus:pid:];
-[SBKeyboardFocusService clientDidDisconnect:];
-[SBKeyboardFocusService initWithKeyboardFocusController:sceneResolver:serviceListenerFactory:];
-[SBKeyboardFocusService initWithSceneStore:keyboardFocusController:systemUIScenesCoordinator:];
```
