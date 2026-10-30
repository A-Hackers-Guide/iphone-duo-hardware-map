# `ExclaveAudioFormatBase`

- Image: [`/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`](../userland/System__Library__PrivateFrameworks__CoreAudioOrchestration.framework__CoreAudioOrchestration.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _sampleRate;
@"NSNumber" _channels;
@"NSNumber" _framesPerIO;
```

## Properties

```
@property (T@"NSNumber",R,N,V_sampleRate) sampleRate;
@property (T@"NSNumber",R,N,V_channels) channels;
@property (T@"NSNumber",R,N,V_framesPerIO) framesPerIO;
```

## Class methods

```
+[ExclaveAudioFormatBase createFrom:forUseCase:destination:error:];
```

## Instance methods

```
-[ExclaveAudioFormatBase sampleRate];
-[ExclaveAudioFormatBase channels];
-[ExclaveAudioFormatBase isEqual:];
-[ExclaveAudioFormatBase framesPerIO];
-[ExclaveAudioFormatBase initFormat:];
-[ExclaveAudioFormatBase initWithExclaveUseCaseFormat:];
-[ExclaveAudioFormatBase initWithSampleRate:andChannels:andFrameSize:];
```
