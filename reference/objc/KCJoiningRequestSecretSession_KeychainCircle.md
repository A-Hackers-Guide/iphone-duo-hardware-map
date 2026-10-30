# `KCJoiningRequestSecretSession`

- Image: [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](../userland/System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 15 properties, 41 instance methods, 2 class methods

## Instance variables

```
i _state;
@"NSString" _altDSID;
@"KCAESGCMDuplexSession" _session;
@"<KCJoiningRequestSecretDelegate>" _secretDelegate;
@"KCSRPClientContext" _context;
Q _dsid;
@"NSString" _piggy_uuid;
Q _piggy_version;
Q _epoch;
@"NSData" _challenge;
@"NSData" _salt;
@"NSString" _sessionUUID;
@"NSString" _flowID;
@"NSString" _deviceSessionID;
@"NSMutableDictionary" _defaults;
```

## Properties

```
@property (T@"<KCJoiningRequestSecretDelegate>",W,V_secretDelegate) secretDelegate;
@property (T@"KCSRPClientContext",R,V_context) context;
@property (TQ,R,V_dsid) dsid;
@property (Ti,R,V_state) state;
@property (T@"NSString",&,V_piggy_uuid) piggy_uuid;
@property (TQ,V_piggy_version) piggy_version;
@property (TQ,V_epoch) epoch;
@property (T@"NSData",&,V_challenge) challenge;
@property (T@"NSData",&,V_salt) salt;
@property (T@"NSString",&,V_sessionUUID) sessionUUID;
@property (T@"NSString",&,V_flowID) flowID;
@property (T@"NSString",&,V_deviceSessionID) deviceSessionID;
@property (T@"NSMutableDictionary",&,N,V_defaults) defaults;
@property (T@"KCAESGCMDuplexSession",R,V_session) session;
@property (T@"NSString",&,V_altDSID) altDSID;
```

## Class methods

```
+[KCJoiningRequestSecretSession sessionWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:error:];
+[KCJoiningRequestSecretSession sessionWithSecretDelegate:dsid:error:];
```

## Instance methods

```
-[KCJoiningRequestSecretSession setDefaults:];
-[KCJoiningRequestSecretSession dsid];
-[KCJoiningRequestSecretSession epoch];
-[KCJoiningRequestSecretSession defaults];
-[KCJoiningRequestSecretSession salt];
-[KCJoiningRequestSecretSession setSalt:];
-[KCJoiningRequestSecretSession setAltDSID:];
-[KCJoiningRequestSecretSession altDSID];
-[KCJoiningRequestSecretSession sessionUUID];
-[KCJoiningRequestSecretSession flowID];
-[KCJoiningRequestSecretSession setSessionUUID:];
-[KCJoiningRequestSecretSession setEpoch:];
-[KCJoiningRequestSecretSession description];
-[KCJoiningRequestSecretSession setDeviceSessionID:];
-[KCJoiningRequestSecretSession session];
-[KCJoiningRequestSecretSession stateString];
-[KCJoiningRequestSecretSession isDone];
-[KCJoiningRequestSecretSession context];
-[KCJoiningRequestSecretSession deviceSessionID];
-[KCJoiningRequestSecretSession setFlowID:];
-[KCJoiningRequestSecretSession state];
-[KCJoiningRequestSecretSession challenge];
-[KCJoiningRequestSecretSession setChallenge:];
-[KCJoiningRequestSecretSession initialMessage:];
-[KCJoiningRequestSecretSession copyResponseForChallenge:salt:secret:error:];
-[KCJoiningRequestSecretSession copyResponseForSecret:error:];
-[KCJoiningRequestSecretSession createUUID];
-[KCJoiningRequestSecretSession handleChallenge:error:];
-[KCJoiningRequestSecretSession handleChallenge:secret:error:];
-[KCJoiningRequestSecretSession handleChallengeData:secret:error:];
-[KCJoiningRequestSecretSession handleVerification:error:];
-[KCJoiningRequestSecretSession initWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:error:];
-[KCJoiningRequestSecretSession initWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:rng:error:];
-[KCJoiningRequestSecretSession piggy_uuid];
-[KCJoiningRequestSecretSession piggy_version];
-[KCJoiningRequestSecretSession processMessage:error:];
-[KCJoiningRequestSecretSession secretDelegate];
-[KCJoiningRequestSecretSession setPiggy_uuid:];
-[KCJoiningRequestSecretSession setPiggy_version:];
-[KCJoiningRequestSecretSession setSecretDelegate:];
-[KCJoiningRequestSecretSession setupSession:];
```
