# `OTConfigurationContext`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 21 properties, 46 instance methods, 0 class methods

## Instance variables

```
B _octagonCapableRecordsExist;
B _overrideForSetupAccountScript;
B _overrideForJoinAfterRestore;
B _isGuitarfish;
B _canSendMetrics;
B _testsEnabled;
i _pdpState;
@"NSString" _context;
@"NSString" _containerName;
@"NSString" _dsid;
@"NSString" _altDSID;
@"NSString" _authenticationAppleID;
@"NSString" _passwordEquivalentToken;
q _escrowFetchSource;
@"NSString" _flowID;
@"NSString" _deviceSessionID;
q _stableTrustedDeviceIDStatus;
@"OTControl" _otControl;
@"CKKSControl" _ckksControl;
@ _sbd;
```

## Properties

```
@property (T@"NSString",C,N,V_context) context;
@property (T@"NSString",C,N,V_containerName) containerName;
@property (T@"NSString",C,N,V_dsid) dsid;
@property (T@"NSString",C,N,V_altDSID) altDSID;
@property (T@"NSString",C,N,V_authenticationAppleID) authenticationAppleID;
@property (T@"NSString",C,N,V_passwordEquivalentToken) passwordEquivalentToken;
@property (TB,N) overrideEscrowCache;
@property (Tq,N,V_escrowFetchSource) escrowFetchSource;
@property (TB,N,V_octagonCapableRecordsExist) octagonCapableRecordsExist;
@property (TB,N,V_overrideForSetupAccountScript) overrideForSetupAccountScript;
@property (TB,N,V_overrideForJoinAfterRestore) overrideForJoinAfterRestore;
@property (TB,N,V_isGuitarfish) isGuitarfish;
@property (Ti,N,V_pdpState) pdpState;
@property (T@"NSString",C,N,V_flowID) flowID;
@property (T@"NSString",C,N,V_deviceSessionID) deviceSessionID;
@property (TB,N,V_canSendMetrics) canSendMetrics;
@property (Tq,N,V_stableTrustedDeviceIDStatus) stableTrustedDeviceIDStatus;
@property (T@"OTControl",&,V_otControl) otControl;
@property (T@"CKKSControl",&,V_ckksControl) ckksControl;
@property (T@,&,V_sbd) sbd;
@property (TB,N,V_testsEnabled) testsEnabled;
```

## Instance methods

```
-[OTConfigurationContext dsid];
-[OTConfigurationContext setPasswordEquivalentToken:];
-[OTConfigurationContext stableTrustedDeviceIDStatus];
-[OTConfigurationContext setDsid:];
-[OTConfigurationContext setAltDSID:];
-[OTConfigurationContext altDSID];
-[OTConfigurationContext passwordEquivalentToken];
-[OTConfigurationContext flowID];
-[OTConfigurationContext init];
-[OTConfigurationContext canSendMetrics];
-[OTConfigurationContext setCanSendMetrics:];
-[OTConfigurationContext setContext:];
-[OTConfigurationContext containerName];
-[OTConfigurationContext setStableTrustedDeviceIDStatus:];
-[OTConfigurationContext description];
-[OTConfigurationContext setDeviceSessionID:];
-[OTConfigurationContext context];
-[OTConfigurationContext deviceSessionID];
-[OTConfigurationContext setFlowID:];
-[OTConfigurationContext setContainerName:];
-[OTConfigurationContext sbd];
-[OTConfigurationContext setCkksControl:];
-[OTConfigurationContext setSbd:];
-[OTConfigurationContext setOverrideForJoinAfterRestore:];
-[OTConfigurationContext authenticationAppleID];
-[OTConfigurationContext ckksControl];
-[OTConfigurationContext escrowFetchSource];
-[OTConfigurationContext isGuitarfish];
-[OTConfigurationContext makeCKKSControl:];
-[OTConfigurationContext makeOTControl:];
-[OTConfigurationContext octagonCapableRecordsExist];
-[OTConfigurationContext otControl];
-[OTConfigurationContext overrideEscrowCache];
-[OTConfigurationContext overrideForJoinAfterRestore];
-[OTConfigurationContext overrideForSetupAccountScript];
-[OTConfigurationContext pdpState];
-[OTConfigurationContext setAuthenticationAppleID:];
-[OTConfigurationContext setEscrowFetchSource:];
-[OTConfigurationContext setIsGuitarfish:];
-[OTConfigurationContext setOctagonCapableRecordsExist:];
-[OTConfigurationContext setOtControl:];
-[OTConfigurationContext setOverrideEscrowCache:];
-[OTConfigurationContext setOverrideForSetupAccountScript:];
-[OTConfigurationContext setPdpState:];
-[OTConfigurationContext setTestsEnabled:];
-[OTConfigurationContext testsEnabled];
```
