# `UIRemoteInputViewControllerInterface`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSExtensionContext`
- Protocols: `_UIIVCResponseDelegate`
- 1 instance variables, 5 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"<_UIIVCResponseDelegate>" _responseDelegate;
```

## Properties

```
@property (T@"<_UIIVCResponseDelegate>",&,N,V_responseDelegate) responseDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIRemoteInputViewControllerInterface _extensionAuxiliaryHostProtocol];
+[UIRemoteInputViewControllerInterface _extensionAuxiliaryVendorProtocol];
```

## Instance methods

```
-[UIRemoteInputViewControllerInterface _openURL:completion:];
-[UIRemoteInputViewControllerInterface dealloc];
-[UIRemoteInputViewControllerInterface responseDelegate];
-[UIRemoteInputViewControllerInterface _tearDownRemoteService];
-[UIRemoteInputViewControllerInterface _performInputViewControllerOutput:];
-[UIRemoteInputViewControllerInterface setResponseDelegate:];
-[UIRemoteInputViewControllerInterface _handleInputViewControllerState:];
```
