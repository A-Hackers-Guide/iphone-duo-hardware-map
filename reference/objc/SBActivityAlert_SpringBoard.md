# `SBActivityAlert`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 7 instance variables, 11 properties, 29 instance methods, 0 class methods

## Instance variables

```
B _prominent;
@"SBActivityItem" _item;
@"NSString" _payloadIdentifier;
@"ACUISActivityAlertOptions" _options;
@"NSString" _title;
@"NSString" _body;
@"SBUISound" _playingSound;
```

## Properties

```
@property (T@"SBUISound",&,N,V_playingSound) playingSound;
@property (T@"SBActivityItem",R,N,V_item) item;
@property (T@"NSString",R,C,N,V_payloadIdentifier) payloadIdentifier;
@property (T@"ACUISActivityAlertOptions",R,N,V_options) options;
@property (T@"NSString",R,N,V_title) title;
@property (T@"NSString",R,N,V_body) body;
@property (TB,N,GisProminent,V_prominent) prominent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBActivityAlert _canPresentAlertTypeModalFullScreenInEnvironment:];
-[SBActivityAlert body];
-[SBActivityAlert _isHostApplicationForeground];
-[SBActivityAlert _stopSoundIfNeeded:];
-[SBActivityAlert setPlayingSound:];
-[SBActivityAlert succinctDescriptionBuilder];
-[SBActivityAlert dealloc];
-[SBActivityAlert descriptionWithMultilinePrefix:];
-[SBActivityAlert item];
-[SBActivityAlert shouldAlertInEnvironment:];
-[SBActivityAlert succinctDescription];
-[SBActivityAlert playingSound];
-[SBActivityAlert title];
-[SBActivityAlert canPresentAlertTypeAmbientInEnvironment:];
-[SBActivityAlert _playSound];
-[SBActivityAlert canPresentInEnvironment:alertType:];
-[SBActivityAlert stopAlerting];
-[SBActivityAlert description];
-[SBActivityAlert canPresentAlertTypeNoneInEnvironment:];
-[SBActivityAlert _isActiveCoverSheetVisible];
-[SBActivityAlert payloadIdentifier];
-[SBActivityAlert initWithItem:payloadIdentifier:options:title:body:];
-[SBActivityAlert canPresentAlertTypeBannerOrSystemApertureInEnvironment:];
-[SBActivityAlert options];
-[SBActivityAlert _hasPresentationDestination:];
-[SBActivityAlert setProminent:];
-[SBActivityAlert isProminent];
-[SBActivityAlert alertWithScreenOn:playSound:];
-[SBActivityAlert descriptionBuilderWithMultilinePrefix:];
```
