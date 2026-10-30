# `TPDialPromptAlert`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPAlert`
- Protocols: `SBSRemoteAlertHandleObserver`
- 9 instance variables, 13 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _isFaceTimeRequest;
@"SBSRemoteAlertHandle" _remoteAlertHandle;
@? _dialAction;
@"NSString" _buttonTitle;
@"NSSet" _handles;
@"NSArray" _availableSenderIdentities;
@"NSMutableDictionary" _senderIdentitiesMapping;
@? _dialActionForDualSim;
@"BSProcessHandle" _processHandle;
```

## Properties

```
@property (T@"SBSRemoteAlertHandle",&,N,V_remoteAlertHandle) remoteAlertHandle;
@property (T@?,C,N,V_dialAction) dialAction;
@property (T@"NSString",R,C,N,V_buttonTitle) buttonTitle;
@property (T@"NSSet",R,C,N,V_handles) handles;
@property (T@"NSArray",&,N,V_availableSenderIdentities) availableSenderIdentities;
@property (T@"NSMutableDictionary",&,N,V_senderIdentitiesMapping) senderIdentitiesMapping;
@property (T@?,C,N,V_dialActionForDualSim) dialActionForDualSim;
@property (T@"BSProcessHandle",R,N,V_processHandle) processHandle;
@property (TB,N,V_isFaceTimeRequest) isFaceTimeRequest;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPDialPromptAlert remoteAlertHandleDidDeactivate:];
-[TPDialPromptAlert dealloc];
-[TPDialPromptAlert defaultButtonTitle];
-[TPDialPromptAlert invalidate];
-[TPDialPromptAlert title];
-[TPDialPromptAlert processHandle];
-[TPDialPromptAlert show];
-[TPDialPromptAlert handles];
-[TPDialPromptAlert remoteAlertHandle:didInvalidateWithError:];
-[TPDialPromptAlert remoteAlertHandleDidActivate:];
-[TPDialPromptAlert otherButtonTitle];
-[TPDialPromptAlert buttonTitle];
-[TPDialPromptAlert remoteAlertHandle];
-[TPDialPromptAlert setRemoteAlertHandle:];
-[TPDialPromptAlert initWithDialRequest:dialAction:];
-[TPDialPromptAlert initWithJoinRequest:dialAction:];
-[TPDialPromptAlert defaultResponse];
-[TPDialPromptAlert availableSenderIdentities];
-[TPDialPromptAlert defaultDualSimResponseWithIndex:];
-[TPDialPromptAlert dialAction];
-[TPDialPromptAlert dialActionForDualSim];
-[TPDialPromptAlert initWithButtonTitle:handles:isFaceTimeRequest:dialAction:];
-[TPDialPromptAlert initWithButtonTitleForDualSim:handles:isFaceTimeRequest:dialAction:];
-[TPDialPromptAlert initWithDialRequest:dialAction:availableSenderIdentities:];
-[TPDialPromptAlert isFaceTimeRequest];
-[TPDialPromptAlert otherDualSimResponse];
-[TPDialPromptAlert otherResponse];
-[TPDialPromptAlert phoneNumberHandle];
-[TPDialPromptAlert senderIdentitiesMapping];
-[TPDialPromptAlert setAvailableSenderIdentities:];
-[TPDialPromptAlert setDialAction:];
-[TPDialPromptAlert setDialActionForDualSim:];
-[TPDialPromptAlert setIsFaceTimeRequest:];
-[TPDialPromptAlert setSenderIdentitiesMapping:];
```
