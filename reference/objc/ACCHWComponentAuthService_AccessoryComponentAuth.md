# `ACCHWComponentAuthService`

- Image: [`/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth`](../userland/System__Library__PrivateFrameworks__AccessoryComponentAuth.framework__AccessoryComponentAuth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCHWComponentAuthServiceProtocol`
- 1 instance variables, 1 properties, 43 instance methods, 3 class methods

## Instance variables

```
@"NSMutableDictionary" _sessionUUIDs;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_sessionUUIDs) sessionUUIDs;
```

## Class methods

```
+[ACCHWComponentAuthService _verifyModuleFDR:forModuleType:];
+[ACCHWComponentAuthService _findFDRCertData:forModuleType:withAuthParams:hasDeviceCert:withError:];
+[ACCHWComponentAuthService _validateDeviceAndFDRCert:forModuleType:withAuthParams:];
```

## Instance methods

```
-[ACCHWComponentAuthService authenticateRCAMWithChallenge:completionHandler:updateRegistry:];
-[ACCHWComponentAuthService authenticateBatteryWithChallenge:completionHandler:];
-[ACCHWComponentAuthService authenticateBatteryWithChallenge:completionHandler:componentIndex:];
-[ACCHWComponentAuthService authenticateLASWithChallenge:completionHandler:updateRegistry:];
-[ACCHWComponentAuthService authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:];
-[ACCHWComponentAuthService authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:];
-[ACCHWComponentAuthService authenticateTouchControllerWithChallenge:completionHandler:];
-[ACCHWComponentAuthService authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:];
-[ACCHWComponentAuthService authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:];
-[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:];
-[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:componentIndex:];
-[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:];
-[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:];
-[ACCHWComponentAuthService signRCAMChallenge:completionHandler:];
-[ACCHWComponentAuthService signRCAMChallenge:completionHandler:componentIndex:];
-[ACCHWComponentAuthService signTouchControllerChallenge:completionHandler:componentIndex:];
-[ACCHWComponentAuthService signVeridianChallenge:completionHandler:];
-[ACCHWComponentAuthService signVeridianChallenge:completionHandler:componentIndex:];
-[ACCHWComponentAuthService verifyBatteryMatch:completionHandler:];
-[ACCHWComponentAuthService _readSignature:];
-[ACCHWComponentAuthService _logToAnalytics:authError:fdrValidationStatus:authDurationInMS:];
-[ACCHWComponentAuthService _signChallenge:];
-[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:];
-[ACCHWComponentAuthService _findAllModuleAuthServices:];
-[ACCHWComponentAuthService _findModuleAuthService:withAuthFlags:componentIndex:];
-[ACCHWComponentAuthService _notifyComponentAuthFailure];
-[ACCHWComponentAuthService _readCertificate:];
-[ACCHWComponentAuthService _readDeviceIDSN:];
-[ACCHWComponentAuthService _signChallengeForModuleType:challenge:componentIndex:completionHandler:];
-[ACCHWComponentAuthService _validateWithFDRCertificate:forModuleType:withAuthParams:];
-[ACCHWComponentAuthService _verifyBatteryMatch:];
-[ACCHWComponentAuthService _verifyBatteryMatch:outputBatteryCode:];
-[ACCHWComponentAuthService _verifyCertificate:];
-[ACCHWComponentAuthService _verifyDeviceInfo:];
-[ACCHWComponentAuthService _verifySignature:];
-[ACCHWComponentAuthService displayAuthCloseSession:completionHandler:];
-[ACCHWComponentAuthService displayAuthOpenSession:intermediateCertificate:keyData:completionHandler:];
-[ACCHWComponentAuthService displayAuthRefreshAccessState:completionHandler:];
-[ACCHWComponentAuthService displayAuthUserNVMRead:key:completionHandler:];
-[ACCHWComponentAuthService displayAuthUserNVMWrite:key:value:completionHandler:];
-[ACCHWComponentAuthService getTouchControllerQueue];
-[ACCHWComponentAuthService sessionUUIDs];
-[ACCHWComponentAuthService setSessionUUIDs:];
```
