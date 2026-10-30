# `SBiCloudPasscodeRequirementLockoutController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSoftLockoutControllerDelegate`, `SBWindowSceneAttachmentObserving`
- 3 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _softLockoutControllers;
@"SBFMobileKeyBag" _mobileKeybag;
B _providedPasscode;
```

## Properties

```
@property (TB,R,N) desiresPasscode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBiCloudPasscodeRequirementLockoutController init];
-[SBiCloudPasscodeRequirementLockoutController windowSceneDidDisconnect:];
-[SBiCloudPasscodeRequirementLockoutController windowSceneDidConnect:];
-[SBiCloudPasscodeRequirementLockoutController desiresPasscode];
-[SBiCloudPasscodeRequirementLockoutController _deviceHasComplexPasscode];
-[SBiCloudPasscodeRequirementLockoutController initWithMobileKeyBag:];
-[SBiCloudPasscodeRequirementLockoutController noteAuthenticationSucceededWithPasscode:];
-[SBiCloudPasscodeRequirementLockoutController softLockoutControllerRequiresLockout:];
```
