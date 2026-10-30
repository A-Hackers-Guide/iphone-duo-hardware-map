# `AVAudioEngine`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 13 properties, 54 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (T^{OpaqueMusicSequence=},N) musicSequence;
@property (T@"AVAudioOutputNode",R,N) outputNode;
@property (T@"AVAudioInputNode",R,N) inputNode;
@property (T@"AVAudioMixerNode",R,N) mainMixerNode;
@property (TB,R,N,GisRunning) running;
@property (TB,N,GisAutoShutdownEnabled) autoShutdownEnabled;
@property (T@"NSSet",R,C) attachedNodes;
@property (T@?,R,N) manualRenderingBlock;
@property (TB,R,N) isInManualRenderingMode;
@property (Tq,R,N) manualRenderingMode;
@property (T@"AVAudioFormat",R,N) manualRenderingFormat;
@property (TI,R,N) manualRenderingMaximumFrameCount;
@property (Tq,R,N) manualRenderingSampleTime;
```

## Instance methods

```
-[AVAudioEngine isRunning];
-[AVAudioEngine pause];
-[AVAudioEngine audioSession];
-[AVAudioEngine inputNode];
-[AVAudioEngine init];
-[AVAudioEngine stop];
-[AVAudioEngine dealloc];
-[AVAudioEngine reset];
-[AVAudioEngine manualRenderingMaximumFrameCount];
-[AVAudioEngine implementation];
-[AVAudioEngine manualRenderingFormat];
-[AVAudioEngine startAndReturnError:];
-[AVAudioEngine prepare];
-[AVAudioEngine setAudioSession:];
-[AVAudioEngine isAutoShutdownEnabled];
-[AVAudioEngine description];
-[AVAudioEngine lock];
-[AVAudioEngine setAutoShutdownEnabled:];
-[AVAudioEngine outputNode];
-[AVAudioEngine attachNode:];
-[AVAudioEngine connect:to:format:];
-[AVAudioEngine detachNode:];
-[AVAudioEngine disconnectNodeInput:];
-[AVAudioEngine disconnectNodeOutput:];
-[AVAudioEngine mainMixerNode];
-[AVAudioEngine connect:to:format:error:];
-[AVAudioEngine attachedNodes];
-[AVAudioEngine connect:to:fromBus:toBus:format:];
-[AVAudioEngine connect:to:fromBus:toBus:format:error:];
-[AVAudioEngine connect:toConnectionPoints:fromBus:format:];
-[AVAudioEngine connect:toConnectionPoints:fromBus:format:error:];
-[AVAudioEngine connectMIDI:to:format:block:];
-[AVAudioEngine connectMIDI:to:format:eventListBlock:];
-[AVAudioEngine connectMIDI:to:format:eventListProvider:];
-[AVAudioEngine connectMIDI:toNodes:format:block:];
-[AVAudioEngine connectMIDI:toNodes:format:eventListBlock:];
-[AVAudioEngine connectMIDI:toNodes:format:eventListProvider:];
-[AVAudioEngine disableManualRenderingMode];
-[AVAudioEngine disconnectMIDI:from:];
-[AVAudioEngine disconnectMIDI:fromNodes:];
-[AVAudioEngine disconnectMIDIInput:];
-[AVAudioEngine disconnectMIDIOutput:];
-[AVAudioEngine disconnectNodeInput:bus:];
-[AVAudioEngine disconnectNodeOutput:bus:];
-[AVAudioEngine enableManualRenderingMode:format:maximumFrameCount:error:];
-[AVAudioEngine inputConnectionPointForNode:inputBus:];
-[AVAudioEngine isInManualRenderingMode];
-[AVAudioEngine manualRenderingBlock];
-[AVAudioEngine manualRenderingMode];
-[AVAudioEngine manualRenderingSampleTime];
-[AVAudioEngine musicSequence];
-[AVAudioEngine outputConnectionPointsForNode:outputBus:];
-[AVAudioEngine renderOffline:toBuffer:error:];
-[AVAudioEngine setMusicSequence:];
```
