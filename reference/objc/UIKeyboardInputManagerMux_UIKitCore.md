# `UIKeyboardInputManagerMux`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 17 instance methods, 2 class methods

## Instance variables

```
@"NSMutableArray" _clients;
@"<_UIIVCResponseDelegateImpl>" _responseDelegate;
@"<TIKeyboardInputManager>" _systemInputManager;
```

## Properties

```
@property (T@"<TIKeyboardInputManager>",&,N,V_systemInputManager) systemInputManager;
@property (TB,R,N) hasSystemInputManager;
@property (T@"<_UIIVCResponseDelegateImpl>",&,N,V_responseDelegate) responseDelegate;
```

## Class methods

```
+[UIKeyboardInputManagerMux sharedInstance];
+[UIKeyboardInputManagerMux instancesRespondToSelector:];
```

## Instance methods

```
-[UIKeyboardInputManagerMux _systemHasKbd];
-[UIKeyboardInputManagerMux removeAllClients];
-[UIKeyboardInputManagerMux removeClient:];
-[UIKeyboardInputManagerMux hasSystemInputManager];
-[UIKeyboardInputManagerMux updateClientResponseDelegatesWithDelegate:];
-[UIKeyboardInputManagerMux addClient:];
-[UIKeyboardInputManagerMux responseDelegate];
-[UIKeyboardInputManagerMux releaseConnectedClients];
-[UIKeyboardInputManagerMux systemInputManager];
-[UIKeyboardInputManagerMux conformsToProtocol:];
-[UIKeyboardInputManagerMux methodSignatureForSelector:];
-[UIKeyboardInputManagerMux setResponseDelegate:];
-[UIKeyboardInputManagerMux isKindOfClass:];
-[UIKeyboardInputManagerMux respondsToSelector:];
-[UIKeyboardInputManagerMux setSystemInputManagerFromTextInputTraits:autofillMode:implProxy:];
-[UIKeyboardInputManagerMux forwardInvocation:];
-[UIKeyboardInputManagerMux setSystemInputManager:];
```
