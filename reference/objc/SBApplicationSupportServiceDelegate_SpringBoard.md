# `SBApplicationSupportServiceDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISApplicationSupportServiceDelegate`
- 1 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UISApplicationSupportService" _service;
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
-[SBApplicationSupportServiceDelegate init];
-[SBApplicationSupportServiceDelegate dealloc];
-[SBApplicationSupportServiceDelegate destroyScenesWithPersistentIdentifiers:animationType:destroySessions:forClient:completion:];
-[SBApplicationSupportServiceDelegate requestPasscodeUnlockUIForClient:withCompletion:];
-[SBApplicationSupportServiceDelegate service:initializeClient:withCompletion:];
-[SBApplicationSupportServiceDelegate service:overrideClientInitialization:];
-[SBApplicationSupportServiceDelegate _rebuildDefaultContext];
-[SBApplicationSupportServiceDelegate requestPasscodeCheckUIForClient:withCompletion:];
```
