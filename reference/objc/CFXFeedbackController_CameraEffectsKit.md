# `CFXFeedbackController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"_UIButtonFeedbackGenerator" __shutterButtonLatchingOnFeedbackGenerator;
@"_UIButtonFeedbackGenerator" __shutterButtonLatchingOffFeedbackGenerator;
@"_UIButtonFeedbackGenerator" __shutterButtonMomentaryFeedbackGenerator;
@"NSMutableSet" __activePairedFeedbackGenerators;
@"CUShutterButton" _shutterButton;
Q _feedbackToPerform;
```

## Properties

```
@property (T@"_UIButtonFeedbackGenerator",R,N,V__shutterButtonLatchingOnFeedbackGenerator) _shutterButtonLatchingOnFeedbackGenerator;
@property (T@"_UIButtonFeedbackGenerator",R,N,V__shutterButtonLatchingOffFeedbackGenerator) _shutterButtonLatchingOffFeedbackGenerator;
@property (T@"_UIButtonFeedbackGenerator",R,N,V__shutterButtonMomentaryFeedbackGenerator) _shutterButtonMomentaryFeedbackGenerator;
@property (T@"NSMutableSet",R,N,V__activePairedFeedbackGenerators) _activePairedFeedbackGenerators;
@property (T@"CUShutterButton",R,N,V_shutterButton) shutterButton;
@property (TQ,N,V_feedbackToPerform) feedbackToPerform;
```

## Instance methods

```
-[CFXFeedbackController _shutterButtonLatchingOnFeedbackGenerator];
-[CFXFeedbackController init];
-[CFXFeedbackController performPressButtonFeedback:];
-[CFXFeedbackController performReleaseButtonFeedback:];
-[CFXFeedbackController _shutterButtonMomentaryFeedbackGenerator];
-[CFXFeedbackController prepareButtonFeedback:];
-[CFXFeedbackController _shutterButtonLatchingOffFeedbackGenerator];
-[CFXFeedbackController _debugStringForPairedFeedback:];
-[CFXFeedbackController _activePairedFeedbackGenerators];
-[CFXFeedbackController _feedbackGeneratorForPairedFeedback:];
-[CFXFeedbackController shutterButton];
-[CFXFeedbackController feedbackToPerform];
-[CFXFeedbackController initWithShutterButton:];
-[CFXFeedbackController setFeedbackToPerform:];
-[CFXFeedbackController shutterButtonDown:];
-[CFXFeedbackController shutterButtonFeedbackForCurrentConfiguration];
-[CFXFeedbackController shutterButtonUp:];
```
