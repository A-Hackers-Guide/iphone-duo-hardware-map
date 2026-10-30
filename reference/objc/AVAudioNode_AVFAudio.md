# `AVAudioNode`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 8 properties, 50 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (T^v,R,N) impl;
@property (T@"AVAudioEngine",R,N) engine;
@property (TQ,R,N) numberOfInputs;
@property (TQ,R,N) numberOfOutputs;
@property (T@"AVAudioTime",R,N) lastRenderTime;
@property (T@"AUAudioUnit",R,N) AUAudioUnit;
@property (Td,R,N) latency;
@property (Td,R,N) outputPresentationLatency;
```

## Instance methods

```
-[AVAudioNode pan];
-[AVAudioNode clock];
-[AVAudioNode impl];
-[AVAudioNode rate];
-[AVAudioNode engine];
-[AVAudioNode initWithImpl:];
-[AVAudioNode position];
-[AVAudioNode latency];
-[AVAudioNode volume];
-[AVAudioNode init];
-[AVAudioNode dealloc];
-[AVAudioNode reset];
-[AVAudioNode setVolume:];
-[AVAudioNode setRate:];
-[AVAudioNode lock];
-[AVAudioNode setPosition:];
-[AVAudioNode setPan:];
-[AVAudioNode audioUnit];
-[AVAudioNode setSourceMode:];
-[AVAudioNode sourceMode];
-[AVAudioNode occlusion];
-[AVAudioNode removeTapOnBus:];
-[AVAudioNode inputFormatForBus:];
-[AVAudioNode numberOfOutputs];
-[AVAudioNode numberOfInputs];
-[AVAudioNode setObstruction:];
-[AVAudioNode setReverbBlend:];
-[AVAudioNode installTapOnBus:bufferSize:format:block:];
-[AVAudioNode obstruction];
-[AVAudioNode pointSourceInHeadMode];
-[AVAudioNode renderingAlgorithm];
-[AVAudioNode reverbBlend];
-[AVAudioNode setOcclusion:];
-[AVAudioNode setPointSourceInHeadMode:];
-[AVAudioNode setRenderingAlgorithm:];
-[AVAudioNode outputFormatForBus:];
-[AVAudioNode AUAudioUnit];
-[AVAudioNode destinationForMixer:bus:];
-[AVAudioNode didAttachToEngine:];
-[AVAudioNode didDetachFromEngine:error:];
-[AVAudioNode installTapOnBus:bufferSize:format:error:block:];
-[AVAudioNode lastRenderTime];
-[AVAudioNode nameForInputBus:];
-[AVAudioNode nameForOutputBus:];
-[AVAudioNode outputPresentationLatency];
-[AVAudioNode resetImpl:];
-[AVAudioNode setInputFormat:forBus:error:];
-[AVAudioNode setNumberOfInputs:];
-[AVAudioNode setNumberOfOutputs:];
-[AVAudioNode setOutputFormat:forBus:error:];
```
