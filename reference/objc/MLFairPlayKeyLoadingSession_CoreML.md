# `MLFairPlayKeyLoadingSession`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
I _sessionID;
@"NSString" _keyIdentifier;
^{?=III{?=II[136C]I[4096C][128C]}{?=[16C][16C][16C][128C]}} _sessionContext;
```

## Properties

```
@property (T@"NSString",C,V_keyIdentifier) keyIdentifier;
@property (TI,V_sessionID) sessionID;
@property (T^{?=III{?=II[136C]I[4096C][128C]}{?=[16C][16C][16C][128C]}},V_sessionContext) sessionContext;
```

## Instance methods

```
-[MLFairPlayKeyLoadingSession sessionID];
-[MLFairPlayKeyLoadingSession setSessionID:];
-[MLFairPlayKeyLoadingSession init];
-[MLFairPlayKeyLoadingSession dealloc];
-[MLFairPlayKeyLoadingSession setSessionContext:];
-[MLFairPlayKeyLoadingSession sessionContext];
-[MLFairPlayKeyLoadingSession keyIdentifier];
-[MLFairPlayKeyLoadingSession setKeyIdentifier:];
-[MLFairPlayKeyLoadingSession generateKeyRequestForKeyIdentifier:teamIdentifier:error:];
-[MLFairPlayKeyLoadingSession generatePersistentKeyBlobFromKeyResponse:error:];
-[MLFairPlayKeyLoadingSession transformKeyIdentifier:error:];
```
