# `UITextServicesInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextInteraction`
- Protocols: `_UITextServicesResponderProxyDelegate`
- 6 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"_UITextServiceSession" _definitionSession;
@"_UITextServiceSession" _learnSession;
@"_UITextServiceSession" _shareSession;
@"_UITextServiceSession" _lookupSession;
@"_UITextServiceSession" _translateSession;
@"_UITextServicesResponderProxy" _responderProxy;
```

## Properties

```
@property (T@"_UITextServicesResponderProxy",&,N,V_responderProxy) responderProxy;
@property (T@"UIResponder",R,N) responder;
```

## Instance methods

```
-[UITextServicesInteraction _share:];
-[UITextServicesInteraction _define:];
-[UITextServicesInteraction finishSetup];
-[UITextServicesInteraction _removeShortcutController];
-[UITextServicesInteraction responderProxy];
-[UITextServicesInteraction setResponderProxy:];
-[UITextServicesInteraction _removeShareController];
-[UITextServicesInteraction _addShortcut:];
-[UITextServicesInteraction _translate:];
-[UITextServicesInteraction responder];
-[UITextServicesInteraction _beginSessionWithType:sender:];
-[UITextServicesInteraction canPerformAction:withSender:];
```
