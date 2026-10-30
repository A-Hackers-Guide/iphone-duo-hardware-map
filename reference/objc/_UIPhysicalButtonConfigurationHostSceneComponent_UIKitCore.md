# `_UIPhysicalButtonConfigurationHostSceneComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `FBSceneObserver`, `_UIPhysicalButtonProxyInteractionDelegate`
- 3 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
{?="needsSceneEligibilityEvaluation"b1"sceneIsEligibleForProxyInteraction"b1} _flags;
@"_UIPhysicalButtonConfigurationSet" _clientPhysicalButtonConfigurations;
@"_UIPhysicalButtonProxyInteraction" _proxyPhysicalButtonInteraction;
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
-[_UIPhysicalButtonConfigurationHostSceneComponent sceneWillActivate:];
-[_UIPhysicalButtonConfigurationHostSceneComponent debugDescription];
-[_UIPhysicalButtonConfigurationHostSceneComponent _physicalButtonProxyInteraction:didReceiveBSAction:];
-[_UIPhysicalButtonConfigurationHostSceneComponent setScene:];
-[_UIPhysicalButtonConfigurationHostSceneComponent description];
-[_UIPhysicalButtonConfigurationHostSceneComponent appendDescriptionToStream:];
-[_UIPhysicalButtonConfigurationHostSceneComponent scene:didUpdateClientSettings:];
-[_UIPhysicalButtonConfigurationHostSceneComponent _physicalButtonInteraction:handleAction:withActiveActions:];
```
