# `SRHeadphoneSettingsHearingAssistance`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSSecureCoding`, `NSCopying`
- 10 instance variables, 14 properties, 19 instance methods, 1 class methods

## Instance variables

```
q _hearingAidEnabled;
q _mediaAssistEnabled;
q _adjustMediaEnabled;
q _adjustVoiceEnabled;
q _hearingProtectionEnabled;
q _conversationBoostEnabled;
d _hearingAidAmplification;
d _hearingAidBalance;
d _hearingAidTone;
d _ambientNoiseReduction;
```

## Properties

```
@property (Tq,R,N,V_hearingAidEnabled) hearingAidEnabled;
@property (Tq,R,N,V_mediaAssistEnabled) mediaAssistEnabled;
@property (Tq,R,N,V_adjustMediaEnabled) adjustMediaEnabled;
@property (Tq,R,N,V_adjustVoiceEnabled) adjustVoiceEnabled;
@property (Tq,R,N,V_hearingProtectionEnabled) hearingProtectionEnabled;
@property (Tq,R,N,V_conversationBoostEnabled) conversationBoostEnabled;
@property (Td,R,N,V_hearingAidAmplification) hearingAidAmplification;
@property (Td,R,N,V_hearingAidBalance) hearingAidBalance;
@property (Td,R,N,V_hearingAidTone) hearingAidTone;
@property (Td,R,N,V_ambientNoiseReduction) ambientNoiseReduction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRHeadphoneSettingsHearingAssistance supportsSecureCoding];
```

## Instance methods

```
-[SRHeadphoneSettingsHearingAssistance encodeWithCoder:];
-[SRHeadphoneSettingsHearingAssistance hash];
-[SRHeadphoneSettingsHearingAssistance description];
-[SRHeadphoneSettingsHearingAssistance initWithCoder:];
-[SRHeadphoneSettingsHearingAssistance copyWithZone:];
-[SRHeadphoneSettingsHearingAssistance isEqual:];
-[SRHeadphoneSettingsHearingAssistance binarySampleRepresentation];
-[SRHeadphoneSettingsHearingAssistance initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRHeadphoneSettingsHearingAssistance hearingAidEnabled];
-[SRHeadphoneSettingsHearingAssistance hearingProtectionEnabled];
-[SRHeadphoneSettingsHearingAssistance mediaAssistEnabled];
-[SRHeadphoneSettingsHearingAssistance adjustMediaEnabled];
-[SRHeadphoneSettingsHearingAssistance adjustVoiceEnabled];
-[SRHeadphoneSettingsHearingAssistance ambientNoiseReduction];
-[SRHeadphoneSettingsHearingAssistance conversationBoostEnabled];
-[SRHeadphoneSettingsHearingAssistance hearingAidAmplification];
-[SRHeadphoneSettingsHearingAssistance hearingAidBalance];
-[SRHeadphoneSettingsHearingAssistance hearingAidTone];
-[SRHeadphoneSettingsHearingAssistance initWithHearingAidEnabled:mediaAssistEnabled:adjustMediaEnabled:adjustVoiceEnabled:hearingProtectionEnabled:conversationBoostEnabled:hearingAidAmplification:hearingAidBalance:hearingAidTone:ambientNoiseReduction:];
```
