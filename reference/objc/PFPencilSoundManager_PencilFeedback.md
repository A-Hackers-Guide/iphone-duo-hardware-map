# `PFPencilSoundManager`

- Image: [`/System/Library/PrivateFrameworks/PencilFeedback.framework/PencilFeedback`](../userland/System__Library__PrivateFrameworks__PencilFeedback.framework__PencilFeedback.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 17 properties, 61 instance methods, 0 class methods

## Instance variables

```
{vector<PFInputPoint, std::allocator<PFInputPoint>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} touchBuffer;
B _useRoll;
B _useMagicNumbers;
f _normalizedPickerThickness;
f _horizontalSpread;
f _verticalSpread;
q _interfaceOrientation;
@"<PFSoundGenerator>" _soundGenerator;
@"NSObject<OS_dispatch_queue>" _audioQueue;
q _bufferSize;
@"PFPencilSoundProfileFactory" _profileFactory;
@"PFPencilSoundProfile" _currentProfile;
@"PFBezierMapping" _currentMapping;
@"<PFToolDescriptor>" _currentTool;
d _lastRoll;
d _currentAzimuth;
@"NSTimer" _idleTimer;
{?="bandpassFrequency"f"highpassFrequency"f"noiseVolume"f"bandwidth"f"fixedGain"f"lowpassFrequency"f"panH"f"panV"f"channel"i} _soundParameters;
```

## Properties

```
@property (T@"<PFSoundGenerator>",&,N,V_soundGenerator) soundGenerator;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_audioQueue) audioQueue;
@property (Tq,N,V_bufferSize) bufferSize;
@property (T@"PFPencilSoundProfileFactory",&,N,V_profileFactory) profileFactory;
@property (T@"PFPencilSoundProfile",&,N,V_currentProfile) currentProfile;
@property (T@"PFBezierMapping",&,N,V_currentMapping) currentMapping;
@property (T{?=ffffffffi},N,V_soundParameters) soundParameters;
@property (T@"<PFToolDescriptor>",&,N,V_currentTool) currentTool;
@property (Tf,N,V_normalizedPickerThickness) normalizedPickerThickness;
@property (Td,N,V_lastRoll) lastRoll;
@property (Td,N,V_currentAzimuth) currentAzimuth;
@property (TB,N,V_useRoll) useRoll;
@property (TB,N,V_useMagicNumbers) useMagicNumbers;
@property (Tf,N,V_horizontalSpread) horizontalSpread;
@property (Tf,N,V_verticalSpread) verticalSpread;
@property (T@"NSTimer",&,N,V_idleTimer) idleTimer;
@property (Tq,N,V_interfaceOrientation) interfaceOrientation;
```

## Instance methods

```
-[PFPencilSoundManager idleTimer];
-[PFPencilSoundManager interfaceOrientation];
-[PFPencilSoundManager setSoundGenerator:];
-[PFPencilSoundManager setIdleTimer:];
-[PFPencilSoundManager bufferSize];
-[PFPencilSoundManager setInterfaceOrientation:];
-[PFPencilSoundManager init];
-[PFPencilSoundManager soundGenerator];
-[PFPencilSoundManager dealloc];
-[PFPencilSoundManager cancelIdleTimer];
-[PFPencilSoundManager setBufferSize:];
-[PFPencilSoundManager audioQueue];
-[PFPencilSoundManager setAudioQueue:];
-[PFPencilSoundManager lastRoll];
-[PFPencilSoundManager setLastRoll:];
-[PFPencilSoundManager currentProfile];
-[PFPencilSoundManager setCurrentProfile:];
-[PFPencilSoundManager handleIdleTimeout];
-[PFPencilSoundManager startIdleTimer];
-[PFPencilSoundManager stopSound];
-[PFPencilSoundManager clamp:];
-[PFPencilSoundManager setCurrentTool:];
-[PFPencilSoundManager soundParameters];
-[PFPencilSoundManager useRoll];
-[PFPencilSoundManager stopSoundEngine];
-[PFPencilSoundManager useMagicNumbers];
-[PFPencilSoundManager addTouchToBuffer:];
-[PFPencilSoundManager clampRotation:];
-[PFPencilSoundManager computeAltitudeNorm:];
-[PFPencilSoundManager computeSmoothedDeltaRoll];
-[PFPencilSoundManager computeSmoothedDirection];
-[PFPencilSoundManager computeSmoothedForce];
-[PFPencilSoundManager computeSmoothedVelocity];
-[PFPencilSoundManager computeStrokeAzimuth];
-[PFPencilSoundManager computeStrokeVector];
-[PFPencilSoundManager currentAzimuth];
-[PFPencilSoundManager currentMapping];
-[PFPencilSoundManager currentTool];
-[PFPencilSoundManager horizontalSpread];
-[PFPencilSoundManager normalizedPickerThickness];
-[PFPencilSoundManager normalizedVector:];
-[PFPencilSoundManager pauseSoundEngine];
-[PFPencilSoundManager profileFactory];
-[PFPencilSoundManager resumeSoundEngine];
-[PFPencilSoundManager setCurrentAzimuth:];
-[PFPencilSoundManager setCurrentMapping:];
-[PFPencilSoundManager setHorizontalSpread:];
-[PFPencilSoundManager setNormalizedPickerThickness:];
-[PFPencilSoundManager setProfileFactory:];
-[PFPencilSoundManager setSoundParameters:];
-[PFPencilSoundManager setUseMagicNumbers:];
-[PFPencilSoundManager setUseRoll:];
-[PFPencilSoundManager setVerticalSpread:];
-[PFPencilSoundManager soundDidBeginAtPoint:panPosition:];
-[PFPencilSoundManager soundDidEnd];
-[PFPencilSoundManager soundDidMoveToPoint:panPosition:];
-[PFPencilSoundManager startSound];
-[PFPencilSoundManager toolDidChange:];
-[PFPencilSoundManager transformPanPosition:];
-[PFPencilSoundManager updateGeneratorWithVelocity:force:tool:direction:altitudeNorm:roll:panH:panV:];
-[PFPencilSoundManager verticalSpread];
```
