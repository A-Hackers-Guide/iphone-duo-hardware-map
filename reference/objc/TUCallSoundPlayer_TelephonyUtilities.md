# `TUCallSoundPlayer`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
q _currentlyPlayingSoundType;
@"TUSoundPlayer" _player;
```

## Properties

```
@property (T@"TUSoundPlayer",&,N,V_player) player;
@property (Tq,N,V_currentlyPlayingSoundType) currentlyPlayingSoundType;
@property (TB,R,N,GisPlaying) playing;
```

## Instance methods

```
-[TUCallSoundPlayer player];
-[TUCallSoundPlayer init];
-[TUCallSoundPlayer dealloc];
-[TUCallSoundPlayer isPlaying];
-[TUCallSoundPlayer setPlayer:];
-[TUCallSoundPlayer attemptToPlaySoundType:forCall:];
-[TUCallSoundPlayer attemptToPlayDescriptor:];
-[TUCallSoundPlayer attemptToPlayDescriptor:completion:];
-[TUCallSoundPlayer attemptToPlaySoundType:forCall:completion:];
-[TUCallSoundPlayer currentlyPlayingSoundType];
-[TUCallSoundPlayer setCurrentlyPlayingSoundType:];
-[TUCallSoundPlayer stopPlaying];
```
