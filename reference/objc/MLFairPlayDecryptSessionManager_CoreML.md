# `MLFairPlayDecryptSessionManager`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _modelPathToSessionID;
^{?=III{?=II[136C]I[4096C][128C]}{?=[16C][16C][16C][128C]}} _sessionContext;
@"NSObject<OS_dispatch_queue>" _syncQueue;
```

## Properties

```
@property (T@"NSMutableDictionary",R,&,V_modelPathToSessionID) modelPathToSessionID;
@property (T^{?=III{?=II[136C]I[4096C][128C]}{?=[16C][16C][16C][128C]}},R,V_sessionContext) sessionContext;
@property (T@"NSObject<OS_dispatch_queue>",R,&,V_syncQueue) syncQueue;
```

## Instance methods

```
-[MLFairPlayDecryptSessionManager syncQueue];
-[MLFairPlayDecryptSessionManager init];
-[MLFairPlayDecryptSessionManager dealloc];
-[MLFairPlayDecryptSessionManager sessionContext];
-[MLFairPlayDecryptSessionManager startDecryptionOfModelAtPath:usingKeyBlob:teamIdentifier:error:];
-[MLFairPlayDecryptSessionManager modelPathToSessionID];
-[MLFairPlayDecryptSessionManager stopDecryptionOfModelAtPath:];
-[MLFairPlayDecryptSessionManager stopDecryptionOfModelAtPath:error:];
```
