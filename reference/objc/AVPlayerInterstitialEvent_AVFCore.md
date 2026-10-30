# `AVPlayerInterstitialEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 20 properties, 56 instance methods, 5 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _ivarAccessQueue;
@"AVPlayerItem" _primaryItem;
^{OpaqueFigPlayerInterstitialEvent=} _figEvent;
@"NSArray" _templateItems;
```

## Properties

```
@property (T@"AVPlayerItem",R,W,N) primaryItem;
@property (T@"NSString",R,N) identifier;
@property (T{?=qiIq},R,N) time;
@property (T@"NSDate",R,N) date;
@property (T@"NSArray",R,N) templateItems;
@property (TQ,R,N) restrictions;
@property (T{?=qiIq},R,N) resumptionOffset;
@property (T{?=qiIq},R,N) playoutLimit;
@property (TB,R,N) alignsStartWithPrimarySegmentBoundary;
@property (TB,R,N) alignsResumptionWithPrimarySegmentBoundary;
@property (T@"NSString",R,N) cue;
@property (TB,R,N) willPlayOnce;
@property (T@"NSDictionary",R,N) userDefinedAttributes;
@property (T@"NSDictionary",R) assetListResponse;
@property (T@"NSString",R) scheduleIdentifier;
@property (Tq,R,N) timelineOccupancy;
@property (TB,R,N) supplementsPrimaryContent;
@property (TB,R,N) contentMayVary;
@property (T{?={?=qiIq}{?=qiIq}},R,N) skipControlTimeRange;
@property (T@"NSString",R,N) skipControlLocalizedLabelBundleKey;
```

## Class methods

```
+[AVPlayerInterstitialEvent interstitialEventWithPrimaryItem:date:];
+[AVPlayerInterstitialEvent interstitialEventWithPrimaryItem:identifier:date:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:];
+[AVPlayerInterstitialEvent interstitialEventWithPrimaryItem:identifier:time:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:];
+[AVPlayerInterstitialEvent interstitialEventWithPrimaryItem:time:];
+[AVPlayerInterstitialEvent newItemArrayWithCopiedItems:];
```

## Instance methods

```
-[AVPlayerInterstitialEvent validate:];
-[AVPlayerInterstitialEvent identifier];
-[AVPlayerInterstitialEvent setDate:];
-[AVPlayerInterstitialEvent dealloc];
-[AVPlayerInterstitialEvent date];
-[AVPlayerInterstitialEvent setIdentifier:];
-[AVPlayerInterstitialEvent restrictions];
-[AVPlayerInterstitialEvent hash];
-[AVPlayerInterstitialEvent description];
-[AVPlayerInterstitialEvent setTime:];
-[AVPlayerInterstitialEvent copyWithZone:];
-[AVPlayerInterstitialEvent isEqual:];
-[AVPlayerInterstitialEvent setRestrictions:];
-[AVPlayerInterstitialEvent time];
-[AVPlayerInterstitialEvent primaryItem];
-[AVPlayerInterstitialEvent checkMutability];
-[AVPlayerInterstitialEvent cue];
-[AVPlayerInterstitialEvent plannedDuration];
-[AVPlayerInterstitialEvent setCue:];
-[AVPlayerInterstitialEvent setPrimaryItem:];
-[AVPlayerInterstitialEvent _internalTemplateItems];
-[AVPlayerInterstitialEvent _participatesInCoordinatedPlayback];
-[AVPlayerInterstitialEvent _updateStartOffset];
-[AVPlayerInterstitialEvent alignsResumptionWithPrimarySegmentBoundary];
-[AVPlayerInterstitialEvent alignsStartWithPrimarySegmentBoundary];
-[AVPlayerInterstitialEvent assetListResponse];
-[AVPlayerInterstitialEvent assetURLsReturningError:];
-[AVPlayerInterstitialEvent contentMayVary];
-[AVPlayerInterstitialEvent figEvent];
-[AVPlayerInterstitialEvent initWithPrimaryItem:identifier:time:date:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:];
-[AVPlayerInterstitialEvent initWithPrimaryItem:time:date:];
-[AVPlayerInterstitialEvent initWithPrimaryItemAndFigEvent:templateItems:figEvent:];
-[AVPlayerInterstitialEvent playoutLimit];
-[AVPlayerInterstitialEvent resumptionOffset];
-[AVPlayerInterstitialEvent scheduleIdentifier];
-[AVPlayerInterstitialEvent setAlignsResumptionWithPrimarySegmentBoundary:];
-[AVPlayerInterstitialEvent setAlignsStartWithPrimarySegmentBoundary:];
-[AVPlayerInterstitialEvent setContentMayVary:];
-[AVPlayerInterstitialEvent setImmutable];
-[AVPlayerInterstitialEvent setPlannedDuration:];
-[AVPlayerInterstitialEvent setPlayoutLimit:];
-[AVPlayerInterstitialEvent setResumptionOffset:];
-[AVPlayerInterstitialEvent setSkipControlLocalizedLabelBundleKey:];
-[AVPlayerInterstitialEvent setSkipControlTimeRange:];
-[AVPlayerInterstitialEvent setSupplementsPrimaryContent:];
-[AVPlayerInterstitialEvent setTemplateItems:];
-[AVPlayerInterstitialEvent setTimelineOccupancy:];
-[AVPlayerInterstitialEvent setUserDefinedAttributes:];
-[AVPlayerInterstitialEvent setWillPlayOnce:];
-[AVPlayerInterstitialEvent skipControlLocalizedLabelBundleKey];
-[AVPlayerInterstitialEvent skipControlTimeRange];
-[AVPlayerInterstitialEvent supplementsPrimaryContent];
-[AVPlayerInterstitialEvent templateItems];
-[AVPlayerInterstitialEvent timelineOccupancy];
-[AVPlayerInterstitialEvent userDefinedAttributes];
-[AVPlayerInterstitialEvent willPlayOnce];
```
