# `/System/Library/PrivateFrameworks/PencilFeedback.framework/PencilFeedback`

iOS 27.2 dyld shared cache image. Version `12.0.0.0.0`. **[DSC]**

## Linked libraries (11)

- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking`
- `/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`
- `/System/Library/Frameworks/AVFoundation.framework/AVFoundation`
- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/Frameworks/Accelerate.framework/Accelerate`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/AVFAudio.framework/AVFAudio`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 10 classes, 2 protocols, 294 methods, 92 properties

### Class pages

Every class and protocol, with its methods: [`NSObject`](../objc/NSObject_PencilFeedback.protocol.md), [`PFBezierMapping`](../objc/PFBezierMapping_PencilFeedback.md), [`PFPencilSoundManager`](../objc/PFPencilSoundManager_PencilFeedback.md), [`PFPencilSoundProfile`](../objc/PFPencilSoundProfile_PencilFeedback.md), [`PFPencilSoundProfileFactory`](../objc/PFPencilSoundProfileFactory_PencilFeedback.md), [`PFQuadPanAudioUnit`](../objc/PFQuadPanAudioUnit_PencilFeedback.md), [`PFQuadPanAudioUnitImpl`](../objc/PFQuadPanAudioUnitImpl_PencilFeedback.md), [`PFSoundGenerator`](../objc/PFSoundGenerator_PencilFeedback.protocol.md), [`PFSoundGeneratorAVAE`](../objc/PFSoundGeneratorAVAE_PencilFeedback.md), [`PFSoundGeneratorBase`](../objc/PFSoundGeneratorBase_PencilFeedback.md), [`PFSoundGeneratorPHASE`](../objc/PFSoundGeneratorPHASE_PencilFeedback.md), [`PFSoundXYPanner`](../objc/PFSoundXYPanner_PencilFeedback.md)

### Classes

`PFBezierMapping`, `PFPencilSoundManager`, `PFPencilSoundProfile`, `PFPencilSoundProfileFactory`, `PFQuadPanAudioUnit`, `PFQuadPanAudioUnitImpl`, `PFSoundGeneratorAVAE`, `PFSoundGeneratorBase`, `PFSoundGeneratorPHASE`, `PFSoundXYPanner`

### Protocols

`NSObject`, `PFSoundGenerator`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,N) currentVolumeState;
@property (Tf,N) outputVolume;
@property (TI,R,N) channelCount;
@property (Tf,N) strokeVolume;
@property (Tf,N) bandpassFrequency;
@property (Tf,N) bandwidth;
@property (Tf,N) highPassFrequency;
@property (Tf,N) lowPassFrequency;
@property (Tf,R,N) panHorizontal;
@property (Tf,R,N) panVertical;
@property (T{CGPoint=dd},N,V_controlPoint1) controlPoint1;
@property (T{CGPoint=dd},N,V_controlPoint2) controlPoint2;
@property (T{CGPoint=dd},N,V_controlPoint3) controlPoint3;
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
@property (Td,N,V_velocityFrequencyAddAmount) velocityFrequencyAddAmount;
@property (Td,N,V_baseBPFrequency) baseBPFrequency;
@property (Td,N,V_baseBPBandwidth) baseBPBandwidth;
@property (Td,N,V_baseHPFrequency) baseHPFrequency;
@property (Td,N,V_baseLPFrequency) baseLPFrequency;
@property (Td,N,V_directionFrequencyDeviation) directionFrequencyDeviation;
@property (Td,N,V_forceFrequencyDeviation) forceFrequencyDeviation;
@property (Td,N,V_fixedGain) fixedGain;
@property (Td,N,V_velocityRatio) velocityRatio;
@property (Tf,N,V_minThickness) minThickness;
@property (Tf,N,V_maxThickness) maxThickness;
@property (Tf,N,V_thicknessFrequencyRange) thicknessFrequencyRange;
@property (Tf,N,V_originalDirectionValue) originalDirectionValue;
@property (T{CGPoint=dd},N,V_controlPoint1) controlPoint1;
@property (T{CGPoint=dd},N,V_controlPoint2) controlPoint2;
@property (T{CGPoint=dd},N,V_controlPoint3) controlPoint3;
@property (T@"PFPencilSoundProfile",&,N,V_currentProfile) currentProfile;
@property (Tf,N) horizontalPan;
@property (Tf,N) verticalPan;
@property (Tq,N) algorithm;
@property (Tf,N,V_horizontalPan) horizontalPan;
@property (Tf,N,V_verticalPan) verticalPan;
@property (Tq,N,V_algorithm) algorithm;
@property (T@"AVAudioEngine",&,N,V_engine) engine;
@property (TB,N,V_isAudioActive) isAudioActive;
@property (T@"AVAudioSourceNode",&,N,V_noiseSourceNode) noiseSourceNode;
@property (T^{NoiseGenerator=},N,V_noiseGenerator) noiseGenerator;
@property (T@"AVAudioUnit",&,N,V_highPassFilter) highPassFilter;
@property (T@"AVAudioUnit",&,N,V_bandPassFilter) bandPassFilter;
@property (T@"AVAudioUnit",&,N,V_lowPassFilter) lowPassFilter;
@property (T@"AVAudioUnit",&,N,V_crossoverLowPassFilter) crossoverLowPassFilter;
@property (T@"AVAudioFormat",&,N,V_monoFormat) monoFormat;
@property (T@"PFSoundXYPanner",&,N,V_panner) panner;
@property (Tf,N,V_gainNormalizationDivisor) gainNormalizationDivisor;
@property (Tf,N,V_crossoverFrequency) crossoverFrequency;
@property (T@"AVAudioSession",&,N,V_auxiliarySession) auxiliarySession;
@property (Tq,N,V_currentVolumeState) currentVolumeState;
@property (Tf,N,V_outputVolume) outputVolume;
@property (TI,R,N,V_channelCount) channelCount;
@property (Tf,N,V_strokeVolume) strokeVolume;
@property (Tf,N,V_bandpassFrequency) bandpassFrequency;
@property (Tf,N,V_bandwidth) bandwidth;
@property (Tf,N,V_highPassFrequency) highPassFrequency;
@property (Tf,N,V_lowPassFrequency) lowPassFrequency;
@property (Tf,R,N,V_panHorizontal) panHorizontal;
@property (Tf,R,N,V_panVertical) panVertical;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"PHASEEngine",&,N,V_engine) engine;
@property (T@"PHASEDataBundleAsset",&,N,V_dataBundleAsset) dataBundleAsset;
@property (T@"PHASESoundEvent",&,N,V_soundEvent) soundEvent;
@property (TB,N,V_isAudioActive) isAudioActive;
@property (T@"PFQuadPanAudioUnit",R,N,V_quadPannerAU) quadPannerAU;
@property (T@"AVAudioMixerNode",R,N,V_stereoMixer) stereoMixer;
@property (T@"AVAudioNode",R,N) audioNode;
@property (T@"AVAudioFormat",R,N,V_outputFormat) outputFormat;
```

