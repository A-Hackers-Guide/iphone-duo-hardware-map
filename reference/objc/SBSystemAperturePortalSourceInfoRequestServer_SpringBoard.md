# `SBSystemAperturePortalSourceInfoRequestServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSSystemAperturePortalSourceInfoRequestClientToServerInterface`, `BSServiceConnectionListenerDelegate`
- 3 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnectionListener" _connectionListener;
@"SBSPortalSource" _rootSystemApertureWindowPortalSource;
@"FBServiceClientAuthenticator" _serviceClientAuthenticator;
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
-[SBSystemAperturePortalSourceInfoRequestServer listener:didReceiveConnection:withContext:];
-[SBSystemAperturePortalSourceInfoRequestServer dealloc];
-[SBSystemAperturePortalSourceInfoRequestServer startListener];
-[SBSystemAperturePortalSourceInfoRequestServer rootWindowPortalSourceWithCompletion:];
-[SBSystemAperturePortalSourceInfoRequestServer initWithPortalSource:];
```
