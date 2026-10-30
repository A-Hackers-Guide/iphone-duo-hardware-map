# `VTUIGMEnrollmentViewController`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBWelcomeController`
- Protocols: `UNNotificationOnboardingControllerDelegate`, `_TtP14VoiceTriggerUI45VisualIntelligenceIntroViewControllerDelegate_`
- 8 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"<VTUIGMEnrollmentViewControllerDelegate>" _delegate;
@"CSFAvailability" _availability;
@"_TtC14VoiceTriggerUI23GMAvailabilityViewModel" _viewModel;
Q _enrollmentType;
@"_TtC14VoiceTriggerUI20GMHeaderIconProvider" _headerIconProvider;
@"UIViewController<UNNotificationOnboardingController>" _summarizationOnboardingController;
@"OBTrayButton" continueButton;
B _isSkippingIntroduction;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTUIGMEnrollmentViewController initWithDelegate:];
-[VTUIGMEnrollmentViewController userDidCancel];
-[VTUIGMEnrollmentViewController viewDidLoad];
-[VTUIGMEnrollmentViewController viewWillAppear:];
-[VTUIGMEnrollmentViewController onboardingControllerDidFinish:];
-[VTUIGMEnrollmentViewController onboardingController:requestsPushingTo:];
-[VTUIGMEnrollmentViewController onboardingControllerRequestsCancellation:];
-[VTUIGMEnrollmentViewController onboardingControllerRequestsGoingBack:];
-[VTUIGMEnrollmentViewController _setupContent];
-[VTUIGMEnrollmentViewController _continueFromGMEnrollment];
-[VTUIGMEnrollmentViewController _discoverAppleIntelligenceButton];
-[VTUIGMEnrollmentViewController _enrollUserIntoWaitlist];
-[VTUIGMEnrollmentViewController _presentAppleIntelligenceTipsView];
-[VTUIGMEnrollmentViewController _presentEnrollmentErrorWithCompletion:];
-[VTUIGMEnrollmentViewController _pushVisualIntelligenceIntro];
-[VTUIGMEnrollmentViewController _userDidTapContinueButton];
-[VTUIGMEnrollmentViewController _userDidTapSetupLaterButton];
-[VTUIGMEnrollmentViewController initWithEnrollmentType:delegate:];
-[VTUIGMEnrollmentViewController userDidTapContinue:];
```
