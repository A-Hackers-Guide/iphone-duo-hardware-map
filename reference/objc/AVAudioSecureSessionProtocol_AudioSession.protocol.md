# `AVAudioSecureSessionProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 9 properties, 13 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",R) availableCategories;
@property (T@"NSArray",R) availableModes;
@property (T@"NSString",R) category;
@property (T@"NSString",R) mode;
@property (Td,R) inputSampleRate;
@property (Td,R) IOBufferDuration;
@property (TQ,R) IOBufferFrameSize;
@property (Td,R) inputLatency;
@property (TB,R,N) prefersAggressiveEchoCancellation;
```

## Instance methods

```
-[AVAudioSecureSessionProtocol availableModes];
-[AVAudioSecureSessionProtocol category];
-[AVAudioSecureSessionProtocol inputLatency];
-[AVAudioSecureSessionProtocol mode];
-[AVAudioSecureSessionProtocol setCategory:error:];
-[AVAudioSecureSessionProtocol setActive:error:];
-[AVAudioSecureSessionProtocol IOBufferFrameSize];
-[AVAudioSecureSessionProtocol setCategory:mode:options:error:];
-[AVAudioSecureSessionProtocol IOBufferDuration];
-[AVAudioSecureSessionProtocol inputSampleRate];
-[AVAudioSecureSessionProtocol availableCategories];
-[AVAudioSecureSessionProtocol prefersAggressiveEchoCancellation];
-[AVAudioSecureSessionProtocol setPrefersAggressiveEchoCancellation:error:];
```
