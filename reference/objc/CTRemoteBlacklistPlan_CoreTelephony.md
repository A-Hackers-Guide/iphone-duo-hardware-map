# `CTRemoteBlacklistPlan`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTPlan`
- 6 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _key;
@"NSString" _blacklistIMEI;
@"NSString" _blacklistEID;
@"NSString" _blacklistICCID;
@"NSString" _uploaderIMEI;
@"NSString" _uploaderEID;
```

## Properties

```
@property (T@"NSString",R,N,V_key) key;
@property (T@"NSString",R,N,V_blacklistIMEI) blacklistIMEI;
@property (T@"NSString",R,N,V_blacklistEID) blacklistEID;
@property (T@"NSString",R,N,V_blacklistICCID) blacklistICCID;
@property (T@"NSString",R,N,V_uploaderIMEI) uploaderIMEI;
@property (T@"NSString",R,N,V_uploaderEID) uploaderEID;
```

## Class methods

```
+[CTRemoteBlacklistPlan supportsSecureCoding];
```

## Instance methods

```
-[CTRemoteBlacklistPlan encodeWithCoder:];
-[CTRemoteBlacklistPlan description];
-[CTRemoteBlacklistPlan initWithCoder:];
-[CTRemoteBlacklistPlan isEqual:];
-[CTRemoteBlacklistPlan key];
-[CTRemoteBlacklistPlan blacklistEID];
-[CTRemoteBlacklistPlan blacklistICCID];
-[CTRemoteBlacklistPlan blacklistIMEI];
-[CTRemoteBlacklistPlan initWithkey:blacklistIMEI:blacklistEID:blacklistICCID:uploaderIMEI:uploaderEID:];
-[CTRemoteBlacklistPlan uploaderEID];
-[CTRemoteBlacklistPlan uploaderIMEI];
```
