# `BKDevice`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BiometricKitXPCClientDelegate`, `BiometricKitDelegateXpcProtocol`
- 5 instance variables, 7 properties, 64 instance methods, 5 class methods

## Instance variables

```
@"BiometricKitXPCClient" _xpcClient;
@"NSDictionary" _deviceProperties;
@"<BKDeviceDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _queue;
@"BKDeviceDescriptor" _descriptor;
```

## Properties

```
@property (T@"BKDeviceDescriptor",&,N,V_descriptor) descriptor;
@property (T@"<BKDeviceDelegate>",W,N,V_delegate) delegate;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKDevice deviceWithDescriptor:error:];
+[BKDevice biometryAvailabilityInfo:fromDeviceInfo:error:];
+[BKDevice deviceAvailableWithFailure:];
+[BKDevice extendedLockoutState:fromDeviceLockoutState:error:];
+[BKDevice lockoutState:fromDeviceLockoutState:error:];
```

## Instance methods

```
-[BKDevice isDelegate];
-[BKDevice setDescriptor:];
-[BKDevice statusMessage:client:];
-[BKDevice dispatchQueue];
-[BKDevice homeButtonPressed:];
-[BKDevice connectionInterrupted];
-[BKDevice statusMessage:details:client:];
-[BKDevice descriptor];
-[BKDevice enrollUpdate:client:];
-[BKDevice dealloc];
-[BKDevice queue];
-[BKDevice createMatchOperationWithError:];
-[BKDevice createPresenceDetectOperationWithError:];
-[BKDevice enrollResult:details:client:];
-[BKDevice setDelegate:];
-[BKDevice templateUpdate:details:client:];
-[BKDevice taskResumeStatus:client:];
-[BKDevice delegate];
-[BKDevice createEnrollOperationWithError:];
-[BKDevice touchIDButtonPressed:client:];
-[BKDevice enrollFeedback:client:];
-[BKDevice setQueue:];
-[BKDevice matchResult:details:client:];
-[BKDevice bioLockoutState:forUser:error:];
-[BKDevice forceBioLockoutForUser:error:];
-[BKDevice identitiesWithError:];
-[BKDevice protectedConfigurationForUser:error:];
-[BKDevice maxIdentityCountWithError:];
-[BKDevice removeIdentity:error:];
-[BKDevice updateIdentity:error:];
-[BKDevice extendedBioLockoutState:forUser:error:];
-[BKDevice identitiesForUser:error:];
-[BKDevice freeIdentityCountForUser:error:];
-[BKDevice expressModeState:forUser:error:];
-[BKDevice accessoriesWithError:];
-[BKDevice accessoryGroupsWithError:];
-[BKDevice biometryAvailability:forUser:error:];
-[BKDevice connectedAccessoriesWithError:];
-[BKDevice deviceHardwareState:error:];
-[BKDevice dropAllUnlockTokensWithError:];
-[BKDevice effectiveProtectedConfigurationForUser:error:];
-[BKDevice forceBioLockoutForAllUsersWithError:];
-[BKDevice forceBioLockoutIfLockedForUser:error:];
-[BKDevice freeIdentityCountForUser:accessoryGroup:error:];
-[BKDevice identitiesDatabaseHashForUser:error:];
-[BKDevice identitiesDatabaseUUIDForUser:error:];
-[BKDevice identitiesForUser:accessoryGroup:error:];
-[BKDevice identityForUUID:error:];
-[BKDevice lastMatchEventWithError:];
-[BKDevice removeAllIdentitiesForUser:async:reply:];
-[BKDevice removeAllIdentitiesForUser:error:];
-[BKDevice removeAllIdentitiesForUser:reply:];
-[BKDevice removeIdentity:async:reply:];
-[BKDevice removeIdentity:reply:];
-[BKDevice setProtectedConfiguration:forUser:credentialSet:async:reply:];
-[BKDevice setProtectedConfiguration:forUser:credentialSet:error:];
-[BKDevice setProtectedConfiguration:forUser:credentialSet:reply:];
-[BKDevice setSystemProtectedConfiguration:credentialSet:async:reply:];
-[BKDevice setSystemProtectedConfiguration:credentialSet:error:];
-[BKDevice setSystemProtectedConfiguration:credentialSet:reply:];
-[BKDevice systemProtectedConfigurationWithError:];
-[BKDevice updateIdentity:async:reply:];
-[BKDevice updateIdentity:reply:];
-[BKDevice valueForDeviceProperty:error:];
```
