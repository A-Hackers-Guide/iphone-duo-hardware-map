# `UIInputViewControllerInterface`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TIKeyboardInputManagerStub`
- Protocols: `_UIIVCInterface`
- 3 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<_UIIVCResponseDelegate>" _responseDelegate;
@"<_UIIVCInterface>" _forwardingInterface;
@"_UIInputViewControllerState" _cachedState;
```

## Properties

```
@property (T@"_UIInputViewControllerState",&,N,G_cachedState,S_setCachedState:,V_cachedState) cachedState;
@property (T@"<_UIIVCInterface>",&,N,V_forwardingInterface) forwardingInterface;
@property (T@"<_UIIVCResponseDelegate>",&,N,V_responseDelegate) responseDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIInputViewControllerInterface init];
-[UIInputViewControllerInterface _cachedState];
-[UIInputViewControllerInterface dealloc];
-[UIInputViewControllerInterface forwardingInterface];
-[UIInputViewControllerInterface setForwardingInterface:];
-[UIInputViewControllerInterface responseDelegate];
-[UIInputViewControllerInterface _tearDownRemoteService];
-[UIInputViewControllerInterface _setCachedState:];
-[UIInputViewControllerInterface syncToKeyboardState:completionHandler:];
-[UIInputViewControllerInterface setResponseDelegate:];
-[UIInputViewControllerInterface _handleInputViewControllerState:];
```
