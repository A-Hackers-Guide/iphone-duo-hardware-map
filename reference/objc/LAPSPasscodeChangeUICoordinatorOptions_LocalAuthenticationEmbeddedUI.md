# `LAPSPasscodeChangeUICoordinatorOptions`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _isPasscodeRecoveryOptionVisible;
B _isPasscodeRecoveryMessageHidden;
@"NSString" _title;
@"NSString" _oldPasscodePrompt;
@"NSString" _oldPasscodeSubPrompt;
@"NSString" _passcodePrompt;
@"NSString" _passcodeSubPrompt;
```

## Properties

```
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSString",&,N,V_oldPasscodePrompt) oldPasscodePrompt;
@property (T@"NSString",&,N,V_oldPasscodeSubPrompt) oldPasscodeSubPrompt;
@property (T@"NSString",&,N,V_passcodePrompt) passcodePrompt;
@property (T@"NSString",&,N,V_passcodeSubPrompt) passcodeSubPrompt;
@property (TB,N,V_isPasscodeRecoveryOptionVisible) isPasscodeRecoveryOptionVisible;
@property (TB,N,V_isPasscodeRecoveryMessageHidden) isPasscodeRecoveryMessageHidden;
```

## Instance methods

```
-[LAPSPasscodeChangeUICoordinatorOptions title];
-[LAPSPasscodeChangeUICoordinatorOptions setTitle:];
-[LAPSPasscodeChangeUICoordinatorOptions setPasscodePrompt:];
-[LAPSPasscodeChangeUICoordinatorOptions isPasscodeRecoveryOptionVisible];
-[LAPSPasscodeChangeUICoordinatorOptions isPasscodeRecoveryMessageHidden];
-[LAPSPasscodeChangeUICoordinatorOptions oldPasscodePrompt];
-[LAPSPasscodeChangeUICoordinatorOptions oldPasscodeSubPrompt];
-[LAPSPasscodeChangeUICoordinatorOptions passcodePrompt];
-[LAPSPasscodeChangeUICoordinatorOptions passcodeSubPrompt];
-[LAPSPasscodeChangeUICoordinatorOptions setIsPasscodeRecoveryMessageHidden:];
-[LAPSPasscodeChangeUICoordinatorOptions setIsPasscodeRecoveryOptionVisible:];
-[LAPSPasscodeChangeUICoordinatorOptions setOldPasscodePrompt:];
-[LAPSPasscodeChangeUICoordinatorOptions setOldPasscodeSubPrompt:];
-[LAPSPasscodeChangeUICoordinatorOptions setPasscodeSubPrompt:];
```
