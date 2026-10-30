# `CHHapticAdvancedPatternPlayer` (protocol)

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `CHHapticPatternPlayer`
- 0 instance variables, 5 properties, 13 instance methods, 0 class methods

## Properties

```
@property (TB) loopEnabled;
@property (Td) loopEnd;
@property (Tf) playbackRate;
@property (TB) isMuted;
@property (T@?,C) completionHandler;
```

## Instance methods

```
-[CHHapticAdvancedPatternPlayer resumeAtTime:error:];
-[CHHapticAdvancedPatternPlayer isMuted];
-[CHHapticAdvancedPatternPlayer loopEnd];
-[CHHapticAdvancedPatternPlayer setPlaybackRate:];
-[CHHapticAdvancedPatternPlayer pauseAtTime:error:];
-[CHHapticAdvancedPatternPlayer playbackRate];
-[CHHapticAdvancedPatternPlayer seekToOffset:error:];
-[CHHapticAdvancedPatternPlayer setCompletionHandler:];
-[CHHapticAdvancedPatternPlayer setLoopEnd:];
-[CHHapticAdvancedPatternPlayer completionHandler];
-[CHHapticAdvancedPatternPlayer setIsMuted:];
-[CHHapticAdvancedPatternPlayer loopEnabled];
-[CHHapticAdvancedPatternPlayer setLoopEnabled:];
```
