# `_TtC14VoiceTriggerUI23GMAvailabilityViewModel`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 13 instance methods, 3 class methods

## Instance variables

```
GenerativeModels.GenerativeModelsAvailability provider;
_$sSo9VTUIStyleC vtuiStyle;
VoiceTriggerUI.GMAnalyticsProvider analyticsProvider;
```

## Properties

```
@property (TB,N,R) isBuddyOrCFU;
@property (TB,N,R) hasCameraButton;
@property (TB,N,R) shouldShowVisualIntelligenceIntro;
```

## Class methods

```
+[_TtC14VoiceTriggerUI23GMAvailabilityViewModel isDeviceEligible];
+[_TtC14VoiceTriggerUI23GMAvailabilityViewModel isBuddy];
+[_TtC14VoiceTriggerUI23GMAvailabilityViewModel shouldShowGM];
```

## Instance methods

```
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel init];
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel hasCameraButton];
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel enrollmentType];
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel optInGM];
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel continueButtonTitleKeyWithEnrollmentType:];
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel isBuddyOrCFU];
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel sendCancelEventWithEnrollmentType:];
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel sendContinueEventWithEnrollmentType:];
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel sendViewDidLoadEventWithEnrollmentType:];
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel shouldShowVisualIntelligenceIntro];
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel showNotNowWithEnrollmentType:];
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel subtitleKeyWithEnrollmentType:];
-[_TtC14VoiceTriggerUI23GMAvailabilityViewModel titleKeyWithEnrollmentType:];
```
