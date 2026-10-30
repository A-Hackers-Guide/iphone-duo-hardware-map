# `SBWalletPreArmController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NFWalletPresentation" _walletPresentation;
@"<SBUIBiometricResource>" _biometricResource;
q _triggerSource;
@"NSHashTable" _disabledPreArmAssertions;
@"NSMutableDictionary" _disabledPreArmAssertionsByType;
B _walletDoublePressConsumerAvailable;
@"NSUserDefaults" _nfDefaults;
@"<BSInvalidatable>" _stateCaptureAssertion;
```

## Properties

```
@property (T@"NSUserDefaults",&,N,G_getNFDefaults,S_setNFDefaults:,V_nfDefaults) nfDefaults;
@property (TB,R,D,N,GisPreArmAvailable) preArmAvailable;
@property (TB,R,D,N,GisPreArmAllowed) preArmAllowed;
@property (TB,R,D,N,GisPreArmTriggeredByLockButtonDoublePress) preArmTriggeredByLockButtonDoublePress;
@property (TB,R,D,N,GisPreArmTriggeredByHomeButtonDoublePress) preArmTriggeredByHomeButtonDoublePress;
@property (TB,R,D,N,GisPreArmSuppressed) preArmSuppressed;
@property (TB,R,D,N,GisPreArmExternallySuppressed) preArmExternallySuppressed;
```

## Class methods

```
+[SBWalletPreArmController sharedInstance];
```

## Instance methods

```
-[SBWalletPreArmController observeValueForKeyPath:ofObject:change:context:];
-[SBWalletPreArmController succinctDescriptionBuilder];
-[SBWalletPreArmController init];
-[SBWalletPreArmController dealloc];
-[SBWalletPreArmController descriptionWithMultilinePrefix:];
-[SBWalletPreArmController succinctDescription];
-[SBWalletPreArmController description];
-[SBWalletPreArmController descriptionBuilderWithMultilinePrefix:];
-[SBWalletPreArmController _setNFDefaults:];
-[SBWalletPreArmController isPreArmAllowed];
-[SBWalletPreArmController _computeTriggerSource];
-[SBWalletPreArmController _contactlessInterfaceSourceForTriggerSource:];
-[SBWalletPreArmController _getNFDefaults];
-[SBWalletPreArmController acquireSuppressPreArmAssertionForReason:];
-[SBWalletPreArmController acquireSuppressPreArmAssertionOfType:forReason:];
-[SBWalletPreArmController initWithWalletPresentation:biometricResource:];
-[SBWalletPreArmController isPreArmAvailable];
-[SBWalletPreArmController isPreArmExternallySuppressed];
-[SBWalletPreArmController isPreArmSuppressed];
-[SBWalletPreArmController isPreArmTriggeredByHomeButtonDoublePress];
-[SBWalletPreArmController isPreArmTriggeredByLockButtonDoublePress];
-[SBWalletPreArmController presentPreArmInterfaceForWalletConsumer];
```
