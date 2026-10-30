# `_UISceneKeyboardProxyLayerForwardingStateMachine`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIWindowLevelObserver`, `_UISceneKeyboardProxyLayerForwardingPresentationEnvironmentObserver`, `_UISceneKeyboardProxyLayerForwardingHostingEnvironmentObserver`
- 7 instance variables, 4 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<_UISceneKeyboardProxyLayerForwardingPresentationEnvironment>" _presentationEnvironment;
@"<_UISceneKeyboardProxyLayerForwardingHostingEnvironment>" _hostingEnvironment;
Q _state;
@ _windowDidMoveToSceneNotificationToken;
@"UIWindow" _hostingWindow;
@"NSSet" _keyboardLayersTracked;
@"NSSet" _keyboardLayersAddedToHostingEnvironment;
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
-[_UISceneKeyboardProxyLayerForwardingStateMachine _state];
-[_UISceneKeyboardProxyLayerForwardingStateMachine debugDescription];
-[_UISceneKeyboardProxyLayerForwardingStateMachine _setState:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine succinctDescriptionBuilder];
-[_UISceneKeyboardProxyLayerForwardingStateMachine _removeLayers:fromEnvironment:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine window:changedFromLevel:toLevel:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine dealloc];
-[_UISceneKeyboardProxyLayerForwardingStateMachine descriptionWithMultilinePrefix:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine hostingEnvironmentForWindow:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine succinctDescription];
-[_UISceneKeyboardProxyLayerForwardingStateMachine presentationEnvironmentDidUpdateKeyboardLayers:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine noteKeyboardLayersBeingTracked:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine hostingEnvironmentDidInvalidate:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine _newProxyLayers];
-[_UISceneKeyboardProxyLayerForwardingStateMachine _addLayers:toEnvironment:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine description];
-[_UISceneKeyboardProxyLayerForwardingStateMachine presentationEnvironmentDidInvalidate:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine presentationEnvironment:didMoveToWindow:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine _noteHostedInWindow:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine initWithPresentationEnvironment:];
-[_UISceneKeyboardProxyLayerForwardingStateMachine descriptionBuilderWithMultilinePrefix:];
```
