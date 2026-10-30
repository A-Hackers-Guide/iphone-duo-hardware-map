# `UIDraggingSystemSessionInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 6 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _supportsSystemDrag;
I _sessionIdentifier;
i _processIdentifier;
@"NSString" _persistentSceneIdentifier;
{?="val"[8I]} _auditToken;
```

## Properties

```
@property (TI,N,V_sessionIdentifier) sessionIdentifier;
@property (Ti,N,V_processIdentifier) processIdentifier;
@property (T{?=[8I]},N,V_auditToken) auditToken;
@property (TB,N,V_supportsSystemDrag) supportsSystemDrag;
@property (T@"NSString",C,N,V_persistentSceneIdentifier) persistentSceneIdentifier;
@property (T@"NSString",C,N) sceneIdentifier;
```

## Class methods

```
+[UIDraggingSystemSessionInfo supportsSecureCoding];
```

## Instance methods

```
-[UIDraggingSystemSessionInfo sessionIdentifier];
-[UIDraggingSystemSessionInfo setProcessIdentifier:];
-[UIDraggingSystemSessionInfo setSessionIdentifier:];
-[UIDraggingSystemSessionInfo setSceneIdentifier:];
-[UIDraggingSystemSessionInfo sceneIdentifier];
-[UIDraggingSystemSessionInfo setAuditToken:];
-[UIDraggingSystemSessionInfo encodeWithCoder:];
-[UIDraggingSystemSessionInfo hash];
-[UIDraggingSystemSessionInfo description];
-[UIDraggingSystemSessionInfo initWithCoder:];
-[UIDraggingSystemSessionInfo auditToken];
-[UIDraggingSystemSessionInfo processIdentifier];
-[UIDraggingSystemSessionInfo copyWithZone:];
-[UIDraggingSystemSessionInfo isEqual:];
-[UIDraggingSystemSessionInfo persistentSceneIdentifier];
-[UIDraggingSystemSessionInfo setPersistentSceneIdentifier:];
-[UIDraggingSystemSessionInfo setSupportsSystemDrag:];
-[UIDraggingSystemSessionInfo supportsSystemDrag];
```
