# `ATBlurMixer`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 4 properties, 26 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<OpaqueAudioComponentInstance, applesauce::raii::detail::opaque_deletion_functor<OpaqueAudioComponentInstance *, &AudioComponentInstanceDispose>>=""{?="__ptr_"^{OpaqueAudioComponentInstance}}} mAUDSPGraph;
{StreamDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} mStreamDescription;
I mMaxFrames;
{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}} mTuningDirectory;
B mIsInitialized;
f mBlurHoldTimeSec;
B mRemoteFeedbackFeatureEnabled;
B _isUplink;
```

## Properties

```
@property (TB,R,N,V_isUplink) isUplink;
@property (TB,N,GisBlurEnabled) enableBlur;
@property (Tf,N) blendTimeMs;
@property (T@?,R,N) processBlock;
```

## Instance methods

```
-[ATBlurMixer configure];
-[ATBlurMixer isBlurEnabled];
-[ATBlurMixer setFormat:];
-[ATBlurMixer processBlock];
-[ATBlurMixer isUplink];
-[ATBlurMixer audioUnit];
-[ATBlurMixer blurHoldTimeSec];
-[ATBlurMixer setupAU];
-[ATBlurMixer getDSPGraphPath];
-[ATBlurMixer setBlendTimeMs:];
-[ATBlurMixer blendTimeMs];
-[ATBlurMixer getAUStripPath];
-[ATBlurMixer getBusCountForScope:];
-[ATBlurMixer getPropStripPath];
-[ATBlurMixer initDownlinkWithFormat:maxFrames:error:];
-[ATBlurMixer initInternalWithFormat:maxFrames:isUplink:error:];
-[ATBlurMixer initUplinkWithFormat:maxFrames:error:];
-[ATBlurMixer initializeAU];
-[ATBlurMixer setAUStrip:propertyStrip:];
-[ATBlurMixer setDSPGraph:];
-[ATBlurMixer setElementCount:];
-[ATBlurMixer setEnableBlur:];
-[ATBlurMixer setMaxFramesPerSlice];
-[ATBlurMixer uninitializeAU];
-[ATBlurMixer updateFormat:error:];
-[ATBlurMixer updateFormats];
```
