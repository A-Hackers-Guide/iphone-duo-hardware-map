# `LACBiometryHelper`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 9 properties, 52 instance methods, 3 class methods

## Instance variables

```
@"NSMutableDictionary" _databaseHashesByUserId;
@"LACCacheSync" _biolockoutStateCache;
@"NSHashTable" _observers;
@"NSDictionary" _identities;
@"BKDevice" _device;
q _biometryType;
@"<LACBiometryDelegate>" _delegate;
@"NSError" _fault;
@"NSError" _permanentError;
q _deviceType;
```

## Properties

```
@property (T@"NSError",R,N,V_fault) fault;
@property (T@"NSError",R,N,V_permanentError) permanentError;
@property (Tq,R,N,V_deviceType) deviceType;
@property (T@"NSObject<OS_dispatch_queue>",R,N) workQueue;
@property (T@"NSDictionary",R,N,V_identities) identities;
@property (T@"NSDictionary",R,N) adminIdentities;
@property (T@"BKDevice",R,N,V_device) device;
@property (Tq,R,N,V_biometryType) biometryType;
@property (T@"<LACBiometryDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[LACBiometryHelper sharedInstance];
+[LACBiometryHelper touchIdInstance];
+[LACBiometryHelper faceIdInstance];
```

## Instance methods

```
-[LACBiometryHelper identities];
-[LACBiometryHelper _setup];
-[LACBiometryHelper isPeriocularMatchingEnabledForUser:];
-[LACBiometryHelper permanentError];
-[LACBiometryHelper isLockedOutForUser:request:error:];
-[LACBiometryHelper _setupDeviceWithDescriptor:];
-[LACBiometryHelper _shouldCacheIdentities];
-[LACBiometryHelper isNotLockedOutForAnyUserWithAdminRole:request:error:];
-[LACBiometryHelper removeObserver:];
-[LACBiometryHelper device];
-[LACBiometryHelper deviceType];
-[LACBiometryHelper isAnyUserEnrolledWithError:];
-[LACBiometryHelper workQueue];
-[LACBiometryHelper dealloc];
-[LACBiometryHelper isIdentificationEnabled:];
-[LACBiometryHelper _setupWithPermanentError:];
-[LACBiometryHelper _dumpEnvironmentForUser:];
-[LACBiometryHelper _handleLockoutStateChangedNotification];
-[LACBiometryHelper biometryLostErrorForUser:request:];
-[LACBiometryHelper addObserver:];
-[LACBiometryHelper setDelegate:];
-[LACBiometryHelper _isEnrolled:adminOnly:hardwareMustBeAvailable:error:];
-[LACBiometryHelper biometryDatabaseHashForUser:error:];
-[LACBiometryHelper lockoutErrorForState:userId:];
-[LACBiometryHelper dumpStatus];
-[LACBiometryHelper deviceHasBiometryWithError:];
-[LACBiometryHelper isBiometryOnForApplePay:];
-[LACBiometryHelper resetBiometry];
-[LACBiometryHelper _protectedConfigurationForUser:];
-[LACBiometryHelper isBiometryOnForUnlock:];
-[LACBiometryHelper _lockoutErrorForExtendedState:userId:];
-[LACBiometryHelper _errorDisconnected:notEnrolled:];
-[LACBiometryHelper delegate];
-[LACBiometryHelper biometryType];
-[LACBiometryHelper fault];
-[LACBiometryHelper _biolockoutStateForUser:request:error:];
-[LACBiometryHelper isLockedOutForUser:adminOnly:request:error:];
-[LACBiometryHelper catacombUUID:];
-[LACBiometryHelper _handleAccessoriesChangedNotification];
-[LACBiometryHelper _refreshIdentitiesDueToAccessoryChange:];
-[LACBiometryHelper _identitiesForUser:adminOnly:];
-[LACBiometryHelper _handleEnrollmentChangedNotification];
-[LACBiometryHelper _uidFromUserId:];
-[LACBiometryHelper _setupWithFault:];
-[LACBiometryHelper _shouldRetryAvailableDevices];
-[LACBiometryHelper isEnrolled:error:];
-[LACBiometryHelper initWithBiometryType:];
-[LACBiometryHelper userPresent:error:];
-[LACBiometryHelper _clearHashes];
-[LACBiometryHelper adminIdentities];
-[LACBiometryHelper isEnrolledWithoutHardware:error:];
-[LACBiometryHelper isAnyUserEnrolledWithAdminRole:error:];
```
