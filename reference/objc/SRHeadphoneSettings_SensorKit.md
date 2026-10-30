# `SRHeadphoneSettings`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSSecureCoding`, `NSCopying`
- 7 instance variables, 11 properties, 19 instance methods, 3 class methods

## Instance variables

```
I _adaptiveAudioStrength;
q _listeningMode;
q _personalizedVolumeEnabled;
q _conversationAwarenessEnabled;
q _spatialAudioEnabled;
q _personalizedSpatialAudioEnabled;
@"SRHeadphoneSettingsHearingAssistance" _hearingAssistance;
```

## Properties

```
@property (TI,R,N,V_adaptiveAudioStrength) adaptiveAudioStrength;
@property (Tq,R,N,V_listeningMode) listeningMode;
@property (Tq,R,N,V_personalizedVolumeEnabled) personalizedVolumeEnabled;
@property (Tq,R,N,V_conversationAwarenessEnabled) conversationAwarenessEnabled;
@property (Tq,R,N,V_spatialAudioEnabled) spatialAudioEnabled;
@property (Tq,R,N,V_personalizedSpatialAudioEnabled) personalizedSpatialAudioEnabled;
@property (T@"SRHeadphoneSettingsHearingAssistance",R,N,V_hearingAssistance) hearingAssistance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRHeadphoneSettings supportsSecureCoding];
+[SRHeadphoneSettings initialize];
+[SRHeadphoneSettings new];
```

## Instance methods

```
-[SRHeadphoneSettings init];
-[SRHeadphoneSettings dealloc];
-[SRHeadphoneSettings encodeWithCoder:];
-[SRHeadphoneSettings hash];
-[SRHeadphoneSettings description];
-[SRHeadphoneSettings initWithCoder:];
-[SRHeadphoneSettings copyWithZone:];
-[SRHeadphoneSettings isEqual:];
-[SRHeadphoneSettings listeningMode];
-[SRHeadphoneSettings binarySampleRepresentation];
-[SRHeadphoneSettings initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRHeadphoneSettings personalizedSpatialAudioEnabled];
-[SRHeadphoneSettings adaptiveAudioStrength];
-[SRHeadphoneSettings conversationAwarenessEnabled];
-[SRHeadphoneSettings hearingAssistance];
-[SRHeadphoneSettings initWithListeningMode:adaptiveAudioStrength:personalizedVolumeEnabled:hearingAidEnabled:conversationAwarenessEnabled:spatialAudioEnabled:mediaAssistEnabled:adjustMediaEnabled:adjustVoiceEnabled:hearingProtectionEnabled:conversationBoostEnabled:hearingAidAmplification:hearingAidBalance:hearingAidTone:ambientNoiseReduction:personalizedSpatialAudioEnabled:];
-[SRHeadphoneSettings initWithListeningMode:adaptiveAudioStrength:personalizedVolumeEnabled:hearingAssistance:conversationAwarenessEnabled:spatialAudioEnabled:personalizedSpatialAudioEnabled:];
-[SRHeadphoneSettings personalizedVolumeEnabled];
-[SRHeadphoneSettings spatialAudioEnabled];
```
