# `BiometricKit`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BiometricKitXPCClientDelegate`, `BiometricKitDelegateXpcProtocol`
- 14 instance variables, 7 properties, 103 instance methods, 3 class methods

## Instance variables

```
@"BiometricKitXPCClient" _xpcClient;
i _enrollingMode;
i _matchingMode;
[300@"NSDictionary"] _images;
{?="count"i"capa"i"items"^^{?}"unusedImageCount"i"componentCount"i"componentCapa"i"bestComponentIndex"i"bestMapiComponentIndex"i"components"^^{?}"mapiNodeAddedIndex"s"mapiNodeRemovedIndex"s"updateCount"i"structureIsInconsistent"B} _compSet;
B _showDebugImages;
{?="nodes"[300{?="imageData"@"NSData""width"I"height"I}]} _enrollImageSet;
B _isInternalInstall;
B _ariadneSignposts;
@"NSObject<OS_os_log>" _osLog;
@"NSObject<OS_os_log>" _osLogTrace;
B _inUse;
i _enrollProgressConfigRenderMode;
@"<BiometricKitDelegate>" _delegate;
```

## Properties

```
@property (T@"<BiometricKitDelegate>",N,V_delegate) delegate;
@property (TB,V_inUse) inUse;
@property (Ti,N,V_enrollProgressConfigRenderMode) enrollProgressConfigRenderMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BiometricKit allocWithZone:];
+[BiometricKit manager];
+[BiometricKit getSensorPatchVersion];
```

## Instance methods

```
-[BiometricKit isDelegate];
-[BiometricKit statusMessage:client:];
-[BiometricKit appWillResignActive:];
-[BiometricKit setProtectedConfiguration:withAuthToken:];
-[BiometricKit getSensorCalibrationStatus];
-[BiometricKit setInUse:];
-[BiometricKit _statusMessage:];
-[BiometricKit isTouchIDCapable];
-[BiometricKit homeButtonPressed:];
-[BiometricKit connectionInterrupted];
-[BiometricKit statusMessage:details:client:];
-[BiometricKit removeIdentity:];
-[BiometricKit getModulationRatio];
-[BiometricKit removeIdentity:withOptions:withReply:];
-[BiometricKit pullDebugImageData:rotated:target:];
-[BiometricKit getSensorInfo];
-[BiometricKit init];
-[BiometricKit getProtectedConfigurationForUser:];
-[BiometricKit setSystemProtectedConfiguration:withOptions:withReply:];
-[BiometricKit getProvisioningState];
-[BiometricKit setUserDSID:withAuthToken:];
-[BiometricKit registerStoreToken:];
-[BiometricKit enrollUpdate:client:];
-[BiometricKit dealloc];
-[BiometricKit dropUnlockToken];
-[BiometricKit getIdentitiesDatabaseHashForUser:];
-[BiometricKit getMaxIdentityCount:];
-[BiometricKit isTouchIDAvailableWithInfo:];
-[BiometricKit getCalibrationDataState];
-[BiometricKit getIdentitiesDatabaseUUID];
-[BiometricKit pullCaptureBuffer];
-[BiometricKit setSystemProtectedConfiguration:withOptions:];
-[BiometricKit fileRadarWithLogs:withDescription:];
-[BiometricKit _homeButtonPressed];
-[BiometricKit getProtectedConfiguration];
-[BiometricKit getSystemProtectedConfiguration];
-[BiometricKit match:];
-[BiometricKit enrollResult:details:client:];
-[BiometricKit updateIdentity:withOptions:];
-[BiometricKit identities:];
-[BiometricKit resetAppleConnectCounter];
-[BiometricKit setProtectedConfiguration:forUser:withOptions:];
-[BiometricKit setDelegate:];
-[BiometricKit registerDSID:withAuthToken:];
-[BiometricKit enroll:withOptions:];
-[BiometricKit _templateUpdate:withDictionary:];
-[BiometricKit diagnostics:withOptions:passed:withDetails:];
-[BiometricKit templateUpdate:details:client:];
-[BiometricKit enrollProgressMessage:];
-[BiometricKit _touchIDButtonPressed:];
-[BiometricKit registerDSID:withOptions:];
-[BiometricKit detectPresenceWithOptions:];
-[BiometricKit match:withOptions:];
-[BiometricKit setDebugImages:];
-[BiometricKit _taskResumeStatus:];
-[BiometricKit getCountersignedStoreToken:];
-[BiometricKit imageDictFromRawImageData:];
-[BiometricKit createMatchInfo:withTopology:withMatchImage:];
-[BiometricKit enroll:forUser:withOptions:];
-[BiometricKit getBioLockoutState];
-[BiometricKit taskResumeStatus:client:];
-[BiometricKit delegate];
-[BiometricKit getBioLockoutStateForUser:];
-[BiometricKit forceBioLockoutForUser:];
-[BiometricKit appDidEnterBackground:];
-[BiometricKit getFreeIdentityCount:forUser:];
-[BiometricKit setProtectedConfiguration:withOptions:withReply:];
-[BiometricKit setEnrollProgressConfigRenderMode:];
-[BiometricKit updateIdentity:withOptions:withReply:];
-[BiometricKit pullDebugImage:rotated:];
-[BiometricKit _enrollResult:];
-[BiometricKit setProtectedConfiguration:forUser:withOptions:withReply:];
-[BiometricKit appWillEnterForeground:];
-[BiometricKit inUse];
-[BiometricKit getIdentitiesDatabaseUUIDForUser:];
-[BiometricKit timestampEvent:];
-[BiometricKit getMatchPolicyInfo];
-[BiometricKit getIdentitiesDatabaseHash];
-[BiometricKit updateIdentity:];
-[BiometricKit getIdentityFromUUID:];
-[BiometricKit getCalibrationDataInfo];
-[BiometricKit touchIDButtonPressed:client:];
-[BiometricKit copyWithZone:];
-[BiometricKit isFingerOn];
-[BiometricKit _matchResult:withDictionary:];
-[BiometricKit cancel];
-[BiometricKit getCalBlobVersion];
-[BiometricKit detectFingerWithOptions:];
-[BiometricKit enrollFeedback:client:];
-[BiometricKit forceBioLockout];
-[BiometricKit setProtectedConfiguration:withOptions:];
-[BiometricKit getTemplateInfo:];
-[BiometricKit appDidBecomeActive:];
-[BiometricKit setUserDSID:withOptions:];
-[BiometricKit enrollProgressConfigRenderMode];
-[BiometricKit pullCalibrationData];
-[BiometricKit removeAllIdentitiesForUser:withOptions:];
-[BiometricKit logEventOrCode:];
-[BiometricKit getLogs:withDetails:];
-[BiometricKit removeIdentity:withOptions:];
-[BiometricKit enableBackgroundFdet:];
-[BiometricKit matchResult:details:client:];
-[BiometricKit removeAllIdentitiesForUser:withOptions:withReply:];
```
