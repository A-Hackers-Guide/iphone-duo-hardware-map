# `KCJoiningAcceptSession`

- Image: [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](../userland/System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 19 properties, 55 instance methods, 2 class methods

## Instance variables

```
B _failSOSForTests;
i _state;
i _piggy_version;
Q _dsid;
@"<KCJoiningAcceptSecretDelegate>" _secretDelegate;
@"<KCJoiningAcceptCircleDelegate>" _circleDelegate;
@"KCSRPServerContext" _context;
@"KCAESGCMDuplexSession" _session;
@"NSData" _startMessage;
@"NSString" _piggy_uuid;
@"NSData" _octagon;
@"OTJoiningConfiguration" _joiningConfiguration;
@"OTControlArguments" _controlArguments;
@"OTControl" _otControl;
@"NSMutableDictionary" _defaults;
@"NSString" _altDSID;
@"NSString" _flowID;
@"NSString" _deviceSessionID;
Q _piggybacking_version_for_tests;
```

## Properties

```
@property (TQ,R,V_dsid) dsid;
@property (T@"<KCJoiningAcceptSecretDelegate>",W,V_secretDelegate) secretDelegate;
@property (T@"<KCJoiningAcceptCircleDelegate>",W,V_circleDelegate) circleDelegate;
@property (T@"KCSRPServerContext",R,V_context) context;
@property (T@"KCAESGCMDuplexSession",R,V_session) session;
@property (Ti,R,V_state) state;
@property (T@"NSData",&,V_startMessage) startMessage;
@property (T@"NSString",&,V_piggy_uuid) piggy_uuid;
@property (Ti,V_piggy_version) piggy_version;
@property (T@"NSData",&,V_octagon) octagon;
@property (T@"OTJoiningConfiguration",&,N,V_joiningConfiguration) joiningConfiguration;
@property (T@"OTControlArguments",&,N,V_controlArguments) controlArguments;
@property (T@"OTControl",&,N,V_otControl) otControl;
@property (T@"NSMutableDictionary",&,N,V_defaults) defaults;
@property (T@"NSString",&,N,V_altDSID) altDSID;
@property (T@"NSString",&,N,V_flowID) flowID;
@property (T@"NSString",&,N,V_deviceSessionID) deviceSessionID;
@property (TQ,N,V_piggybacking_version_for_tests) piggybacking_version_for_tests;
@property (TB,N,V_failSOSForTests) failSOSForTests;
```

## Class methods

```
+[KCJoiningAcceptSession sessionWithInitialMessage:secretDelegate:circleDelegate:dsid:altDSID:flowID:deviceSessionID:error:];
+[KCJoiningAcceptSession sessionWithInitialMessage:secretDelegate:circleDelegate:dsid:error:];
```

## Instance methods

```
-[KCJoiningAcceptSession setDefaults:];
-[KCJoiningAcceptSession dsid];
-[KCJoiningAcceptSession defaults];
-[KCJoiningAcceptSession setAltDSID:];
-[KCJoiningAcceptSession altDSID];
-[KCJoiningAcceptSession flowID];
-[KCJoiningAcceptSession setConfiguration:];
-[KCJoiningAcceptSession description];
-[KCJoiningAcceptSession setDeviceSessionID:];
-[KCJoiningAcceptSession session];
-[KCJoiningAcceptSession stateString];
-[KCJoiningAcceptSession isDone];
-[KCJoiningAcceptSession context];
-[KCJoiningAcceptSession deviceSessionID];
-[KCJoiningAcceptSession setFlowID:];
-[KCJoiningAcceptSession state];
-[KCJoiningAcceptSession otControl];
-[KCJoiningAcceptSession setOtControl:];
-[KCJoiningAcceptSession octagon];
-[KCJoiningAcceptSession failSOSForTests];
-[KCJoiningAcceptSession accessSession];
-[KCJoiningAcceptSession circleDelegate];
-[KCJoiningAcceptSession controlArguments];
-[KCJoiningAcceptSession copyChallengeMessage:];
-[KCJoiningAcceptSession createPairingMessageFromJoiningMessage:error:];
-[KCJoiningAcceptSession createTLKRequestResponse:];
-[KCJoiningAcceptSession initWithSecretDelegate:circleDelegate:dsid:altDSID:flowID:deviceSessionID:rng:error:];
-[KCJoiningAcceptSession joiningConfiguration];
-[KCJoiningAcceptSession piggy_uuid];
-[KCJoiningAcceptSession piggy_version];
-[KCJoiningAcceptSession piggybacking_version_for_tests];
-[KCJoiningAcceptSession processApplication:error:];
-[KCJoiningAcceptSession processInitialMessage:error:];
-[KCJoiningAcceptSession processMessage:error:];
-[KCJoiningAcceptSession processResponse:error:];
-[KCJoiningAcceptSession processSOSApplication:error:];
-[KCJoiningAcceptSession secretDelegate];
-[KCJoiningAcceptSession setCircleDelegate:];
-[KCJoiningAcceptSession setControlArguments:];
-[KCJoiningAcceptSession setControlObject:];
-[KCJoiningAcceptSession setFailSOSForTests:];
-[KCJoiningAcceptSession setFailSOSPropertyForTests:];
-[KCJoiningAcceptSession setJoiningConfiguration:];
-[KCJoiningAcceptSession setOctagon:];
-[KCJoiningAcceptSession setPiggy_uuid:];
-[KCJoiningAcceptSession setPiggy_version:];
-[KCJoiningAcceptSession setPiggybackingVersion:];
-[KCJoiningAcceptSession setPiggybacking_version_for_tests:];
-[KCJoiningAcceptSession setSecretDelegate:];
-[KCJoiningAcceptSession setSessionControlArguments:];
-[KCJoiningAcceptSession setStartMessage:];
-[KCJoiningAcceptSession setupSession:];
-[KCJoiningAcceptSession shouldAcceptOctagonRequests];
-[KCJoiningAcceptSession shouldProcessSOSApplication:pairingMessage:];
-[KCJoiningAcceptSession startMessage];
```
