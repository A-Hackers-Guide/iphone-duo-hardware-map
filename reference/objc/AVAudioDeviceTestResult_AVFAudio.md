# `AVAudioDeviceTestResult`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
q _inputID;
q _outputID;
@"NSData" _data;
d _sampleRate;
d _correlationValue;
```

## Properties

```
@property (Tq,N,V_outputID) outputID;
@property (Tq,N,V_inputID) inputID;
@property (Td,N,V_sampleRate) sampleRate;
@property (Td,N,V_correlationValue) correlationValue;
@property (T@"NSData",R,N,V_data) data;
```

## Class methods

```
+[AVAudioDeviceTestResult supportsSecureCoding];
```

## Instance methods

```
-[AVAudioDeviceTestResult sampleRate];
-[AVAudioDeviceTestResult data];
-[AVAudioDeviceTestResult setSampleRate:];
-[AVAudioDeviceTestResult encodeWithCoder:];
-[AVAudioDeviceTestResult initWithCoder:];
-[AVAudioDeviceTestResult inputID];
-[AVAudioDeviceTestResult correlationValue];
-[AVAudioDeviceTestResult initWithData:inputID:outputID:sampleRate:correlationValue:];
-[AVAudioDeviceTestResult outputID];
-[AVAudioDeviceTestResult setCorrelationValue:];
-[AVAudioDeviceTestResult setInputID:];
-[AVAudioDeviceTestResult setOutputID:];
```
