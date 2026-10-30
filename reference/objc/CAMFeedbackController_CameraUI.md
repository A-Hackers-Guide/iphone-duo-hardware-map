# `CAMFeedbackController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"_UIDiscreteFeedback" __fullTap300Feedback;
@"_UIDiscreteFeedback" __fullTap270Feedback;
@"_UIButtonFeedbackGenerator" __shutterButtonMomentaryFeedbackGenerator;
@"_UIButtonFeedbackGenerator" __shutterButtonLatchingOnFeedbackGenerator;
@"_UIButtonFeedbackGenerator" __shutterButtonLatchingOffFeedbackGenerator;
@"NSMutableSet" __activePairedFeedbackGenerators;
@"NSMutableDictionary" __discreteFeedbackGenerators;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V__discreteFeedbackGenerators) _discreteFeedbackGenerators;
@property (T@"_UIButtonFeedbackGenerator",R,N,V__shutterButtonLatchingOnFeedbackGenerator) _shutterButtonLatchingOnFeedbackGenerator;
@property (T@"_UIButtonFeedbackGenerator",R,N,V__shutterButtonLatchingOffFeedbackGenerator) _shutterButtonLatchingOffFeedbackGenerator;
@property (T@"_UIButtonFeedbackGenerator",R,N,V__shutterButtonMomentaryFeedbackGenerator) _shutterButtonMomentaryFeedbackGenerator;
@property (T@"NSMutableSet",R,N,V__activePairedFeedbackGenerators) _activePairedFeedbackGenerators;
@property (T@"_UIDiscreteFeedback",R,N,V__fullTap300Feedback) _fullTap300Feedback;
@property (T@"_UIDiscreteFeedback",R,N,V__fullTap270Feedback) _fullTap270Feedback;
```

## Class methods

```
+[CAMFeedbackController sharedController];
```

## Instance methods

```
-[CAMFeedbackController performDiscreteFeedback:];
-[CAMFeedbackController prepareDiscreteFeedback:];
-[CAMFeedbackController _newFeedbackGeneratorForDiscreteFeedback:];
-[CAMFeedbackController _shutterButtonLatchingOnFeedbackGenerator];
-[CAMFeedbackController init];
-[CAMFeedbackController _feedbackGeneratorForDiscreteFeedback:];
-[CAMFeedbackController _discreteFeedbackGenerators];
-[CAMFeedbackController _fullTap300Feedback];
-[CAMFeedbackController _fullTap270Feedback];
-[CAMFeedbackController performPressButtonFeedback:];
-[CAMFeedbackController performReleaseButtonFeedback:];
-[CAMFeedbackController _shutterButtonMomentaryFeedbackGenerator];
-[CAMFeedbackController prepareButtonFeedback:];
-[CAMFeedbackController _configurationForFeedback:];
-[CAMFeedbackController _shutterButtonLatchingOffFeedbackGenerator];
-[CAMFeedbackController _debugStringForPairedFeedback:];
-[CAMFeedbackController _activePairedFeedbackGenerators];
-[CAMFeedbackController _feedbackGeneratorForPairedFeedback:];
```
