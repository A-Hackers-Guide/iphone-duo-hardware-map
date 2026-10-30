# `AVPlayerRateState`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
f _rate;
B _automaticallyWaitsToMinimizeStalling;
B _usesLegacyAutomaticWaitingBehavior;
q _timeControlStatus;
@"NSString" _reasonForWaitingToPlay;
```

## Properties

```
@property (Tf,R,N,V_rate) rate;
@property (TB,R,N,V_automaticallyWaitsToMinimizeStalling) automaticallyWaitsToMinimizeStalling;
@property (TB,R,N,V_usesLegacyAutomaticWaitingBehavior) usesLegacyAutomaticWaitingBehavior;
@property (Tq,R,N,V_timeControlStatus) timeControlStatus;
@property (T@"NSString",R,N,V_reasonForWaitingToPlay) reasonForWaitingToPlay;
```

## Instance methods

```
-[AVPlayerRateState rate];
-[AVPlayerRateState rateStateBySettingRate:nameForLogging:];
-[AVPlayerRateState dealloc];
-[AVPlayerRateState timeControlStatus];
-[AVPlayerRateState rateStateByUpdatingBasedOnFigPlayerPlaybackState:hasCurrentInterstitialEvent:nameForLogging:];
-[AVPlayerRateState rateStateBySettingAutomaticallyWaitsToMinimizeStalling:];
-[AVPlayerRateState rateStateByUpdatingBasedOnFigPlayer:hasCurrentItem:hasCurrentInterstitialEvent:nameForLogging:];
-[AVPlayerRateState usesLegacyAutomaticWaitingBehavior];
-[AVPlayerRateState automaticallyWaitsToMinimizeStalling];
-[AVPlayerRateState reasonForWaitingToPlay];
-[AVPlayerRateState copyWithZone:];
-[AVPlayerRateState initWithAutomaticallyWaitsToMinimizeStalling:usesLegacyAutomaticWaitingBehavior:timeControlStatus:];
-[AVPlayerRateState rateStateBySettingUsesLegacyAutomaticWaitingBehavior:];
-[AVPlayerRateState rateStateBySettingTimeControlStatus:reasonForWaitingToPlay:nameForLogging:];
-[AVPlayerRateState rateStateByInferringTimeControlStatusAndWaitingReasonBasedOnPresenceOfCurrentItem:hasCurrentInterstitialEvent:nameForLogging:];
-[AVPlayerRateState rateStateByUpdatingBasedOnPresenceOfCurrentInterstitialEvent:nameForLogging:];
```
