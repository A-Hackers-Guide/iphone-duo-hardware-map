# `BKSSystemShellControlService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSSystemShellControlClientInterface`
- 2 instance variables, 4 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"BSServiceConnection" _connection;
@"NSObject<OS_dispatch_queue>" _calloutQueue;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSSystemShellControlService sharedInstance];
```

## Instance methods

```
-[BKSSystemShellControlService _activateServerConnection];
-[BKSSystemShellControlService initWithCalloutQueue:];
-[BKSSystemShellControlService terminateSystemShellWithJobLabel:];
```
