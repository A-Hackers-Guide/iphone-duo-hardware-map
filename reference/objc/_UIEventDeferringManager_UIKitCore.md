# `_UIEventDeferringManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIEventDeferringEnvironmentTargetProviding`, `_UIEventDeferringManagerCoordinating`, `BSDebugDescriptionProviding`, `_UIWindowHostingSceneComponentProviding`
- 15 instance variables, 7 properties, 22 instance methods, 2 class methods

## Instance variables

```
Q _currentState;
@"NSMutableDictionary" _localContainerDeferringTokensByEnvironment;
@"NSMutableDictionary" _localDeferringRecordsByEnvironment;
@"NSMutableDictionary" _remoteDeferringRecordStacksByEnvironment;
@"NSMapTable" _targetWindowProvidersByEnvironment;
@"NSMutableDictionary" _trackedLocalTargetWindowPointersByEnvironment;
@"NSCountedSet" _localTargetWindowPointersUnderObservation;
@"NSString" _previousScreenHardwareIdentifier;
@"<BSInvalidatable>" _stateCaptureToken;
Aq _bufferingAssertionCount;
{?="availableForProcess"b1"hasInvalidated"b1"evaluatedInitialExternalScreenDisconnection"b1"processingScreenIdentifierWillChange"b1"processedScreenIdentifierWillChange"b1"processingScreenIdentifierDidChange"b1"processingSceneChangingScreens"b1} _deferringManagerFlags;
@"UIScene" _scene;
@"<BSInvalidatable>" _transactionAssertion;
@"BKSHIDEventDeferringToken" _localContainerToken;
@"<_UIEventDeferringBehavior>" _behavior;
```

## Properties

```
@property (T@"UIScene<_UISceneUIWindowHosting>",R,W,N) windowHostingScene;
@property (T@"<_UIEventDeferringBehavior>",R,N,V_behavior) behavior;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
```

## Class methods

```
+[_UIEventDeferringManager systemShellBehaviorDelegate];
+[_UIEventDeferringManager setSystemShellBehaviorDelegate:];
```

## Instance methods

```
-[_UIEventDeferringManager eventDeferringManager:didRemoveLocalCompatibilityRecordForDescriptor:];
-[_UIEventDeferringManager _screenUniqueIdDidChange:];
-[_UIEventDeferringManager _localTargetWindowDidDetachContext:];
-[_UIEventDeferringManager localEventDeferringTargetWindowForEnvironment:];
-[_UIEventDeferringManager _windowHostingScene:didMoveFromScreen:toScreen:];
-[_UIEventDeferringManager _scene];
-[_UIEventDeferringManager debugDescription];
-[_UIEventDeferringManager succinctDescriptionBuilder];
-[_UIEventDeferringManager _sceneWillInvalidate:];
-[_UIEventDeferringManager dealloc];
-[_UIEventDeferringManager descriptionWithMultilinePrefix:];
-[_UIEventDeferringManager initWithScene:];
-[_UIEventDeferringManager succinctDescription];
-[_UIEventDeferringManager behavior];
-[_UIEventDeferringManager windowHostingScene];
-[_UIEventDeferringManager debugDescriptionWithMultilinePrefix:];
-[_UIEventDeferringManager description];
-[_UIEventDeferringManager _localTargetWindowDidAttachContext:];
-[_UIEventDeferringManager _setScene:];
-[_UIEventDeferringManager _screenUniqueIdWillChange:];
-[_UIEventDeferringManager setNeedsRemoteEventDeferringRuleComparisonInEnvironments:forBehaviorDelegate:withReason:];
-[_UIEventDeferringManager descriptionBuilderWithMultilinePrefix:];
```
