# `LARatchetManager`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACContextProviding`
- 1 instance variables, 13 properties, 32 instance methods, 5 class methods

## Instance variables

```
@"LACDTORatchetManager" _coreManager;
```

## Properties

```
@property (TB,R,N) isFeatureEnabled;
@property (TB,R,N) isFeatureSupported;
@property (TB,R,N) isFeatureAvailable;
@property (TB,R,N) isFeatureStrictModeEnabled;
@property (TB,R,N) isExtendedPolicyProtectionAvailable;
@property (TB,R,N) isExtendedPolicyProtectionEnabled;
@property (TB,R,N) isSensorTrusted;
@property (T@"LARatchetState",R,N) ratchetState;
@property (TB,R,N) isRatchetFeatureEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LARatchetManager sharedInstance];
+[LARatchetManager _optionForRatchetOption:];
+[LARatchetManager optionsForRatchetArmOptions:];
+[LARatchetManager ratchetErrorForError:];
+[LARatchetManager ratchetResultForResult:];
```

## Instance methods

```
-[LARatchetManager removeObserver:];
-[LARatchetManager init];
-[LARatchetManager reset];
-[LARatchetManager addObserver:];
-[LARatchetManager isFeatureSupported];
-[LARatchetManager isExtendedPolicyProtectionEnabled];
-[LARatchetManager isExtendedPolicyProtectionAvailable];
-[LARatchetManager isFeatureEnabled];
-[LARatchetManager ratchetState];
-[LARatchetManager createContext];
-[LARatchetManager isFeatureAvailable];
-[LARatchetManager stateWithCompletion:];
-[LARatchetManager enableFeatureWithOptions:reply:];
-[LARatchetManager isSensorTrusted];
-[LARatchetManager cancelArmRequestWithIdentifier:reason:completion:];
-[LARatchetManager cancelCurrentRatchetWithReason:completion:];
-[LARatchetManager checkCanEnableFeatureWithCompletion:];
-[LARatchetManager currentRatchetWithCompletion:];
-[LARatchetManager disableExtendedPolicyProtectionWithContext:completion:];
-[LARatchetManager disableFeatureStrictModeWithContext:completion:];
-[LARatchetManager disableFeatureWithContext:completion:];
-[LARatchetManager enableExtendedPolicyProtectionWithCompletion:];
-[LARatchetManager enableFeatureActivatingGracePeriodWithReply:];
-[LARatchetManager enableFeatureStrictModeWithCompletion:];
-[LARatchetManager enableFeatureWithCompletion:];
-[LARatchetManager enableFeatureWithReply:];
-[LARatchetManager isAutoEnablementAllowed:];
-[LARatchetManager isFeatureStrictModeEnabled];
-[LARatchetManager isRatchetFeatureEnabled];
-[LARatchetManager performArmRequestWithContext:options:completion:];
-[LARatchetManager resetRatchetWithReason:completion:];
-[LARatchetManager stateInContext:completion:];
```
