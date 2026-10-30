# `SSRSamplingManager`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
```

## Class methods

```
+[SSRSamplingManager sharedManager];
```

## Instance methods

```
-[SSRSamplingManager init];
-[SSRSamplingManager queue];
-[SSRSamplingManager setQueue:];
-[SSRSamplingManager getDonationDataWithEnrollmentId:error:];
-[SSRSamplingManager getDonationDataWithVoiceProfileId:error:];
-[SSRSamplingManager getDonationIdsWithEnrollmentId:error:];
-[SSRSamplingManager getEnrollmentDateWithLocale:error:];
-[SSRSamplingManager getEnrollmentIdWithLocale:error:];
-[SSRSamplingManager getEnrollmentSelectionStatusWithLocale:error:];
```
