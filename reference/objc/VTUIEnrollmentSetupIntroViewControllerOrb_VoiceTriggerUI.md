# `VTUIEnrollmentSetupIntroViewControllerOrb`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBWelcomeController`
- Protocols: `VTUIEnrollmentSetupIntroViewControlling`
- 8 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<VTUISiriIntroViewControllerDelegate>" _delegate;
B _showSiriConversations;
B _isPostUpgradeDisclosure;
B _includeHomePodInDisclosure;
B _showMultitriggerForSetup;
@"VTUIButton" _laterButton;
@"OBTrayButton" _continueButton;
@"NSString" _languageCode;
```

## Properties

```
@property (T@"VTUIButton",R,N,V_laterButton) laterButton;
@property (T@"OBTrayButton",R,N,V_continueButton) continueButton;
@property (T@"NSString",R,C,N,V_languageCode) languageCode;
```

## Instance methods

```
-[VTUIEnrollmentSetupIntroViewControllerOrb didEnterBackground];
-[VTUIEnrollmentSetupIntroViewControllerOrb initWithDelegate:];
-[VTUIEnrollmentSetupIntroViewControllerOrb languageCode];
-[VTUIEnrollmentSetupIntroViewControllerOrb continueButton];
-[VTUIEnrollmentSetupIntroViewControllerOrb laterButton];
-[VTUIEnrollmentSetupIntroViewControllerOrb _setupContent];
-[VTUIEnrollmentSetupIntroViewControllerOrb _continuePressed:];
-[VTUIEnrollmentSetupIntroViewControllerOrb _fadeInSubViews];
-[VTUIEnrollmentSetupIntroViewControllerOrb enrollmentWillAppear];
-[VTUIEnrollmentSetupIntroViewControllerOrb isLaterButtonAvailable];
-[VTUIEnrollmentSetupIntroViewControllerOrb setContinueButtonEnabled:];
-[VTUIEnrollmentSetupIntroViewControllerOrb setLaterButtonEnabled:];
-[VTUIEnrollmentSetupIntroViewControllerOrb shouldCleanupForEnrollment];
```
