# `HalogenAudio`

- Image: [`/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`](../userland/System__Library__PrivateFrameworks__IOAccessoryManager.framework__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 23 instance methods, 0 class methods

## Instance variables

```
i _nInputChannels;
i _nOutputChannels;
i _sampleRate;
i _bitDepth;
i _inputFrameSizeInBytes;
i _outputFrameSizeInBytes;
@"<HalogenAudioDelegate>" _halogenUnitDelegate;
^{OpaqueAudioComponentInstance=} _audioComponentInst;
```

## Properties

```
@property (T^{OpaqueAudioComponentInstance=},V_audioComponentInst) audioComponentInst;
@property (Ti,V_nInputChannels) nInputChannels;
@property (Ti,V_nOutputChannels) nOutputChannels;
@property (Ti,V_sampleRate) sampleRate;
@property (Ti,V_bitDepth) bitDepth;
@property (Ti,V_inputFrameSizeInBytes) inputFrameSizeInBytes;
@property (Ti,V_outputFrameSizeInBytes) outputFrameSizeInBytes;
@property (T@"<HalogenAudioDelegate>",&,N,V_halogenUnitDelegate) halogenUnitDelegate;
```

## Instance methods

```
-[HalogenAudio sampleRate];
-[HalogenAudio bitDepth];
-[HalogenAudio dealloc];
-[HalogenAudio setSampleRate:];
-[HalogenAudio setBitDepth:];
-[HalogenAudio nOutputChannels];
-[HalogenAudio _deinitAudioInstance];
-[HalogenAudio audioComponentInst];
-[HalogenAudio getAudioComponentInstance];
-[HalogenAudio halogenUnitDelegate];
-[HalogenAudio initAudioWithParameters:nInputChannels:nOutputChannels:sampleRate:bitDepth:inputFrameSizeInBytes:outputFrameSizeInBytes:];
-[HalogenAudio inputFrameSizeInBytes];
-[HalogenAudio nInputChannels];
-[HalogenAudio outputFrameSizeInBytes];
-[HalogenAudio releaseAudioUnitInstance];
-[HalogenAudio setAudioComponentInst:];
-[HalogenAudio setHalogenUnitDelegate:];
-[HalogenAudio setInputFrameSizeInBytes:];
-[HalogenAudio setNInputChannels:];
-[HalogenAudio setNOutputChannels:];
-[HalogenAudio setOutputFrameSizeInBytes:];
-[HalogenAudio startAudioUnit];
-[HalogenAudio stopAudioUnit];
```