## Strings (125)

```
frames=%u paused=%d
NoiseRenderCallback
result=rendered amp=%.3f
vel=%.1f force=%.3f bufSize=%ld
ProcessTouchEnd
result=silence
force=%.3f altitude=%.3f azimuth=%.3f panX=%.3f panY=%.3f
ProcessTouchBegin
ProcessTouchMove
PHASESoundEvent
[PencilFeedback:%@][ERROR] readValueFromDefaults: nil value pointer for key '%@'
[PencilFeedback:%@] PFPencilSoundManager: Sound engine resume in foreground
internalSettings.pencilFeedback.gainNormalizationDivisor
[PencilFeedback:%@] PFSoundGeneratorBase: Audio buffer size: %.0f samples (%.2fms at %.0f Hz)
[PencilFeedback:%@] PFPencilSoundProfileFactory: Creating fountain pen profile
PencilSounds
[PencilFeedback:%@] PFPencilSoundManager: Initialized with PFSoundGeneratorAVAE
input.processing
i36@?0^B8r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}16I24^{AudioBufferList=I[1{AudioBuffer=II^v}]}28
[PencilFeedback:%@] PFPencilSoundManager: Idle timeout reached, pausing engine
f16@?0@\"AUParameter\"8
crossoverfreq
[PencilFeedback:%@] PFPencilSoundProfileFactory: Creating reed profile (same as fountain pen)
v20@?0@\"AUParameter\"8f16
[PencilFeedback:%@] PFPencilSoundManager: Idle timer started
[PencilFeedback:%@] PFPencilSoundProfileFactory: Creating crayon profile
[PencilFeedback:%@] PFPencilSoundProfileFactory: Creating eraser profile
Horizontal Pan
Pair-wise algorithm
Linear
[PencilFeedback:%@] PFSoundGeneratorAVAE: Pausing engine
[PencilFeedback:%@][ERROR] PFSoundGeneratorAVAE: Error deactivating audio session: %@
[PencilFeedback:%@] PFPencilSoundManager: Sound engine stopped
com.apple.pencilfeedback
phasebundle
[PencilFeedback:%@][ERROR] readValueFromDefaults: key '%@' not found or invalid type, using default value %f
Pencil
internalSettings.pencilFeedback.crossoverFrequency
com.apple.PencilFeedback
Monoline
[PencilFeedback:%@][ERROR] PFSoundGeneratorPHASE: Error starting audio engine: %@
PencilFeedback
[PencilFeedback:%@][ERROR] PFSoundGeneratorBase: Error setting up audio session: %@
[PencilFeedback:%@] PFSoundGeneratorPHASE: Resuming engine
internalSettings.pencilFeedback.horizontalSpreadFactor
[PencilFeedback:%@] PFSoundGeneratorAVAE: Resuming engine
highpassfreq
[PencilFeedback:%@][ERROR] PFSoundGeneratorPHASE: Error deactivating audio session: %@
[PencilFeedback:%@][ERROR] Failed to load pencil bundle: %@
[PencilFeedback:%@] PFPencilSoundManager: Idle timer cancelled
vector
[PencilFeedback:%@] PFSoundGeneratorPHASE: Stopping engine
Eraser
panY
com.apple.pencilkit.audio.processing
[PencilFeedback:%@] PFSoundGeneratorAVAE: Stopping sound
[PencilFeedback:%@][ERROR] Sound event failed to prepare. State: %ld
[PencilFeedback:%@] PFPencilSoundManager: Sound generation start with stroke
[PencilFeedback:%@] PFSoundGeneratorPHASE: Starting sound
[PencilFeedback:%@][ERROR] Sound event failed to start. Rendering state: %ld
Fountain Pen
bandpassfreq
[PencilFeedback:%@][ERROR] PFSoundGeneratorPHASE: Error resuming engine: %@
PencilBundle
internalSettings.pencilFeedback.verticalSpreadFactor
[PencilFeedback:%@] PFPencilSoundProfileFactory: Creating marker profile
[PencilFeedback:%@] PFPencilSoundProfileFactory: Unknown tool type encountered: %@
[PencilFeedback:%@][ERROR] ERROR: Filter parameters contain NaN values!
[PencilFeedback:%@] PFSoundGeneratorPHASE: Stopping sound
[PencilFeedback:%@] PFSoundGeneratorPHASE: Pausing engine
SystemUtils
[PencilFeedback:%@] PFPencilSoundManager: Sound generation stop with stroke
[PencilFeedback:%@] PFPencilSoundProfileFactory: profileForTool called with tool type: %@
verticalPan
i60@?0^I8r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}16I24q28^{AudioBufferList=I[1{AudioBuffer=II^v}]}36r^(AURenderEvent={AURenderEventHeader=^(AURenderEvent)qCC}{AUParameterEvent=^(AURenderEvent)qC[3C]IQf}{AUMIDIEvent=^(AURenderEvent)qCC
[PencilFeedback:%@] PFSoundGeneratorAVAE: Starting sound
[PencilFeedback:%@][ERROR] PFSoundGeneratorAVAE: Error reactivating audio session: %@
[PencilFeedback:%@] PFSoundGeneratorAVAE: Initializing audio engine with %i channels
PHASESoundGenerator
Sin Cos
audio.realtime
Unable to find class %s
[PencilFeedback:%@] PFPencilSoundProfileFactory: Creating pencil profile
horizontalPan
[PencilFeedback:%@] PFSoundGeneratorAVAE: Stopping engine
[PencilFeedback:%@][ERROR] PFSoundGeneratorAVAE: Error starting audio engine: %@
[PencilFeedback:%@] PFPencilSoundProfileFactory: Creating pen profile
panX
[PencilFeedback:%@][ERROR] Failed to find pencil.phasebundle resource
Marker
[PencilFeedback:%@] PFPencilSoundProfileFactory: Creating watercolor profile
smoothing
Unknown
Vertical Pan
v8@?0
lifecycle
q
Pen
[PencilFeedback:%@] PFPencilSoundProfileFactory: Creating monoline profile
AUQuadPanner
[PencilFeedback:%@][ERROR] PFSoundGeneratorBase: Error activating audio session: %@
lowpassfreq
%s
Crayon
[PencilFeedback:%@][ERROR] Failed to create sound event: %@
Reed
Unknown error
PHASEEngine
[PencilFeedback:%@][ERROR] PFSoundGeneratorAVAE: Error resuming engine: %@
[PencilFeedback:%@][ERROR] PFSoundGeneratorBase: Error setting preferred IO buffer duration: %@
Watercolor
bandwidth
[PencilFeedback:%@] PFSoundGeneratorPHASE: Initializing audio engine
databundle.json
[PencilFeedback:%@] PFPencilSoundManager: Initialized with PFSoundGeneratorPHASE
[PencilFeedback:%@] PFPencilSoundManager: Tool changed to: %@ (width: %.2f)
i
audio.parameters
[PencilFeedback:%@] PFPencilSoundManager: Sound engine pause in background
algorithm
Normalized
gain
[PencilFeedback:%@][ERROR] PFSoundGeneratorPHASE: Error reactivating audio session: %@
pencil
softlink:r:path:/System/Library/Frameworks/PHASE.framework/PHASE
```
