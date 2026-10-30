# `LACRemoteUIParams`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 13 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"LACUserInterfaceRequest" _uiRequest;
@"NSString" _identifier;
@"<LACUIMechanism><LACRemoteUIHost>" _uiMechanism;
q _hostedRemoteController;
@"<LACEvaluationRequest>" _evaluationRequest;
@"<LACAuthenticationUINotifying>" _notificationCenter;
@"<LACRemoteUI>" _remoteUI;
```

## Properties

```
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"<LACUIMechanism><LACRemoteUIHost>",R,N,V_uiMechanism) uiMechanism;
@property (Tq,R,N,V_hostedRemoteController) hostedRemoteController;
@property (T@"NSData",R,N) auditTokenData;
@property (TB,R,N) lsApplicationIdentity;
@property (TB,R,N) forSoftwareUpdate;
@property (TB,R,N) forSiri;
@property (Ti,R,N) pid;
@property (T@"NSNumber",R,N) userId;
@property (TI,R,N) requestID;
@property (T@"<LACEvaluationRequest>",R,N,V_evaluationRequest) evaluationRequest;
@property (T@"<LACAuthenticationUINotifying>",&,N,V_notificationCenter) notificationCenter;
@property (T@"<LACRemoteUI>",&,N,V_remoteUI) remoteUI;
```

## Instance methods

```
-[LACRemoteUIParams auditTokenData];
-[LACRemoteUIParams notificationCenter];
-[LACRemoteUIParams setNotificationCenter:];
-[LACRemoteUIParams requestID];
-[LACRemoteUIParams identifier];
-[LACRemoteUIParams pid];
-[LACRemoteUIParams description];
-[LACRemoteUIParams userId];
-[LACRemoteUIParams forSiri];
-[LACRemoteUIParams evaluationRequest];
-[LACRemoteUIParams forSoftwareUpdate];
-[LACRemoteUIParams hostedRemoteController];
-[LACRemoteUIParams initWithMechanism:];
-[LACRemoteUIParams initWithMechanism:hostedRemoteController:];
-[LACRemoteUIParams lsApplicationIdentity];
-[LACRemoteUIParams remoteUI];
-[LACRemoteUIParams setRemoteUI:];
-[LACRemoteUIParams uiMechanism];
```
