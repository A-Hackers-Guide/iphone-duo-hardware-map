# `VTEvent`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 18 instance methods, 2 class methods

## Instance variables

```
@"NSURL" _jsonFileUrl;
@"NSDictionary" _voiceTriggerEventInfo;
```

## Properties

```
@property (T@"NSURL",R,N,V_jsonFileUrl) jsonFileUrl;
@property (T@"NSDictionary",R,N,V_voiceTriggerEventInfo) voiceTriggerEventInfo;
```

## Class methods

```
+[VTEvent eventFromURL:];
+[VTEvent eventTypeFromURL:];
```

## Instance methods

```
-[VTEvent voiceTriggerEventInfo];
-[VTEvent timestampString];
-[VTEvent _packStringFromVTEventInfo:key:];
-[VTEvent _buildContent];
-[VTEvent _buildDetail];
-[VTEvent _buildTitle];
-[VTEvent _buildTriggerContent];
-[VTEvent _buildTriggerDetail];
-[VTEvent _getFloatStringFromVTEventWithKey:decimal:];
-[VTEvent _packAudioContent:filepath:];
-[VTEvent _packAudioURLFromVTEventInfo:key:];
-[VTEvent _packBooleanFromVTEventInfo:key:];
-[VTEvent _packStringContent:value:];
-[VTEvent _readJsonFile:];
-[VTEvent eventTrackerDictionary];
-[VTEvent initWithEventLogURL:];
-[VTEvent jsonFileName];
-[VTEvent jsonFileUrl];
```
