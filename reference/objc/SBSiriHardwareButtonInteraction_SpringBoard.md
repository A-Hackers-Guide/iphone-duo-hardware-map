# `SBSiriHardwareButtonInteraction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHardwareButtonGestureParametersProviderBase`
- Protocols: `SiriLongPressButtonSourceDelegate`, `SBHardwareButtonInteraction`
- 6 instance variables, 10 properties, 25 instance methods, 4 class methods

## Instance variables

```
d _initialPressDownTime;
q _siriButtonIdentifier;
@"SiriLongPressButtonSource" _siriActivationSource;
d _activationInterval;
@"<SiriAssertion>" _siriPreheatAssertion;
@"<SiriAssertion>" _siriButtonDownAssertion;
```

## Properties

```
@property (Tq,N,V_siriButtonIdentifier) siriButtonIdentifier;
@property (T@"SiriLongPressButtonSource",&,N,V_siriActivationSource) siriActivationSource;
@property (Td,N,V_activationInterval) activationInterval;
@property (T@"<SiriAssertion>",&,N,V_siriPreheatAssertion) siriPreheatAssertion;
@property (T@"<SiriAssertion>",&,N,V_siriButtonDownAssertion) siriButtonDownAssertion;
@property (Td,N,V_initialPressDownTime) initialPressDownTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSiriHardwareButtonInteraction dismissSiriTransientOverlayOnSinglePressUp:];
+[SBSiriHardwareButtonInteraction hardwareButtonInteractionForHomeButton];
+[SBSiriHardwareButtonInteraction hardwareButtonInteractionForLockButton];
+[SBSiriHardwareButtonInteraction hardwareButtonInteractionForVoiceCommandButton];
```

## Instance methods

```
-[SBSiriHardwareButtonInteraction consumeInitialPressDown];
-[SBSiriHardwareButtonInteraction observeFinalPressUp];
-[SBSiriHardwareButtonInteraction hardwareButtonGestureParameters];
-[SBSiriHardwareButtonInteraction siriButtonIdentifier];
-[SBSiriHardwareButtonInteraction configurationDidUpdateOnLongPressSource:];
-[SBSiriHardwareButtonInteraction _cancelAllSiriActions];
-[SBSiriHardwareButtonInteraction _cancelPreheating];
-[SBSiriHardwareButtonInteraction _preheatSiriForPresentationAfterInterval:];
-[SBSiriHardwareButtonInteraction _siriHomeButtonPrefsDidChange:];
-[SBSiriHardwareButtonInteraction activationInterval];
-[SBSiriHardwareButtonInteraction consumeLongPress];
-[SBSiriHardwareButtonInteraction consumeSinglePressUp];
-[SBSiriHardwareButtonInteraction initWithSiriButton:];
-[SBSiriHardwareButtonInteraction initialPressDownTime];
-[SBSiriHardwareButtonInteraction observeInitialPressUp];
-[SBSiriHardwareButtonInteraction observeLongPressCanceled];
-[SBSiriHardwareButtonInteraction setActivationInterval:];
-[SBSiriHardwareButtonInteraction setInitialPressDownTime:];
-[SBSiriHardwareButtonInteraction setSiriActivationSource:];
-[SBSiriHardwareButtonInteraction setSiriButtonDownAssertion:];
-[SBSiriHardwareButtonInteraction setSiriButtonIdentifier:];
-[SBSiriHardwareButtonInteraction setSiriPreheatAssertion:];
-[SBSiriHardwareButtonInteraction siriActivationSource];
-[SBSiriHardwareButtonInteraction siriButtonDownAssertion];
-[SBSiriHardwareButtonInteraction siriPreheatAssertion];
```
