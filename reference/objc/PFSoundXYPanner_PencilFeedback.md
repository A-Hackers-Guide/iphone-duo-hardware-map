# `PFSoundXYPanner`

- Image: [`/System/Library/PrivateFrameworks/PencilFeedback.framework/PencilFeedback`](../userland/System__Library__PrivateFrameworks__PencilFeedback.framework__PencilFeedback.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"AVAudioFormat" _outputFormat;
@"PFQuadPanAudioUnit" _quadPannerAU;
@"AVAudioMixerNode" _stereoMixer;
```

## Properties

```
@property (T@"PFQuadPanAudioUnit",R,N,V_quadPannerAU) quadPannerAU;
@property (T@"AVAudioMixerNode",R,N,V_stereoMixer) stereoMixer;
@property (T@"AVAudioNode",R,N) audioNode;
@property (T@"AVAudioFormat",R,N,V_outputFormat) outputFormat;
```

## Instance methods

```
-[PFSoundXYPanner outputFormat];
-[PFSoundXYPanner audioNode];
-[PFSoundXYPanner initWithCustomAU:];
-[PFSoundXYPanner quadPannerAU];
-[PFSoundXYPanner setPanPositionX:Y:];
-[PFSoundXYPanner stereoMixer];
```
