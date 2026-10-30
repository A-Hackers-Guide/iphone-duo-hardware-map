# `_UIPhysicalButtonInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPhysicalButtonInteractionDriverReceiving`, `_UIGeometryChangeObserver`, `BSDebugDescriptionProviding`, `UIInteraction`
- 12 instance variables, 15 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _drivers;
@"NSMutableDictionary" _actionsByPhysicalButton;
@"NSMutableArray" _orderedActionsForAllPhysicalButtons;
{?="wantsRelaxedVisibilityRequirement"b1"wantsSystemShellExclusivePriority"b1"hasExclusiveBehaviorConfiguration"b1"isWithinSceneBounds"b1} _interactionFlags;
B _enabled;
@"UIView" _view;
@"_UIPhysicalButtonConfigurationSet" _configurationSet;
@"<_UIPhysicalButtonInteractionDelegate>" _delegate;
Q _identifier;
@"NSString" _name;
@"<BSInvalidatable>" _arbiterRegistrationToken;
@"_UISceneTargetingInteraction" _registrationInteraction;
```

## Properties

```
@property (TB,R,N) _isProxyInteraction;
@property (T@"NSArray",R,C,N) _driverClasses;
@property (T@"_UIPhysicalButtonConfigurationSet",R,C,N,V_configurationSet) _configurationSet;
@property (TB,N,S_setWantsRelaxedVisibilityRequirement:) _wantsRelaxedVisibilityRequirement;
@property (TB,N,S_setWantsSystemShellExclusivePriority:) _wantsSystemShellExclusivePriority;
@property (T@"NSSet",C,N,S_setConfigurations:) _configurations;
@property (T@"<_UIPhysicalButtonInteractionDelegate>",R,W,N,V_delegate) _delegate;
@property (TQ,N,S_setIdentifier:,V_identifier) _identifier;
@property (T@"NSString",C,N,S_setName:,V_name) _name;
@property (TB,N,G_isEnabled,S_setEnabled:,V_enabled) _enabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[_UIPhysicalButtonInteraction _setName:];
-[_UIPhysicalButtonInteraction _setIdentifier:];
-[_UIPhysicalButtonInteraction _name];
-[_UIPhysicalButtonInteraction _configurationForButton:];
-[_UIPhysicalButtonInteraction debugDescription];
-[_UIPhysicalButtonInteraction _setEnabled:];
-[_UIPhysicalButtonInteraction _isEnabled];
-[_UIPhysicalButtonInteraction succinctDescriptionBuilder];
-[_UIPhysicalButtonInteraction init];
-[_UIPhysicalButtonInteraction _setConfigurations:];
-[_UIPhysicalButtonInteraction dealloc];
-[_UIPhysicalButtonInteraction _driver:didCreateProposedAction:];
-[_UIPhysicalButtonInteraction _isProxyInteraction];
-[_UIPhysicalButtonInteraction descriptionWithMultilinePrefix:];
-[_UIPhysicalButtonInteraction _wantsSystemShellExclusivePriority];
-[_UIPhysicalButtonInteraction _geometryChanged:forAncestor:];
-[_UIPhysicalButtonInteraction succinctDescription];
-[_UIPhysicalButtonInteraction _delegate];
-[_UIPhysicalButtonInteraction view];
-[_UIPhysicalButtonInteraction _driverClasses];
-[_UIPhysicalButtonInteraction _wantsRelaxedVisibilityRequirement];
-[_UIPhysicalButtonInteraction initWithConfigurations:delegate:];
-[_UIPhysicalButtonInteraction debugDescriptionWithMultilinePrefix:];
-[_UIPhysicalButtonInteraction willMoveToView:];
-[_UIPhysicalButtonInteraction _configurations];
-[_UIPhysicalButtonInteraction description];
-[_UIPhysicalButtonInteraction _setWantsSystemShellExclusivePriority:];
-[_UIPhysicalButtonInteraction _setWantsRelaxedVisibilityRequirement:];
-[_UIPhysicalButtonInteraction _identifier];
-[_UIPhysicalButtonInteraction didMoveToView:];
-[_UIPhysicalButtonInteraction _configurationSet];
-[_UIPhysicalButtonInteraction descriptionBuilderWithMultilinePrefix:];
```
