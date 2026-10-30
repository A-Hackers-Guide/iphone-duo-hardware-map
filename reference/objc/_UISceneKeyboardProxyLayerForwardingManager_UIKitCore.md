# `_UISceneKeyboardProxyLayerForwardingManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneKeyboardProxyLayerForwardingPresentationEnvironmentObserver`
- 1 instance variables, 4 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"NSMapTable" _mapEnvironmentToKeyboardForwardingStateMachine;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISceneKeyboardProxyLayerForwardingManager sharedInstance];
+[_UISceneKeyboardProxyLayerForwardingManager isRootSystemShellProcess];
+[_UISceneKeyboardProxyLayerForwardingManager new];
```

## Instance methods

```
-[_UISceneKeyboardProxyLayerForwardingManager _updateKeyboardLayersForPresentationEnvironment:];
-[_UISceneKeyboardProxyLayerForwardingManager debugDescription];
-[_UISceneKeyboardProxyLayerForwardingManager succinctDescriptionBuilder];
-[_UISceneKeyboardProxyLayerForwardingManager init];
-[_UISceneKeyboardProxyLayerForwardingManager descriptionWithMultilinePrefix:];
-[_UISceneKeyboardProxyLayerForwardingManager trackPresentationEnvironment:];
-[_UISceneKeyboardProxyLayerForwardingManager _init];
-[_UISceneKeyboardProxyLayerForwardingManager succinctDescription];
-[_UISceneKeyboardProxyLayerForwardingManager _newStateMachineWithPresentationEnvironment:];
-[_UISceneKeyboardProxyLayerForwardingManager _stateMachineForPresentationEnvironment:];
-[_UISceneKeyboardProxyLayerForwardingManager description];
-[_UISceneKeyboardProxyLayerForwardingManager presentationEnvironmentDidInvalidate:];
-[_UISceneKeyboardProxyLayerForwardingManager descriptionBuilderWithMultilinePrefix:];
```
