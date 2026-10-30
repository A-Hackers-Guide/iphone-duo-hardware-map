# `AVAssetWriterInputConfigurationState`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 25 properties, 51 instance methods, 0 class methods

## Instance variables

```
@"NSString" _mediaType;
@"AVOutputSettings" _outputSettings;
^{opaqueCMFormatDescription=} _sourceFormatHint;
i _trackID;
@"NSDictionary" _sourcePixelBufferAttributes;
@"NSArray" _metadataItems;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
i _mediaTimeScale;
B _expectsMediaDataInRealTime;
{CGSize="width"d"height"d} _naturalSize;
@"NSString" _languageCode;
@"NSString" _extendedLanguageTag;
B _marksOutputTrackAsEnabled;
f _preferredVolume;
q _layer;
s _alternateGroupID;
s _provisionalAlternateGroupID;
@"NSDictionary" _trackReferences;
B _performsMultiPassEncodingIfSupported;
{?="value"q"timescale"i"flags"I"epoch"q} _chunkDuration;
q _chunkAlignment;
q _chunkSize;
@"NSString" _mediaDataLocation;
@"NSURL" _sampleReferenceBaseURL;
B _maximizePowerEfficiency;
```

## Properties

```
@property (T@"NSString",C,N,V_mediaType) mediaType;
@property (T@"AVOutputSettings",C,N,V_outputSettings) outputSettings;
@property (T^{opaqueCMFormatDescription=},&,N,V_sourceFormatHint) sourceFormatHint;
@property (Ti,N,V_trackID) trackID;
@property (T@"NSDictionary",C,N,V_sourcePixelBufferAttributes) sourcePixelBufferAttributes;
@property (T@"NSArray",C,N,V_metadataItems) metadataItems;
@property (T{CGAffineTransform=dddddd},N,V_transform) transform;
@property (Ti,N,V_mediaTimeScale) mediaTimeScale;
@property (TB,N,V_expectsMediaDataInRealTime) expectsMediaDataInRealTime;
@property (T{CGSize=dd},N,V_naturalSize) naturalSize;
@property (T@"NSString",C,N,V_languageCode) languageCode;
@property (T@"NSString",C,N,V_extendedLanguageTag) extendedLanguageTag;
@property (TB,N,V_marksOutputTrackAsEnabled) marksOutputTrackAsEnabled;
@property (Tf,N,V_preferredVolume) preferredVolume;
@property (Tq,N,V_layer) layer;
@property (Ts,N,V_alternateGroupID) alternateGroupID;
@property (Ts,N,V_provisionalAlternateGroupID) provisionalAlternateGroupID;
@property (T@"NSDictionary",C,N,V_trackReferences) trackReferences;
@property (TB,N,V_performsMultiPassEncodingIfSupported) performsMultiPassEncodingIfSupported;
@property (T{?=qiIq},N,V_chunkDuration) preferredMediaChunkDuration;
@property (Tq,N,V_chunkAlignment) preferredMediaChunkAlignment;
@property (Tq,N,V_chunkSize) preferredMediaChunkSize;
@property (T@"NSString",C,N,V_mediaDataLocation) mediaDataLocation;
@property (T@"NSURL",C,N,V_sampleReferenceBaseURL) sampleReferenceBaseURL;
@property (TB,N,V_maximizePowerEfficiency) maximizePowerEfficiency;
```

## Instance methods

```
-[AVAssetWriterInputConfigurationState setNaturalSize:];
-[AVAssetWriterInputConfigurationState trackReferences];
-[AVAssetWriterInputConfigurationState outputSettings];
-[AVAssetWriterInputConfigurationState setExtendedLanguageTag:];
-[AVAssetWriterInputConfigurationState setPreferredVolume:];
-[AVAssetWriterInputConfigurationState layer];
-[AVAssetWriterInputConfigurationState metadataItems];
-[AVAssetWriterInputConfigurationState trackID];
-[AVAssetWriterInputConfigurationState naturalSize];
-[AVAssetWriterInputConfigurationState dealloc];
-[AVAssetWriterInputConfigurationState setTransform:];
-[AVAssetWriterInputConfigurationState transform];
-[AVAssetWriterInputConfigurationState setOutputSettings:];
-[AVAssetWriterInputConfigurationState preferredVolume];
-[AVAssetWriterInputConfigurationState languageCode];
-[AVAssetWriterInputConfigurationState setMediaType:];
-[AVAssetWriterInputConfigurationState provisionalAlternateGroupID];
-[AVAssetWriterInputConfigurationState alternateGroupID];
-[AVAssetWriterInputConfigurationState setAlternateGroupID:];
-[AVAssetWriterInputConfigurationState extendedLanguageTag];
-[AVAssetWriterInputConfigurationState mediaType];
-[AVAssetWriterInputConfigurationState setLanguageCode:];
-[AVAssetWriterInputConfigurationState setLayer:];
-[AVAssetWriterInputConfigurationState sourcePixelBufferAttributes];
-[AVAssetWriterInputConfigurationState setPreferredMediaChunkDuration:];
-[AVAssetWriterInputConfigurationState setProvisionalAlternateGroupID:];
-[AVAssetWriterInputConfigurationState setSourcePixelBufferAttributes:];
-[AVAssetWriterInputConfigurationState expectsMediaDataInRealTime];
-[AVAssetWriterInputConfigurationState marksOutputTrackAsEnabled];
-[AVAssetWriterInputConfigurationState maximizePowerEfficiency];
-[AVAssetWriterInputConfigurationState mediaDataLocation];
-[AVAssetWriterInputConfigurationState mediaTimeScale];
-[AVAssetWriterInputConfigurationState performsMultiPassEncodingIfSupported];
-[AVAssetWriterInputConfigurationState preferredMediaChunkAlignment];
-[AVAssetWriterInputConfigurationState preferredMediaChunkDuration];
-[AVAssetWriterInputConfigurationState preferredMediaChunkSize];
-[AVAssetWriterInputConfigurationState sampleReferenceBaseURL];
-[AVAssetWriterInputConfigurationState setExpectsMediaDataInRealTime:];
-[AVAssetWriterInputConfigurationState setMarksOutputTrackAsEnabled:];
-[AVAssetWriterInputConfigurationState setMaximizePowerEfficiency:];
-[AVAssetWriterInputConfigurationState setMediaDataLocation:];
-[AVAssetWriterInputConfigurationState setMediaTimeScale:];
-[AVAssetWriterInputConfigurationState setMetadataItems:];
-[AVAssetWriterInputConfigurationState setPerformsMultiPassEncodingIfSupported:];
-[AVAssetWriterInputConfigurationState setPreferredMediaChunkAlignment:];
-[AVAssetWriterInputConfigurationState setPreferredMediaChunkSize:];
-[AVAssetWriterInputConfigurationState setSampleReferenceBaseURL:];
-[AVAssetWriterInputConfigurationState setSourceFormatHint:];
-[AVAssetWriterInputConfigurationState setTrackID:];
-[AVAssetWriterInputConfigurationState setTrackReferences:];
-[AVAssetWriterInputConfigurationState sourceFormatHint];
```
