# `_UISystemAuthenticationServiceMessage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
S _secureNamespace;
@"BKSHIDEventAuthenticationMessage" _authenticationMessage;
```

## Properties

```
@property (T@"BKSHIDEventAuthenticationMessage",R,N,V_authenticationMessage) authenticationMessage;
@property (TS,R,N,V_secureNamespace) secureNamespace;
@property (T@"BKSHIDEventAuthenticationMessage",R,N) pasteAuthenticationMessage;
@property (T@"BKSHIDEventAuthenticationMessage",R,N) dictationAuthenticationMessage;
```

## Class methods

```
+[_UISystemAuthenticationServiceMessage supportsSecureCoding];
```

## Instance methods

```
-[_UISystemAuthenticationServiceMessage authenticationMessage];
-[_UISystemAuthenticationServiceMessage encodeWithCoder:];
-[_UISystemAuthenticationServiceMessage initWithCoder:];
-[_UISystemAuthenticationServiceMessage secureNamespace];
-[_UISystemAuthenticationServiceMessage dictationAuthenticationMessage];
-[_UISystemAuthenticationServiceMessage initWithAuthenticationMessage:secureNamespace:];
-[_UISystemAuthenticationServiceMessage pasteAuthenticationMessage];
```
