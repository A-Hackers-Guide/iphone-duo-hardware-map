# `CWFXPCConnectionMessageProxy`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSProxy`
- 2 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"CWFXPCConnection" _target;
@"NSMutableSet" _methodSignatures;
```

## Class methods

```
+[CWFXPCConnectionMessageProxy respondsToSelector:];
```

## Instance methods

```
-[CWFXPCConnectionMessageProxy initWithXPCConnection:];
-[CWFXPCConnectionMessageProxy methodSignatureForSelector:];
-[CWFXPCConnectionMessageProxy forwardInvocation:];
-[CWFXPCConnectionMessageProxy __addMethodSignature:];
-[CWFXPCConnectionMessageProxy __hasMethodSignature:];
```
