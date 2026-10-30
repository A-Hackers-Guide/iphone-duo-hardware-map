# `LACFlagsProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `LACFlagsProviderAutoLock`, `LACFlagsProviderDTO`, `LACFlagsCredentials`
- 0 instance variables, 45 properties, 45 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) flagAuthDialogUseAlwaysOnPasswordFieldEnabledKey;
@property (TB,R,N) valueForFlagAuthDialogUseAlwaysOnPasswordFieldEnabled;
@property (T@"NSString",R,N) flagCompanionMockDevicesKey;
@property (T@"NSNumber",R,N) valueForFlagCompanionMockDevices;
@property (T@"NSString",R,N) flagCompanionSessionAuthenticationKey;
@property (T@"NSData",R,N) valueForFlagCompanionSessionAuthentication;
@property (T@"NSString",R,N) flagDisableSensitiveUIRedactionKey;
@property (TB,R,N) valueForFlagDisableSensitiveUIRedaction;
@property (T@"NSString",R,N) flagOnenessSessionActiveKey;
@property (T@"NSNumber",R,N) valueForFlagOnenessSessionActive;
@property (T@"NSString",R,N) flagPhoneIntegrationSessionActiveKey;
@property (T@"NSNumber",R,N) valueForFlagPhoneIntegrationSessionActive;
@property (T@"NSString",R,N) flagPreboardModeKey;
@property (T@"NSNumber",R,N) valueForFlagPreboardMode;
@property (T@"NSString",R,N) flagReleaseUIDelegateKey;
@property (TB,R,N) valueForFlagReleaseUIDelegate;
@property (T@"NSString",R,N) flagRunningInBATSKey;
@property (T@"NSNumber",R,N) valueForFlagRunningInBATS;
@property (T@"NSString",R,N) flagSharedModeActiveKey;
@property (T@"NSNumber",R,N) valueForFlagSharedModeActive;
@property (T@"NSString",R,N) flagSharedModeLatencyKey;
@property (T@"NSNumber",R,N) valueForFlagSharedModeLatency;
@property (T@"NSString",R,N) flagSimulatorPasscodeTypeKey;
@property (T@"NSNumber",R,N) valueForFlagSimulatorPasscodeType;
@property (T@"NSString",R,N) flagUseTestAppleKeyStoreDaemonKey;
@property (T@"NSNumber",R,N) valueForFlagUseTestAppleKeyStoreDaemon;
@property (TB,R,N) featureFlagAllowTouchIDLandscapeEnabled;
@property (TB,R,N) featureFlagEssoniteClickEnabled;
@property (TB,R,N) featureFlagExtendedAHPEnabled;
@property (TB,R,N) featureFlagExtractableCredentialProtectionEnabled;
@property (TB,R,N) featureFlagLightweightTouchIDEnabled;
@property (TB,R,N) featureFlagPasscodeServicesProtectionEnabled;
@property (TB,R,N) featureFlagPasscodeServicesUseKeyboardGuideEnabled;
@property (TB,R,N) featureFlagPasscodeServicesUseKeyboardGuidePadsEnabled;
@property (TB,R,N) featureFlagPhoneIntegrationEnabled;
@property (TB,R,N) featureFlagPreboardEnabled;
@property (TB,R,N) featureFlagPreboardDeveloperModeEnabled;
@property (TB,R,N) featureFlagPreboardProtectedVariablesEnabled;
@property (TB,R,N) featureFlagPreboardUPPEnabled;
@property (TB,R,N) featureFlagPresentationContextEnabled;
@property (TB,R,N) featureFlagSwiftUIDialogMacOSEnabled;
@property (TB,R,N) featureFlagSwiftUIPasscodeEnabled;
@property (TB,R,N) featureFlagSwiftUIPasscodeLandscapeEnabled;
@property (TB,R,N) featureFlagSwiftUIPasscodeServicesEnabled;
@property (TB,R,N) featureFlagUserAuthDaemonEnabled;
```

## Instance methods

```
-[LACFlagsProvider featureFlagExtractableCredentialProtectionEnabled];
-[LACFlagsProvider featureFlagEssoniteClickEnabled];
-[LACFlagsProvider featureFlagAllowTouchIDLandscapeEnabled];
-[LACFlagsProvider featureFlagExtendedAHPEnabled];
-[LACFlagsProvider featureFlagLightweightTouchIDEnabled];
-[LACFlagsProvider featureFlagPasscodeServicesProtectionEnabled];
-[LACFlagsProvider featureFlagPasscodeServicesUseKeyboardGuideEnabled];
-[LACFlagsProvider featureFlagPasscodeServicesUseKeyboardGuidePadsEnabled];
-[LACFlagsProvider featureFlagPhoneIntegrationEnabled];
-[LACFlagsProvider featureFlagPreboardDeveloperModeEnabled];
-[LACFlagsProvider featureFlagPreboardEnabled];
-[LACFlagsProvider featureFlagPreboardProtectedVariablesEnabled];
-[LACFlagsProvider featureFlagPreboardUPPEnabled];
-[LACFlagsProvider featureFlagPresentationContextEnabled];
-[LACFlagsProvider featureFlagSwiftUIDialogMacOSEnabled];
-[LACFlagsProvider featureFlagSwiftUIPasscodeEnabled];
-[LACFlagsProvider featureFlagSwiftUIPasscodeLandscapeEnabled];
-[LACFlagsProvider featureFlagSwiftUIPasscodeServicesEnabled];
-[LACFlagsProvider featureFlagUserAuthDaemonEnabled];
-[LACFlagsProvider flagAuthDialogUseAlwaysOnPasswordFieldEnabledKey];
-[LACFlagsProvider flagCompanionMockDevicesKey];
-[LACFlagsProvider flagCompanionSessionAuthenticationKey];
-[LACFlagsProvider flagDisableSensitiveUIRedactionKey];
-[LACFlagsProvider flagOnenessSessionActiveKey];
-[LACFlagsProvider flagPhoneIntegrationSessionActiveKey];
-[LACFlagsProvider flagPreboardModeKey];
-[LACFlagsProvider flagReleaseUIDelegateKey];
-[LACFlagsProvider flagRunningInBATSKey];
-[LACFlagsProvider flagSharedModeActiveKey];
-[LACFlagsProvider flagSharedModeLatencyKey];
-[LACFlagsProvider flagSimulatorPasscodeTypeKey];
-[LACFlagsProvider flagUseTestAppleKeyStoreDaemonKey];
-[LACFlagsProvider valueForFlagAuthDialogUseAlwaysOnPasswordFieldEnabled];
-[LACFlagsProvider valueForFlagCompanionMockDevices];
-[LACFlagsProvider valueForFlagCompanionSessionAuthentication];
-[LACFlagsProvider valueForFlagDisableSensitiveUIRedaction];
-[LACFlagsProvider valueForFlagOnenessSessionActive];
-[LACFlagsProvider valueForFlagPhoneIntegrationSessionActive];
-[LACFlagsProvider valueForFlagPreboardMode];
-[LACFlagsProvider valueForFlagReleaseUIDelegate];
-[LACFlagsProvider valueForFlagRunningInBATS];
-[LACFlagsProvider valueForFlagSharedModeActive];
-[LACFlagsProvider valueForFlagSharedModeLatency];
-[LACFlagsProvider valueForFlagSimulatorPasscodeType];
-[LACFlagsProvider valueForFlagUseTestAppleKeyStoreDaemon];
```
