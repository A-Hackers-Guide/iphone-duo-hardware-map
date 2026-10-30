# `CTAudioCodecInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 21 instance methods, 1 class methods

## Instance variables

```
Q _callId;
q _codec;
Q _amrMode;
q _evsBandwidth;
q _evsBitrate;
Q _sampleRate;
Q _i2SClockRate;
```

## Properties

```
@property (TQ,N,V_callId) callId;
@property (Tq,N,V_codec) codec;
@property (TQ,N,V_amrMode) amrMode;
@property (Tq,N,V_evsBandwidth) evsBandwidth;
@property (Tq,N,V_evsBitrate) evsBitrate;
@property (TQ,N,V_sampleRate) sampleRate;
@property (TQ,N,V_i2SClockRate) i2SClockRate;
```

## Class methods

```
+[CTAudioCodecInfo supportsSecureCoding];
```

## Instance methods

```
-[CTAudioCodecInfo sampleRate];
-[CTAudioCodecInfo codec];
-[CTAudioCodecInfo init];
-[CTAudioCodecInfo setSampleRate:];
-[CTAudioCodecInfo encodeWithCoder:];
-[CTAudioCodecInfo description];
-[CTAudioCodecInfo initWithCoder:];
-[CTAudioCodecInfo setCodec:];
-[CTAudioCodecInfo copyWithZone:];
-[CTAudioCodecInfo amrMode];
-[CTAudioCodecInfo callId];
-[CTAudioCodecInfo evsBandwidth];
-[CTAudioCodecInfo evsBitrate];
-[CTAudioCodecInfo i2SClockRate];
-[CTAudioCodecInfo initWithCallId:codec:amrMode:evsBandwidth:evsBitrate:];
-[CTAudioCodecInfo initWithCallId:codec:amrMode:evsBandwidth:evsBitrate:sampleRate:i2SClockRate:];
-[CTAudioCodecInfo setAmrMode:];
-[CTAudioCodecInfo setCallId:];
-[CTAudioCodecInfo setEvsBandwidth:];
-[CTAudioCodecInfo setEvsBitrate:];
-[CTAudioCodecInfo setI2SClockRate:];
```
