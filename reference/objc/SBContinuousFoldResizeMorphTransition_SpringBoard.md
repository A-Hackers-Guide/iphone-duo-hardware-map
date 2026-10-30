# `SBContinuousFoldResizeMorphTransition`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _relayoutDone;
@"SBAppLayout" _appLayout;
q _state;
@"NSString" _bundleIdentifier;
@"NSString" _sceneIdentifier;
@ _capturedContents;
@"SBResizeMorphSideRecord" _liveRecord;
@"SBResizeMorphSideRecord" _portaledRecord;
Q _generation;
d _blurInStartTime;
{CGSize="width"d"height"d} _captureSize;
```

## Properties

```
@property (T@"SBAppLayout",&,N,V_appLayout) appLayout;
@property (Tq,N,V_state) state;
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",C,N,V_sceneIdentifier) sceneIdentifier;
@property (T@,&,N,V_capturedContents) capturedContents;
@property (T{CGSize=dd},N,V_captureSize) captureSize;
@property (T@"SBResizeMorphSideRecord",&,N,V_liveRecord) liveRecord;
@property (T@"SBResizeMorphSideRecord",&,N,V_portaledRecord) portaledRecord;
@property (TQ,N,V_generation) generation;
@property (TB,N,V_relayoutDone) relayoutDone;
@property (Td,N,V_blurInStartTime) blurInStartTime;
```

## Instance methods

```
-[SBContinuousFoldResizeMorphTransition setState:];
-[SBContinuousFoldResizeMorphTransition setGeneration:];
-[SBContinuousFoldResizeMorphTransition init];
-[SBContinuousFoldResizeMorphTransition setAppLayout:];
-[SBContinuousFoldResizeMorphTransition appLayout];
-[SBContinuousFoldResizeMorphTransition bundleIdentifier];
-[SBContinuousFoldResizeMorphTransition setSceneIdentifier:];
-[SBContinuousFoldResizeMorphTransition sceneIdentifier];
-[SBContinuousFoldResizeMorphTransition generation];
-[SBContinuousFoldResizeMorphTransition setBundleIdentifier:];
-[SBContinuousFoldResizeMorphTransition state];
-[SBContinuousFoldResizeMorphTransition blurInStartTime];
-[SBContinuousFoldResizeMorphTransition setCaptureSize:];
-[SBContinuousFoldResizeMorphTransition captureSize];
-[SBContinuousFoldResizeMorphTransition capturedContents];
-[SBContinuousFoldResizeMorphTransition liveRecord];
-[SBContinuousFoldResizeMorphTransition portaledRecord];
-[SBContinuousFoldResizeMorphTransition recordForSide:];
-[SBContinuousFoldResizeMorphTransition relayoutDone];
-[SBContinuousFoldResizeMorphTransition setBlurInStartTime:];
-[SBContinuousFoldResizeMorphTransition setCapturedContents:];
-[SBContinuousFoldResizeMorphTransition setLiveRecord:];
-[SBContinuousFoldResizeMorphTransition setPortaledRecord:];
-[SBContinuousFoldResizeMorphTransition setRelayoutDone:];
```
