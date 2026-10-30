# `_UIPhysicalButtonInteractionArbiter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIEventDeferringEnvironmentTargetProviding`, `_UIEventDeferringRuleOwning`, `_UIWindowLevelObserver`, `_UISceneInteractionRegistrationTarget`, `_UIWindowHostingSceneComponentProviding`, `BSDebugDescriptionProviding`
- 19 instance variables, 7 properties, 26 instance methods, 0 class methods

## Instance variables

```
@? _viewServiceValidationBlock;
@? _interactionValidationBlock;
@"NSMutableArray" _uniqueConfigurationGenerationNumbers;
@"<BSInvalidatable>" _stateCaptureToken;
{?="hasRegisteredAsEventDeferringEnvironmentTargetProvider"b1"hasScheduledDeferredConfigurationResolution"b1"hasScheduledDeferredConfigurationResolutionForReentrancy"b1"configurationResolutionPaused"b1"needsConfigurationResolutionWhenResumed"b1"systemShellRequestedConfigurationResolution"b1} _arbiterFlags;
@"UIScene" _scene;
@"<_UIPhysicalButtonInteractionArbiterSystemShellDelegate>" _systemShellDelegate;
Q _resolutionStrategy;
@"_UIEvaluatedObjectCache" _registeredAndSortedInteractions;
@"NSHashTable" _trackedWindowPointers;
@"NSCountedSet" _countedWindowPointerValues;
@"NSCountedSet" _windowPointersObservedForLevelChanges;
@"CADisplayLink" _deferredConfigurationResolutionDisplayLink;
@"_UIPhysicalButtonConfigurationResolutionContext" _sceneConfigurationResolutionContext;
@"NSHashTable" _systemShellWindowsRequiringResolution;
@"NSMapTable" _systemShellWindowConfigurationResolutionContexts;
@"_UIViewServiceSessionActivityRecord" _mostActiveViewServiceSession;
@"NSHashTable" _viewServiceObservers;
@"NSMutableDictionary" _eventDeferringTokenByEnvironment;
```

## Properties

```
@property (T@"<_UIPhysicalButtonInteractionArbiterSystemShellDelegate>",W,N,V_systemShellDelegate) systemShellDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIScene<_UISceneUIWindowHosting>",R,N) _windowHostingScene;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
```

## Instance methods

```
-[_UIPhysicalButtonInteractionArbiter _windowHostingScene];
-[_UIPhysicalButtonInteractionArbiter interfaceElementCategory];
-[_UIPhysicalButtonInteractionArbiter localEventDeferringTargetWindowForEnvironment:];
-[_UIPhysicalButtonInteractionArbiter _scene];
-[_UIPhysicalButtonInteractionArbiter debugDescription];
-[_UIPhysicalButtonInteractionArbiter _windowVisibilityDidChange:];
-[_UIPhysicalButtonInteractionArbiter _windowHostingScene:willMoveFromScreen:toScreen:];
-[_UIPhysicalButtonInteractionArbiter succinctDescriptionBuilder];
-[_UIPhysicalButtonInteractionArbiter init];
-[_UIPhysicalButtonInteractionArbiter window:changedFromLevel:toLevel:];
-[_UIPhysicalButtonInteractionArbiter _sceneWillInvalidate:];
-[_UIPhysicalButtonInteractionArbiter setSystemShellDelegate:];
-[_UIPhysicalButtonInteractionArbiter dealloc];
-[_UIPhysicalButtonInteractionArbiter descriptionWithMultilinePrefix:];
-[_UIPhysicalButtonInteractionArbiter initWithScene:];
-[_UIPhysicalButtonInteractionArbiter _mostActiveViewServiceSessionDidChange:];
-[_UIPhysicalButtonInteractionArbiter succinctDescription];
-[_UIPhysicalButtonInteractionArbiter configurationResolutionContextForSystemShellWindow:];
-[_UIPhysicalButtonInteractionArbiter debugDescriptionWithMultilinePrefix:];
-[_UIPhysicalButtonInteractionArbiter setNeedsResolutionOfPhysicalButtonConfigurationsForSystemShellDelegate:];
-[_UIPhysicalButtonInteractionArbiter _deferredResolutionDisplayLinkTicked:];
-[_UIPhysicalButtonInteractionArbiter description];
-[_UIPhysicalButtonInteractionArbiter _setScene:];
-[_UIPhysicalButtonInteractionArbiter _actionRespondersForScene:];
-[_UIPhysicalButtonInteractionArbiter descriptionBuilderWithMultilinePrefix:];
-[_UIPhysicalButtonInteractionArbiter systemShellDelegate];
```
