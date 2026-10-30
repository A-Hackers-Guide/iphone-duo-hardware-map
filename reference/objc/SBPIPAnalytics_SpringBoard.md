# `SBPIPAnalytics`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PGPictureInPictureAnalyticsDelegate`
- 2 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _analyticsSourceAssistants;
@"NSMutableDictionary" _analyticsSessionAssistants;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPIPAnalytics pictureInPictureDidActivateAnalyticsSessionWithUUID:analyticsSourceUUID:automatically:];
-[SBPIPAnalytics pictureInPictureDidChangeStashStateForAnalyticsSessionWithUUID:stashed:];
-[SBPIPAnalytics pictureInPictureDidCreateAnalyticsSessionWithUUID:bundleIdentifier:contentType:];
-[SBPIPAnalytics pictureInPictureDidCreateAnalyticsSourceWithUUID:bundleIdentifier:contentType:];
-[SBPIPAnalytics pictureInPictureDidDeactivateAnalyticsSessionWithUUID:analyticsSourceUUID:appStoppedSession:restoredFullScreen:];
-[SBPIPAnalytics pictureInPictureDidDestroyAnalyticsSessionWithUUID:];
-[SBPIPAnalytics pictureInPictureDidDestroyAnalyticsSourceWithUUID:];
-[SBPIPAnalytics assistantForUUID:];
-[SBPIPAnalytics pictureInPictureAnalyticsSourceWithUUID:didBecomePossible:];
```
