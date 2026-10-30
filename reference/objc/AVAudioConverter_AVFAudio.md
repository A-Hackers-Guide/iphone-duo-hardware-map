# `AVAudioConverter`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 21 properties, 39 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (Tq,N) bitRate;
@property (T@"NSString",&,N) bitRateStrategy;
@property (Tq,R,N) maximumOutputPacketSize;
@property (T@"NSArray",R,N) availableEncodeBitRates;
@property (T@"NSArray",R,N) applicableEncodeBitRates;
@property (T@"NSArray",R,N) availableEncodeSampleRates;
@property (T@"NSArray",R,N) applicableEncodeSampleRates;
@property (T@"NSArray",R,N) availableEncodeChannelLayoutTags;
@property (T@"AVAudioFormat",R,N) inputFormat;
@property (T@"AVAudioFormat",R,N) outputFormat;
@property (T@"NSArray",&,N) channelMap;
@property (T@"NSData",&,N) magicCookie;
@property (TB,N) downmix;
@property (TB,N) dither;
@property (Tq,N) sampleRateConverterQuality;
@property (T@"NSString",&,N) sampleRateConverterAlgorithm;
@property (Tq,N) primeMethod;
@property (T{AVAudioConverterPrimeInfo=II},N) primeInfo;
@property (Tq,N) audioSyncPacketFrequency;
@property (Tq,N) contentSource;
@property (Tq,N) dynamicRangeControlConfiguration;
```

## Instance methods

```
-[AVAudioConverter inputFormat];
-[AVAudioConverter dealloc];
-[AVAudioConverter reset];
-[AVAudioConverter setContentSource:];
-[AVAudioConverter magicCookie];
-[AVAudioConverter setMagicCookie:];
-[AVAudioConverter outputFormat];
-[AVAudioConverter contentSource];
-[AVAudioConverter channelMap];
-[AVAudioConverter setChannelMap:];
-[AVAudioConverter dither];
-[AVAudioConverter setDither:];
-[AVAudioConverter convertToBuffer:error:withInputFromBlock:];
-[AVAudioConverter initFromFormat:toFormat:];
-[AVAudioConverter maximumOutputPacketSize];
-[AVAudioConverter bitRate];
-[AVAudioConverter setBitRate:];
-[AVAudioConverter convertToBuffer:fromBuffer:error:];
-[AVAudioConverter setSampleRateConverterQuality:];
-[AVAudioConverter bitRateStrategy];
-[AVAudioConverter downmix];
-[AVAudioConverter setPrimeMethod:];
-[AVAudioConverter applicableEncodeBitRates];
-[AVAudioConverter applicableEncodeSampleRates];
-[AVAudioConverter audioSyncPacketFrequency];
-[AVAudioConverter availableEncodeBitRates];
-[AVAudioConverter availableEncodeChannelLayoutTags];
-[AVAudioConverter availableEncodeSampleRates];
-[AVAudioConverter dynamicRangeControlConfiguration];
-[AVAudioConverter primeInfo];
-[AVAudioConverter primeMethod];
-[AVAudioConverter sampleRateConverterAlgorithm];
-[AVAudioConverter sampleRateConverterQuality];
-[AVAudioConverter setAudioSyncPacketFrequency:];
-[AVAudioConverter setBitRateStrategy:];
-[AVAudioConverter setDownmix:];
-[AVAudioConverter setDynamicRangeControlConfiguration:];
-[AVAudioConverter setPrimeInfo:];
-[AVAudioConverter setSampleRateConverterAlgorithm:];
```
