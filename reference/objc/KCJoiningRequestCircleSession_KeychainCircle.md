# `KCJoiningRequestCircleSession`

- Image: [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](../userland/System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 38 instance methods, 2 class methods

## Instance variables

```
B _failSOSForTests;
i _state;
@"NSObject<KCJoiningRequestCircleDelegate>" _circleDelegate;
@"KCAESGCMDuplexSession" _session;
Q _piggy_version;
@"NSString" _altDSID;
@"NSString" _flowID;
@"NSString" _deviceSessionID;
@"OTControl" _otControl;
@"OTJoiningConfiguration" _joiningConfiguration;
@"OTControlArguments" _controlArguments;
Q _piggybacking_version_for_tests;
```

## Properties

```
@property (T@"NSObject<KCJoiningRequestCircleDelegate>",R,V_circleDelegate) circleDelegate;
@property (T@"KCAESGCMDuplexSession",R,V_session) session;
@property (Ti,V_state) state;
@property (TQ,N,V_piggy_version) piggy_version;
@property (T@"NSString",&,N,V_altDSID) altDSID;
@property (T@"NSString",&,N,V_flowID) flowID;
@property (T@"NSString",&,N,V_deviceSessionID) deviceSessionID;
@property (T@"OTControl",&,N,V_otControl) otControl;
@property (T@"OTJoiningConfiguration",&,N,V_joiningConfiguration) joiningConfiguration;
@property (T@"OTControlArguments",&,N,V_controlArguments) controlArguments;
@property (TQ,N,V_piggybacking_version_for_tests) piggybacking_version_for_tests;
@property (TB,N,V_failSOSForTests) failSOSForTests;
```

## Class methods

```
+[KCJoiningRequestCircleSession sessionWithCircleDelegate:session:altDSID:flowID:deviceSessionID:error:];
+[KCJoiningRequestCircleSession sessionWithCircleDelegate:session:error:];
```

## Instance methods

```
-[KCJoiningRequestCircleSession setState:];
-[KCJoiningRequestCircleSession setAltDSID:];
-[KCJoiningRequestCircleSession altDSID];
-[KCJoiningRequestCircleSession flowID];
-[KCJoiningRequestCircleSession setDeviceSessionID:];
-[KCJoiningRequestCircleSession session];
-[KCJoiningRequestCircleSession isDone];
-[KCJoiningRequestCircleSession deviceSessionID];
-[KCJoiningRequestCircleSession setFlowID:];
-[KCJoiningRequestCircleSession state];
-[KCJoiningRequestCircleSession otControl];
-[KCJoiningRequestCircleSession setOtControl:];
-[KCJoiningRequestCircleSession failSOSForTests];
-[KCJoiningRequestCircleSession initialMessage:];
-[KCJoiningRequestCircleSession accessSession];
-[KCJoiningRequestCircleSession circleDelegate];
-[KCJoiningRequestCircleSession controlArguments];
-[KCJoiningRequestCircleSession encryptPeerInfo:];
-[KCJoiningRequestCircleSession encryptedInitialMessage:error:];
-[KCJoiningRequestCircleSession encryptedPeerInfo:];
-[KCJoiningRequestCircleSession handleCircleBlob:error:];
-[KCJoiningRequestCircleSession initWithCircleDelegate:session:altDSID:flowID:deviceSessionID:error:];
-[KCJoiningRequestCircleSession initWithCircleDelegate:session:otcontrol:altDSID:flowID:deviceSessionID:error:];
-[KCJoiningRequestCircleSession joiningConfiguration];
-[KCJoiningRequestCircleSession piggy_version];
-[KCJoiningRequestCircleSession piggybacking_version_for_tests];
-[KCJoiningRequestCircleSession processMessage:error:];
-[KCJoiningRequestCircleSession setContextIDForSession:];
-[KCJoiningRequestCircleSession setControlArguments:];
-[KCJoiningRequestCircleSession setControlObject:];
-[KCJoiningRequestCircleSession setFailSOSForTests:];
-[KCJoiningRequestCircleSession setFailSOSPropertyForTests:];
-[KCJoiningRequestCircleSession setJoiningConfiguration:];
-[KCJoiningRequestCircleSession setPiggy_version:];
-[KCJoiningRequestCircleSession setPiggybackingVersion:];
-[KCJoiningRequestCircleSession setPiggybacking_version_for_tests:];
-[KCJoiningRequestCircleSession shouldJoinSOS:pairingMessage:];
-[KCJoiningRequestCircleSession waitForOctagonUpgrade];
```
