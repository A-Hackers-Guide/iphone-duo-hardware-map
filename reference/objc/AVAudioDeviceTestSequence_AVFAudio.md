# `AVAudioDeviceTestSequence`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 15 instance variables, 15 properties, 33 instance methods, 1 class methods

## Instance variables

```
B _calculateCrossCorrelationPeak;
B _parallelCrossCorrelationCalculation;
B _requiresBluetoothOutput;
B _processSequenceAsynchronously;
f _volume;
q _outputID;
@"NSURL" _stimulusURL;
@"AVAudioDeviceTestProcessingChain" _inputProcessingChain;
@"AVAudioDeviceTestProcessingChain" _outputProcessingChain;
q _outputMode;
q _priority;
@"NSString" _mode;
q _numberOfChannels;
@"NSArray" _micBufferNumbers;
@"NSString" _microphone;
```

## Properties

```
@property (TB,V_processSequenceAsynchronously) processSequenceAsynchronously;
@property (Tq,N,V_outputID) outputID;
@property (Tf,N,V_volume) volume;
@property (T@"NSURL",&,N,V_stimulusURL) stimulusURL;
@property (T@"AVAudioDeviceTestProcessingChain",&,N,V_inputProcessingChain) inputProcessingChain;
@property (T@"AVAudioDeviceTestProcessingChain",&,N,V_outputProcessingChain) outputProcessingChain;
@property (Tq,N,V_outputMode) outputMode;
@property (Tq,N,V_priority) priority;
@property (T@"NSString",&,V_mode) mode;
@property (TB,V_calculateCrossCorrelationPeak) calculateCrossCorrelationPeak;
@property (TB,V_parallelCrossCorrelationCalculation) parallelCrossCorrelationCalculation;
@property (Tq,N,V_numberOfChannels) numberOfChannels;
@property (T@"NSArray",&,N,V_micBufferNumbers) micBufferNumbers;
@property (TB,V_requiresBluetoothOutput) requiresBluetoothOutput;
@property (T@"NSString",&,N,V_microphone) microphone;
```

## Class methods

```
+[AVAudioDeviceTestSequence supportsSecureCoding];
```

## Instance methods

```
-[AVAudioDeviceTestSequence priority];
-[AVAudioDeviceTestSequence volume];
-[AVAudioDeviceTestSequence init];
-[AVAudioDeviceTestSequence setPriority:];
-[AVAudioDeviceTestSequence setVolume:];
-[AVAudioDeviceTestSequence setMode:];
-[AVAudioDeviceTestSequence encodeWithCoder:];
-[AVAudioDeviceTestSequence mode];
-[AVAudioDeviceTestSequence initWithCoder:];
-[AVAudioDeviceTestSequence outputMode];
-[AVAudioDeviceTestSequence setOutputMode:];
-[AVAudioDeviceTestSequence numberOfChannels];
-[AVAudioDeviceTestSequence microphone];
-[AVAudioDeviceTestSequence setMicrophone:];
-[AVAudioDeviceTestSequence setStimulusURL:];
-[AVAudioDeviceTestSequence calculateCrossCorrelationPeak];
-[AVAudioDeviceTestSequence inputProcessingChain];
-[AVAudioDeviceTestSequence micBufferNumbers];
-[AVAudioDeviceTestSequence outputID];
-[AVAudioDeviceTestSequence outputProcessingChain];
-[AVAudioDeviceTestSequence parallelCrossCorrelationCalculation];
-[AVAudioDeviceTestSequence processSequenceAsynchronously];
-[AVAudioDeviceTestSequence requiresBluetoothOutput];
-[AVAudioDeviceTestSequence setCalculateCrossCorrelationPeak:];
-[AVAudioDeviceTestSequence setInputProcessingChain:];
-[AVAudioDeviceTestSequence setMicBufferNumbers:];
-[AVAudioDeviceTestSequence setNumberOfChannels:];
-[AVAudioDeviceTestSequence setOutputID:];
-[AVAudioDeviceTestSequence setOutputProcessingChain:];
-[AVAudioDeviceTestSequence setParallelCrossCorrelationCalculation:];
-[AVAudioDeviceTestSequence setProcessSequenceAsynchronously:];
-[AVAudioDeviceTestSequence setRequiresBluetoothOutput:];
-[AVAudioDeviceTestSequence stimulusURL];
```
