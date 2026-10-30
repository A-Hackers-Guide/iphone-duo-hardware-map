# `BiometricKitXPCClient`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 3 properties, 84 instance methods, 2 class methods

## Instance variables

```
Q _clientID;
Q _connectionID;
q _clientType;
@"BiometricKitXPCClientConnection" _connection;
B _connectionInitialized;
B _connectionInvalidated;
B _connectionInterrupted;
@"<BiometricKitXPCClientDelegate><BiometricKitDelegateXpcProtocol>" _delegate;
```

## Properties

```
@property (T@"<BiometricKitXPCClientDelegate><BiometricKitDelegateXpcProtocol>",W,N,V_delegate) delegate;
@property (TQ,R,N) clientID;
@property (TQ,R,N) connectionId;
```

## Class methods

```
+[BiometricKitXPCClient initialize];
+[BiometricKitXPCClient clientUUID];
```

## Instance methods

```
-[BiometricKitXPCClient connect];
-[BiometricKitXPCClient getPreferencesValue:forKey:];
-[BiometricKitXPCClient forceBioLockoutForUser:withOptions:];
-[BiometricKitXPCClient enableMatchAutoRetry:];
-[BiometricKitXPCClient clientID];
-[BiometricKitXPCClient getSensorCalibrationStatus];
-[BiometricKitXPCClient prewarmCamera:];
-[BiometricKitXPCClient invalidateConnection];
-[BiometricKitXPCClient setSystemProtectedConfiguration:withOptions:async:withReply:];
-[BiometricKitXPCClient getSensorInfo];
-[BiometricKitXPCClient queryIdentityMigrationFailureForUser:failed:clear:];
-[BiometricKitXPCClient removeAllPreferences];
-[BiometricKitXPCClient init];
-[BiometricKitXPCClient getProtectedConfigurationForUser:];
-[BiometricKitXPCClient getProvisioningState];
-[BiometricKitXPCClient pullDebugImageData:rotated:imageWidth:imageHeight:];
-[BiometricKitXPCClient registerStoreToken:];
-[BiometricKitXPCClient pullMatchPolicyInfoData];
-[BiometricKitXPCClient dealloc];
-[BiometricKitXPCClient initializeConnection];
-[BiometricKitXPCClient dropUnlockToken];
-[BiometricKitXPCClient registerDelegateCall:];
-[BiometricKitXPCClient getIdentitiesDatabaseHashForUser:];
-[BiometricKitXPCClient setTemplate:forIdentity:];
-[BiometricKitXPCClient pauseFaceDetectTimer:];
-[BiometricKitXPCClient getExpressModeState:forUser:];
-[BiometricKitXPCClient getMaxIdentityCount:];
-[BiometricKitXPCClient connectionId];
-[BiometricKitXPCClient listAccessories:];
-[BiometricKitXPCClient pullCaptureBuffer];
-[BiometricKitXPCClient isXARTAvailable];
-[BiometricKitXPCClient getDeviceHardwareState:];
-[BiometricKitXPCClient fileRadarWithLogs:withDescription:];
-[BiometricKitXPCClient removePeriocularTemplatesWithOptions:async:withReply:];
-[BiometricKitXPCClient completeEnrollment];
-[BiometricKitXPCClient isPeriocularEnrollmentSupported:];
-[BiometricKitXPCClient getSystemProtectedConfiguration];
-[BiometricKitXPCClient getFreeIdentityCount:forUser:accessoryGroup:];
-[BiometricKitXPCClient startNewMatchAttempt];
-[BiometricKitXPCClient getBiometryAvailability:forUser:];
-[BiometricKitXPCClient identities:];
-[BiometricKitXPCClient isAriadneSignpostsEnabled];
-[BiometricKitXPCClient notifyAppIsBackground:];
-[BiometricKitXPCClient resetAppleConnectCounter];
-[BiometricKitXPCClient getPeriocularMatchState:state:];
-[BiometricKitXPCClient disconnect];
-[BiometricKitXPCClient timestampEvent:absoluteTime:];
-[BiometricKitXPCClient setDelegate:];
-[BiometricKitXPCClient getLastMatchEvent:];
-[BiometricKitXPCClient diagnostics:withOptions:passed:withDetails:];
-[BiometricKitXPCClient registerDSID:withOptions:];
-[BiometricKitXPCClient detectPresenceWithOptions:async:withReply:];
-[BiometricKitXPCClient match:withOptions:async:withReply:];
-[BiometricKitXPCClient setDebugImages:];
-[BiometricKitXPCClient getCountersignedStoreToken:];
-[BiometricKitXPCClient delegate];
-[BiometricKitXPCClient notifyAppIsInactive:];
-[BiometricKitXPCClient setProtectedConfiguration:forUser:withOptions:async:withReply:];
-[BiometricKitXPCClient getFreeIdentityCount:forUser:];
-[BiometricKitXPCClient pullAlignmentData];
-[BiometricKitXPCClient registerDelegate:];
-[BiometricKitXPCClient getDeviceState];
-[BiometricKitXPCClient getNodeTopologyForIdentity:];
-[BiometricKitXPCClient getIdentitiesDatabaseUUIDForUser:];
-[BiometricKitXPCClient setPreferencesValue:forKey:];
-[BiometricKitXPCClient getBioLockoutState:forUser:];
-[BiometricKitXPCClient suspendEnrollment:];
-[BiometricKitXPCClient getIdentityFromUUID:];
-[BiometricKitXPCClient getCalibrationDataInfo];
-[BiometricKitXPCClient isFingerOn];
-[BiometricKitXPCClient interruptConnection];
-[BiometricKitXPCClient initWithDeviceType:clientType:];
-[BiometricKitXPCClient cancel];
-[BiometricKitXPCClient enrollContinue];
-[BiometricKitXPCClient removeAllIdentitiesForUser:withOptions:async:withReply:];
-[BiometricKitXPCClient setUserDSID:withOptions:];
-[BiometricKitXPCClient pullCalibrationData];
-[BiometricKitXPCClient enroll:forUser:withOptions:async:withReply:];
-[BiometricKitXPCClient updateIdentity:withOptions:async:withReply:];
-[BiometricKitXPCClient logEventOrCode:];
-[BiometricKitXPCClient getDeviceProperties:];
-[BiometricKitXPCClient removeIdentity:withOptions:async:withReply:];
-[BiometricKitXPCClient getLogs:withDetails:];
-[BiometricKitXPCClient enableBackgroundFdet:];
```
