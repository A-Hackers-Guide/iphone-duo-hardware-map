# `AVAudioSecureSession`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioSecureSessionProtocol`
- 1 instance variables, 14 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"AVAudioSession" _innerSession;
```

## Properties

```
@property (T@"AVAudioSession",&,N,V_innerSession) _innerSession;
@property (T@"NSArray",R) availableCategories;
@property (T@"NSArray",R) availableModes;
@property (T@"NSString",R) category;
@property (T@"NSString",R) mode;
@property (Td,R) inputSampleRate;
@property (Td,R) IOBufferDuration;
@property (TQ,R) IOBufferFrameSize;
@property (Td,R) inputLatency;
@property (TB,R,N) prefersAggressiveEchoCancellation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVAudioSecureSession availableModes];
-[AVAudioSecureSession category];
-[AVAudioSecureSession inputLatency];
-[AVAudioSecureSession mode];
-[AVAudioSecureSession setCategory:error:];
-[AVAudioSecureSession setActive:error:];
-[AVAudioSecureSession initWithUseCaseIdentifier:];
-[AVAudioSecureSession IOBufferFrameSize];
-[AVAudioSecureSession setCategory:mode:options:error:];
-[AVAudioSecureSession IOBufferDuration];
-[AVAudioSecureSession initWithIsolatedAudioUseCaseID:];
-[AVAudioSecureSession inputSampleRate];
-[AVAudioSecureSession _innerSession];
-[AVAudioSecureSession availableCategories];
-[AVAudioSecureSession prefersAggressiveEchoCancellation];
-[AVAudioSecureSession setPrefersAggressiveEchoCancellation:error:];
-[AVAudioSecureSession set_innerSession:];
```
