# `SBDefaultAuthenticationPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFAuthenticationPolicy`
- 6 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBiCloudPasscodeRequirementLockoutController" _iCloudPasscodeRequirementLockoutController;
@"SBSoftwareUpdatePasscodePolicyManager" _softwareUpdatePasscodePolicyManager;
@"SecureBackup" _secureBackupHelper;
@"SBFMobileKeyBag" _keyBag;
@"SBUserSessionController" _userSessionController;
@"SBRestartManager" _restartManager;
```

## Properties

```
@property (T@"SecureBackup",&,N,G_secureBackupHelper,S_setSecureBackupHelper:,V_secureBackupHelper) secureBackupHelper;
@property (T@"SBFMobileKeyBag",R,N,V_keyBag) keyBag;
@property (T@"SBUserSessionController",R,N,V_userSessionController) userSessionController;
@property (T@"SBRestartManager",R,N,V_restartManager) restartManager;
@property (T@"SBiCloudPasscodeRequirementLockoutController",&,N,V_iCloudPasscodeRequirementLockoutController) iCloudPasscodeRequirementLockoutController;
@property (T@"SBSoftwareUpdatePasscodePolicyManager",&,N,V_softwareUpdatePasscodePolicyManager) softwareUpdatePasscodePolicyManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDefaultAuthenticationPolicy userSessionController];
-[SBDefaultAuthenticationPolicy allowAuthenticationRevocation];
-[SBDefaultAuthenticationPolicy cachePasscode:];
-[SBDefaultAuthenticationPolicy clearPasscodeCache];
-[SBDefaultAuthenticationPolicy passcodeAuthenticationFailedWithError:];
-[SBDefaultAuthenticationPolicy shouldClearBlockStateOnSync];
-[SBDefaultAuthenticationPolicy usesSecureMode];
-[SBDefaultAuthenticationPolicy wipeDeviceWithReason:];
-[SBDefaultAuthenticationPolicy _secureBackupHelper];
-[SBDefaultAuthenticationPolicy _setSecureBackupHelper:];
-[SBDefaultAuthenticationPolicy iCloudPasscodeRequirementLockoutController];
-[SBDefaultAuthenticationPolicy initWithMobileKeyBag:userSessionController:restartManager:];
-[SBDefaultAuthenticationPolicy keyBag];
-[SBDefaultAuthenticationPolicy restartManager];
-[SBDefaultAuthenticationPolicy setICloudPasscodeRequirementLockoutController:];
-[SBDefaultAuthenticationPolicy setSoftwareUpdatePasscodePolicyManager:];
-[SBDefaultAuthenticationPolicy softwareUpdatePasscodePolicyManager];
```
