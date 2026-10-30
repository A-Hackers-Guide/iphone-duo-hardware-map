# `PNPSyntheticPencilInteractionEventSource`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PNPPencilInteractionEventSource`
- 3 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _playing;
B _cancelled;
@"<PNPPencilInteractionEventDestination>" eventDestination;
```

## Properties

```
@property (T@"NSArray",R,N) playlist;
@property (T@"<PNPPencilInteractionEventDestination>",W,N,VeventDestination) eventDestination;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PNPSyntheticPencilInteractionEventSource play];
-[PNPSyntheticPencilInteractionEventSource stop];
-[PNPSyntheticPencilInteractionEventSource isPlaying];
-[PNPSyntheticPencilInteractionEventSource playlist];
-[PNPSyntheticPencilInteractionEventSource _playEventAtPlayheadPosition:];
-[PNPSyntheticPencilInteractionEventSource _playlistPositionForPosition:];
-[PNPSyntheticPencilInteractionEventSource _terminalEventsForPlayhead];
-[PNPSyntheticPencilInteractionEventSource eventDestination];
-[PNPSyntheticPencilInteractionEventSource setEventDestination:];
```
