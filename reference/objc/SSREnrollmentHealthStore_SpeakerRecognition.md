# `SSREnrollmentHealthStore`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"_TtC18SpeakerRecognition29SSREnrollmentHealthCalculator" _healthCalculator;
```

## Properties

```
@property (T@"_TtC18SpeakerRecognition29SSREnrollmentHealthCalculator",&,N,V_healthCalculator) healthCalculator;
```

## Class methods

```
+[SSREnrollmentHealthStore sharedInstance];
```

## Instance methods

```
-[SSREnrollmentHealthStore init];
-[SSREnrollmentHealthStore updateEnrollmentHealthForVoiceProfile:asset:completionHandler:];
-[SSREnrollmentHealthStore _isHealthCalculationRequiredForProfile:];
-[SSREnrollmentHealthStore calculateEnrollmentHealthWithVoiceProfile:asset:completionHandler:];
-[SSREnrollmentHealthStore healthCalculator];
-[SSREnrollmentHealthStore setHealthCalculator:];
```
