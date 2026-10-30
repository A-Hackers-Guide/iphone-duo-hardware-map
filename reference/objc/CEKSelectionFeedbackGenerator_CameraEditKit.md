# `CEKSelectionFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
I __endStopSoundID;
I __majorTickSoundID;
I __minorTickSoundID;
I __overscrollTickSoundID;
q _profile;
@"UISelectionFeedbackGenerator" __feedbackGenerator;
```

## Properties

```
@property (T@"UISelectionFeedbackGenerator",R,N,V__feedbackGenerator) _feedbackGenerator;
@property (TI,R,N,V__endStopSoundID) _endStopSoundID;
@property (TI,R,N,V__majorTickSoundID) _majorTickSoundID;
@property (TI,R,N,V__minorTickSoundID) _minorTickSoundID;
@property (TI,R,N,V__overscrollTickSoundID) _overscrollTickSoundID;
@property (Tq,N,V_profile) profile;
```

## Instance methods

```
-[CEKSelectionFeedbackGenerator init];
-[CEKSelectionFeedbackGenerator dealloc];
-[CEKSelectionFeedbackGenerator setProfile:];
-[CEKSelectionFeedbackGenerator profile];
-[CEKSelectionFeedbackGenerator _feedbackGenerator];
-[CEKSelectionFeedbackGenerator performFeedback];
-[CEKSelectionFeedbackGenerator prepareFeedback];
-[CEKSelectionFeedbackGenerator _endStopSoundID];
-[CEKSelectionFeedbackGenerator _majorTickSoundID];
-[CEKSelectionFeedbackGenerator _minorTickSoundID];
-[CEKSelectionFeedbackGenerator _overscrollTickSoundID];
-[CEKSelectionFeedbackGenerator _updateFeedbackGeneratorIfNeeded];
-[CEKSelectionFeedbackGenerator playEndTickSound];
-[CEKSelectionFeedbackGenerator playMajorTickSound];
-[CEKSelectionFeedbackGenerator playMinorTickSound];
-[CEKSelectionFeedbackGenerator playOverscrollTickSound];
```
