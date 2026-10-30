# `BWReactionAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 4 instance variables, 8 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSString" _clientApplicationID;
i _continuityCameraClientDeviceClass;
B _uiTriggeredReaction;
@"NSString" _reactionType;
```

## Properties

```
@property (T@"NSString",C,N,V_reactionType) reactionType;
@property (TB,N,V_uiTriggeredReaction) uiTriggeredReaction;
@property (T@"NSString",C,N,V_clientApplicationID) clientApplicationID;
@property (Ti,N,V_continuityCameraClientDeviceClass) continuityCameraClientDeviceClass;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWReactionAnalyticsPayload setContinuityCameraClientDeviceClass:];
-[BWReactionAnalyticsPayload eventDictionary];
-[BWReactionAnalyticsPayload init];
-[BWReactionAnalyticsPayload dealloc];
-[BWReactionAnalyticsPayload reset];
-[BWReactionAnalyticsPayload setClientApplicationID:];
-[BWReactionAnalyticsPayload continuityCameraClientDeviceClass];
-[BWReactionAnalyticsPayload eventName];
-[BWReactionAnalyticsPayload clientApplicationID];
-[BWReactionAnalyticsPayload reactionType];
-[BWReactionAnalyticsPayload setReactionType:];
-[BWReactionAnalyticsPayload setUiTriggeredReaction:];
-[BWReactionAnalyticsPayload uiTriggeredReaction];
```
