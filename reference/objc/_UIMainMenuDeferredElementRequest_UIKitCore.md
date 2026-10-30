# `_UIMainMenuDeferredElementRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"_UIMainMenuSession" _providedSession;
@"_UIMainMenuSessionIdentifier" _sessionIdentifier;
@"_UIMainMenuDeferredElementIdentifier" _deferredElementIdentifier;
```

## Properties

```
@property (T@"_UIMainMenuSessionIdentifier",R,N,V_sessionIdentifier) _sessionIdentifier;
@property (T@"_UIMainMenuDeferredElementIdentifier",R,N,V_deferredElementIdentifier) deferredElementIdentifier;
@property (T@"_UIMainMenuSession",R,N) session;
```

## Class methods

```
+[_UIMainMenuDeferredElementRequest supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuDeferredElementRequest encodeWithCoder:];
-[_UIMainMenuDeferredElementRequest hash];
-[_UIMainMenuDeferredElementRequest description];
-[_UIMainMenuDeferredElementRequest initWithCoder:];
-[_UIMainMenuDeferredElementRequest session];
-[_UIMainMenuDeferredElementRequest isEqual:];
-[_UIMainMenuDeferredElementRequest _sessionIdentifier];
-[_UIMainMenuDeferredElementRequest deferredElementIdentifier];
-[_UIMainMenuDeferredElementRequest initWithDeferredElementIdentifier:session:];
```
