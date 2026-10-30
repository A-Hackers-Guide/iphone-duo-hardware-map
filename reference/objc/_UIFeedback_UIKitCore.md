# `_UIFeedback`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 15 instance variables, 30 properties, 53 instance methods, 5 class methods

## Instance variables

```
B _playing;
f _position;
@"_UIFeedbackParameters" _audioParameters;
@"_UIFeedbackParameters" _hapticParameters;
q _audioOutputMode;
q _hapticOutputMode;
q _peripheralOutputMode;
@"_UIFeedbackPattern" _parentPattern;
@"NSDictionary" _debugDictionary;
@"NSString" _name;
@"NSString" _category;
@"UIView" _view;
d _delay;
@"<_UIFeedbackPlayer>" _player;
{CGPoint="x"d"y"d} _location;
```

## Properties

```
@property (T@"NSMutableArray",R) systemSoundSources;
@property (T@"NSMutableArray",R) visualizerSources;
@property (TB,R,N,GisPlaying,V_playing) playing;
@property (T@"_UIFeedbackPattern",W,N,G_parentPattern,S_setParentPattern:,V_parentPattern) parentPattern;
@property (T@"NSDictionary",R,N,G_debugDictionary,V_debugDictionary) debugDictionary;
@property (T@"NSArray",R,N,G_effectiveFeedbackData) effectiveFeedbackData;
@property (T@"NSString",C,N,G_name,S_setName:,V_name) name;
@property (T@"Protocol",R,N,G_playableProtocol) playableProtocol;
@property (T@"NSString",&,N,G_category,S_setCategory:,V_category) category;
@property (TQ,R,N,G_effectiveFeedbackTypes) effectiveFeedbackTypes;
@property (TQ,R,N,G_effectiveEnabledFeedbackTypes) effectiveEnabledFeedbackTypes;
@property (TQ,R,N,G_effectivePlayableFeedbackTypes) effectivePlayableFeedbackTypes;
@property (TQ,R,N,G_effectiveEventType) effectiveEventType;
@property (TI,R,N,G_effectiveSystemSoundID) effectiveSystemSoundID;
@property (Td,R,N,G_effectiveDuration) effectiveDuration;
@property (Td,R,N,G_effectiveDelay) effectiveDelay;
@property (T@"NSArray",R,N,G_individualFeedbacks) individualFeedbacks;
@property (T@"NSIndexSet",R,N,G_allEventTypes) allEventTypes;
@property (T@"NSIndexSet",R,N,G_allSystemSoundIDs) allSystemSoundIDs;
@property (T@"UIView",W,N,G_view,S_setView:,V_view) view;
@property (T{CGPoint=dd},N,G_location,S_setLocation:,V_location) location;
@property (Td,N,G_delay,S_setDelay:,V_delay) delay;
@property (T@"<_UIFeedbackPlayer>",&,N,G_player,S_setPlayer:,V_player) player;
@property (T@"NSDictionary",R,N) dictionaryRepresentation;
@property (T@"_UIFeedbackParameters",R,N,V_audioParameters) audioParameters;
@property (T@"_UIFeedbackParameters",R,N,V_hapticParameters) hapticParameters;
@property (Tq,N,V_audioOutputMode) audioOutputMode;
@property (Tq,N,V_hapticOutputMode) hapticOutputMode;
@property (Tq,N,V_peripheralOutputMode) peripheralOutputMode;
@property (Tf,N,V_position) position;
```

## Class methods

```
+[_UIFeedback supportsSecureCoding];
+[_UIFeedback type];
+[_UIFeedback _parametersClass];
+[_UIFeedback classForType:];
+[_UIFeedback feedbackWithDictionaryRepresentation:];
```

## Instance methods

```
-[_UIFeedback _setName:];
-[_UIFeedback _view];
-[_UIFeedback _effectivePlayableFeedbackTypes];
-[_UIFeedback position];
-[_UIFeedback _effectiveSystemSoundID];
-[_UIFeedback initWithDictionaryRepresentation:];
-[_UIFeedback play];
-[_UIFeedback _name];
-[_UIFeedback hapticParameters];
-[_UIFeedback _allEventTypes];
-[_UIFeedback _delay];
-[_UIFeedback init];
-[_UIFeedback audioParameters];
-[_UIFeedback stop];
-[_UIFeedback dealloc];
-[_UIFeedback isPlaying];
-[_UIFeedback _setView:];
-[_UIFeedback _effectiveEventType];
-[_UIFeedback _setLocation:];
-[_UIFeedback encodeWithCoder:];
-[_UIFeedback _playableProtocol];
-[_UIFeedback _individualFeedbacks];
-[_UIFeedback description];
-[_UIFeedback initWithCoder:];
-[_UIFeedback _location];
-[_UIFeedback setPosition:];
-[_UIFeedback copyWithZone:];
-[_UIFeedback _allSystemSoundIDs];
-[_UIFeedback isEqual:];
-[_UIFeedback _debugDictionary];
-[_UIFeedback dictionaryRepresentation];
-[_UIFeedback _player];
-[_UIFeedback audioOutputMode];
-[_UIFeedback _effectiveDelay];
-[_UIFeedback _category];
-[_UIFeedback _effectiveDuration];
-[_UIFeedback _effectiveEnabledFeedbackTypes];
-[_UIFeedback _effectiveFeedbackData];
-[_UIFeedback _effectiveFeedbackTypes];
-[_UIFeedback _parentPattern];
-[_UIFeedback _playedAtTime:engine:];
-[_UIFeedback _setCategory:];
-[_UIFeedback _setDelay:];
-[_UIFeedback _setParentPattern:];
-[_UIFeedback _setPlayer:];
-[_UIFeedback hapticOutputMode];
-[_UIFeedback peripheralOutputMode];
-[_UIFeedback playWithCompletion:];
-[_UIFeedback setAudioOutputMode:];
-[_UIFeedback setHapticOutputMode:];
-[_UIFeedback setPeripheralOutputMode:];
-[_UIFeedback systemSoundSources];
-[_UIFeedback visualizerSources];
```
