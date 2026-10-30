# `AVAudioSettingsValueConstrainer`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _inputASBD;
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _outputASBD;
^{OpaqueAudioConverter=} _audioConverter;
I _outputDataRate;
B _needNewConverter;
B _needAvailableSampleRates;
B _needApplicableParameters;
@"NSArray" _availableOutputSampleRates;
@"NSMutableArray" _availableOutputDataRates;
@"NSMutableArray" _applicableOutputSampleRatesForDataRate;
@"NSMutableArray" _applicableOutputDataRatesForSampleRate;
```

## Properties

```
@property (Tf,N) outputSampleRate;
@property (TI,N) outputFormat;
@property (TI,N) outputFormatFlags;
@property (TI,N) outputBitsPerChannel;
@property (TI,N) outputChannelCount;
@property (TI,N) outputDataRate;
```

## Instance methods

```
-[AVAudioSettingsValueConstrainer setOutputFormat:];
-[AVAudioSettingsValueConstrainer init];
-[AVAudioSettingsValueConstrainer dealloc];
-[AVAudioSettingsValueConstrainer outputFormat];
-[AVAudioSettingsValueConstrainer _fetchApplicableOutputDataRates];
-[AVAudioSettingsValueConstrainer _bringUpToDate];
-[AVAudioSettingsValueConstrainer _buildApplicableDataRatesForSampleRates];
-[AVAudioSettingsValueConstrainer _buildAudioConverter];
-[AVAudioSettingsValueConstrainer _buildAvailableSampleRates];
-[AVAudioSettingsValueConstrainer _getAvailableOutputSampleRateFor:rounding:];
-[AVAudioSettingsValueConstrainer applicableOutputSampleRateForDesiredSampleRate:rounding:];
-[AVAudioSettingsValueConstrainer availableOutputChannelCountForDesiredChannelCount:rounding:];
-[AVAudioSettingsValueConstrainer outputBitsPerChannel];
-[AVAudioSettingsValueConstrainer outputChannelCount];
-[AVAudioSettingsValueConstrainer outputDataRate];
-[AVAudioSettingsValueConstrainer outputFormatFlags];
-[AVAudioSettingsValueConstrainer outputSampleRate];
-[AVAudioSettingsValueConstrainer setInputPropertiesFromASBD:];
-[AVAudioSettingsValueConstrainer setOutputBitsPerChannel:];
-[AVAudioSettingsValueConstrainer setOutputChannelCount:];
-[AVAudioSettingsValueConstrainer setOutputDataRate:];
-[AVAudioSettingsValueConstrainer setOutputFormatFlags:];
-[AVAudioSettingsValueConstrainer setOutputSampleRate:];
```
