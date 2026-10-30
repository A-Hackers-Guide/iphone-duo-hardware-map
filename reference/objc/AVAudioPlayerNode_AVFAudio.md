# `AVAudioPlayerNode`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioNode`
- Protocols: `AVAudioMixing`
- 0 instance variables, 6 properties, 21 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisPlaying) playing;
@property (Tf,D,N) volume;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVAudioPlayerNode pause];
-[AVAudioPlayerNode play];
-[AVAudioPlayerNode init];
-[AVAudioPlayerNode stop];
-[AVAudioPlayerNode isPlaying];
-[AVAudioPlayerNode playAtTime:];
-[AVAudioPlayerNode scheduleBuffer:atTime:options:completionHandler:];
-[AVAudioPlayerNode scheduleFile:atTime:completionHandler:];
-[AVAudioPlayerNode playAndReturnError:];
-[AVAudioPlayerNode prepareWithFrameCount:];
-[AVAudioPlayerNode scheduleBuffer:completionHandler:];
-[AVAudioPlayerNode scheduleFile:atTime:completionCallbackType:completionHandler:];
-[AVAudioPlayerNode callLegacyCompletionHandlerForType:legacyHandler:];
-[AVAudioPlayerNode didAttachToEngine:];
-[AVAudioPlayerNode nodeTimeForPlayerTime:];
-[AVAudioPlayerNode playAtTime:error:];
-[AVAudioPlayerNode playerTimeForNodeTime:];
-[AVAudioPlayerNode scheduleBuffer:atTime:options:completionCallbackType:completionHandler:];
-[AVAudioPlayerNode scheduleBuffer:completionCallbackType:completionHandler:];
-[AVAudioPlayerNode scheduleSegment:startingFrame:frameCount:atTime:completionCallbackType:completionHandler:];
-[AVAudioPlayerNode scheduleSegment:startingFrame:frameCount:atTime:completionHandler:];
```
