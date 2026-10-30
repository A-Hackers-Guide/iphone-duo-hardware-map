# `BKUIDevice`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 39 instance methods, 2 class methods

## Instance variables

```
B _isZoomEnabled;
B _shouldUseUnifiedMesaEnrollment;
B _isPad;
B _isNonHomeButtonSensor;
i _mainScreenClass;
@"NSObject<OS_os_log>" _log;
@"BKDevicePearl" _pearlDevice;
@"BKDeviceTouchID" _touchIDDevice;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,N,V_log) log;
@property (Ti,N,V_mainScreenClass) mainScreenClass;
@property (TB,N,V_isPad) isPad;
@property (T@"BKDevicePearl",&,N,V_pearlDevice) pearlDevice;
@property (T@"BKDeviceTouchID",&,N,V_touchIDDevice) touchIDDevice;
@property (TB,N,V_isZoomEnabled) isZoomEnabled;
@property (TB,N,V_isNonHomeButtonSensor) isNonHomeButtonSensor;
@property (TB,N,V_shouldUseUnifiedMesaEnrollment) shouldUseUnifiedMesaEnrollment;
```

## Class methods

```
+[BKUIDevice sharedInstance];
+[BKUIDevice setSharedInstance:];
```

## Instance methods

```
-[BKUIDevice setLog:];
-[BKUIDevice isPad];
-[BKUIDevice init];
-[BKUIDevice setIsPad:];
-[BKUIDevice log];
-[BKUIDevice isZoomEnabled];
-[BKUIDevice setPearlDevice:];
-[BKUIDevice deviceForType:];
-[BKUIDevice deviceTypeForIdentityType:];
-[BKUIDevice identitiesForIdentityType:];
-[BKUIDevice pearlDevice];
-[BKUIDevice setTouchIDDevice:];
-[BKUIDevice touchIDDevice];
-[BKUIDevice _isV68];
-[BKUIDevice mainScreenClass];
-[BKUIDevice isIdiomPad];
-[BKUIDevice isCompactScreen];
-[BKUIDevice isIPad2];
-[BKUIDevice isD10];
-[BKUIDevice isD32Sized];
-[BKUIDevice isD33];
-[BKUIDevice isEnrolledInFaceID];
-[BKUIDevice isJ7xx];
-[BKUIDevice isJ8xx];
-[BKUIDevice isMini];
-[BKUIDevice isN69];
-[BKUIDevice isN84];
-[BKUIDevice isNonHomeButtonSensor];
-[BKUIDevice isNonHomeButtonTouchIDDevice];
-[BKUIDevice isPad6];
-[BKUIDevice isPad7];
-[BKUIDevice isRestrictedToLandscapeEnrollment];
-[BKUIDevice isiPad21];
-[BKUIDevice setIsNonHomeButtonSensor:];
-[BKUIDevice setIsZoomEnabled:];
-[BKUIDevice setMainScreenClass:];
-[BKUIDevice setShouldUseUnifiedMesaEnrollment:];
-[BKUIDevice shouldUseUnifiedMesaEnrollment];
-[BKUIDevice virtualDeviceSensorPosition];
```
