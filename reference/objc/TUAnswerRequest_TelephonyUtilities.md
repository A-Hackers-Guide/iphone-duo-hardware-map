# `TUAnswerRequest`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `TUCallRequest`, `TUVideoRequest`
- 17 instance variables, 21 properties, 40 instance methods, 1 class methods

## Instance variables

```
B _wantsHoldMusic;
B _pauseVideoToStart;
B _downgradeToAudio;
B _sendToScreening;
B _screeningDueToUserInteraction;
B _launchInBackground;
B _allowBluetoothAnswerWithoutDowngrade;
@"NSString" _uniqueProxyIdentifier;
@"NSString" _sourceIdentifier;
@"IDSDestination" _endpointIDSDestination;
@"NSString" _endpointRapportMediaSystemIdentifier;
@"NSString" _endpointRapportEffectiveIdentifier;
q _behavior;
q _screeningType;
@"NSDate" _dateAnswered;
{CGSize="width"d"height"d} _localLandscapeAspectRatio;
{CGSize="width"d"height"d} _localPortraitAspectRatio;
```

## Properties

```
@property (T@"NSDate",&,N,V_dateAnswered) dateAnswered;
@property (TB,N,V_allowBluetoothAnswerWithoutDowngrade) allowBluetoothAnswerWithoutDowngrade;
@property (T@"NSString",C,N,V_sourceIdentifier) sourceIdentifier;
@property (T@"IDSDestination",&,N,V_endpointIDSDestination) endpointIDSDestination;
@property (T@"NSString",&,N,V_endpointRapportMediaSystemIdentifier) endpointRapportMediaSystemIdentifier;
@property (T@"NSString",&,N,V_endpointRapportEffectiveIdentifier) endpointRapportEffectiveIdentifier;
@property (TB,N,V_wantsHoldMusic) wantsHoldMusic;
@property (TB,N,V_pauseVideoToStart) pauseVideoToStart;
@property (TB,N,V_downgradeToAudio) downgradeToAudio;
@property (Tq,N,V_behavior) behavior;
@property (TB,N,V_sendToScreening) sendToScreening;
@property (Tq,N,V_screeningType) screeningType;
@property (TB,N,V_screeningDueToUserInteraction) screeningDueToUserInteraction;
@property (TB,N,V_launchInBackground) launchInBackground;
@property (T@"NSString",C,N,V_uniqueProxyIdentifier) uniqueProxyIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{CGSize=dd},N,V_localLandscapeAspectRatio) localLandscapeAspectRatio;
@property (T{CGSize=dd},N,V_localPortraitAspectRatio) localPortraitAspectRatio;
```

## Class methods

```
+[TUAnswerRequest supportsSecureCoding];
```

## Instance methods

```
-[TUAnswerRequest endpointRapportMediaSystemIdentifier];
-[TUAnswerRequest init];
-[TUAnswerRequest setLocalLandscapeAspectRatio:];
-[TUAnswerRequest setUniqueProxyIdentifier:];
-[TUAnswerRequest launchInBackground];
-[TUAnswerRequest setLocalPortraitAspectRatio:];
-[TUAnswerRequest setWantsHoldMusic:];
-[TUAnswerRequest setLaunchInBackground:];
-[TUAnswerRequest localLandscapeAspectRatio];
-[TUAnswerRequest sourceIdentifier];
-[TUAnswerRequest setBehavior:];
-[TUAnswerRequest endpointRapportEffectiveIdentifier];
-[TUAnswerRequest behavior];
-[TUAnswerRequest setSourceIdentifier:];
-[TUAnswerRequest localPortraitAspectRatio];
-[TUAnswerRequest initWithUniqueProxyIdentifier:];
-[TUAnswerRequest wantsHoldMusic];
-[TUAnswerRequest endpointIDSDestination];
-[TUAnswerRequest encodeWithCoder:];
-[TUAnswerRequest setScreeningDueToUserInteraction:];
-[TUAnswerRequest description];
-[TUAnswerRequest initWithCoder:];
-[TUAnswerRequest setEndpointRapportMediaSystemIdentifier:];
-[TUAnswerRequest setEndpointRapportEffectiveIdentifier:];
-[TUAnswerRequest uniqueProxyIdentifier];
-[TUAnswerRequest initWithCall:];
-[TUAnswerRequest sendToScreening];
-[TUAnswerRequest allowBluetoothAnswerWithoutDowngrade];
-[TUAnswerRequest dateAnswered];
-[TUAnswerRequest downgradeToAudio];
-[TUAnswerRequest pauseVideoToStart];
-[TUAnswerRequest screeningDueToUserInteraction];
-[TUAnswerRequest screeningType];
-[TUAnswerRequest setAllowBluetoothAnswerWithoutDowngrade:];
-[TUAnswerRequest setDateAnswered:];
-[TUAnswerRequest setDowngradeToAudio:];
-[TUAnswerRequest setEndpointIDSDestination:];
-[TUAnswerRequest setPauseVideoToStart:];
-[TUAnswerRequest setScreeningType:];
-[TUAnswerRequest setSendToScreening:];
```
