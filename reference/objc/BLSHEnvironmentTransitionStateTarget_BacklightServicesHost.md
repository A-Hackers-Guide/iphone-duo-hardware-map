# `BLSHEnvironmentTransitionStateTarget`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _isFlipbook;
B _hasExplicitFlipbook;
B _didUpdateInitialState;
B _didCompleteAnimation;
Q _sequenceID;
@"BLSBacklightChangeEvent" _triggerEvent;
@"BLSHPendingBacklightRamp" _pendingBacklightRamp;
@"BLSBacklightSceneVisualState" _visualState;
@"NSDate" _presentationDate;
Q _lowPowerRenderingPresentationTime;
q _backlightState;
```

## Properties

```
@property (TQ,R,N,V_sequenceID) sequenceID;
@property (T@"BLSBacklightChangeEvent",R,N,V_triggerEvent) triggerEvent;
@property (T@"BLSHPendingBacklightRamp",R,N,V_pendingBacklightRamp) pendingBacklightRamp;
@property (T@"BLSBacklightSceneVisualState",R,N,V_visualState) visualState;
@property (T@"NSDate",R,N,V_presentationDate) presentationDate;
@property (TB,N,V_isFlipbook) isFlipbook;
@property (TB,N,V_hasExplicitFlipbook) hasExplicitFlipbook;
@property (TQ,N,V_lowPowerRenderingPresentationTime) lowPowerRenderingPresentationTime;
@property (Tq,V_backlightState) backlightState;
@property (TB,V_didUpdateInitialState) didUpdateInitialState;
@property (TB,V_didCompleteAnimation) didCompleteAnimation;
```

## Instance methods

```
-[BLSHEnvironmentTransitionStateTarget triggerEvent];
-[BLSHEnvironmentTransitionStateTarget setBacklightState:];
-[BLSHEnvironmentTransitionStateTarget visualState];
-[BLSHEnvironmentTransitionStateTarget hasExplicitFlipbook];
-[BLSHEnvironmentTransitionStateTarget isEqualToVisualState:presentationDate:];
-[BLSHEnvironmentTransitionStateTarget debugDescription];
-[BLSHEnvironmentTransitionStateTarget isFlipbook];
-[BLSHEnvironmentTransitionStateTarget initWithSequenceID:backlightState:visualState:presentationDate:triggerEvent:pendingBacklightRamp:];
-[BLSHEnvironmentTransitionStateTarget didUpdateInitialState];
-[BLSHEnvironmentTransitionStateTarget setHasExplicitFlipbook:];
-[BLSHEnvironmentTransitionStateTarget setLowPowerRenderingPresentationTime:];
-[BLSHEnvironmentTransitionStateTarget initWithTarget:visualState:presentationDate:];
-[BLSHEnvironmentTransitionStateTarget initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:forIdentifier:displayLoggingName:previousTarget:];
-[BLSHEnvironmentTransitionStateTarget initWithTarget:visualState:presentationDate:isFlipbook:hasExplicitFlipbook:];
-[BLSHEnvironmentTransitionStateTarget didCompleteAnimation];
-[BLSHEnvironmentTransitionStateTarget pendingBacklightRamp];
-[BLSHEnvironmentTransitionStateTarget backlightState];
-[BLSHEnvironmentTransitionStateTarget setIsFlipbook:];
-[BLSHEnvironmentTransitionStateTarget hash];
-[BLSHEnvironmentTransitionStateTarget description];
-[BLSHEnvironmentTransitionStateTarget presentationDate];
-[BLSHEnvironmentTransitionStateTarget sequenceID];
-[BLSHEnvironmentTransitionStateTarget setDidCompleteAnimation:];
-[BLSHEnvironmentTransitionStateTarget isEqual:];
-[BLSHEnvironmentTransitionStateTarget setDidUpdateInitialState:];
-[BLSHEnvironmentTransitionStateTarget lowPowerRenderingPresentationTime];
```
