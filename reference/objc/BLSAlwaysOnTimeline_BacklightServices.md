# `BLSAlwaysOnTimeline`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 8 instance methods, 8 class methods

## Instance variables

```
@"<NSObject><NSCopying>" _identifier;
@? _configureEntryBlock;
```

## Properties

```
@property (T@"<NSObject><NSCopying>",R,N,V_identifier) identifier;
```

## Class methods

```
+[BLSAlwaysOnTimeline constructFrameSpecifiersForTimelines:dateInterval:shouldConstructStartSpecifier:framesPerSecond:previousSpecifier:];
+[BLSAlwaysOnTimeline emptyTimelineWithIdentifier:];
+[BLSAlwaysOnTimeline timelineWithEntries:identifier:configure:];
+[BLSAlwaysOnTimeline everyMinuteTimelineWithIdentifier:configure:];
+[BLSAlwaysOnTimeline timelineWithPerMinuteUpdateFrequency:identifier:configure:];
+[BLSAlwaysOnTimeline timelineWithUpdateInterval:startDate:identifier:configure:];
+[BLSAlwaysOnTimeline rangeOfEntries:forDateInterval:shouldIncludePrevious:];
+[BLSAlwaysOnTimeline requestedFidelityForTimelines:inDateInterval:];
```

## Instance methods

```
-[BLSAlwaysOnTimeline identifier];
-[BLSAlwaysOnTimeline description];
-[BLSAlwaysOnTimeline requestedFidelityForStartEntryInDateInterval:withPreviousEntry:];
-[BLSAlwaysOnTimeline estimatedFidelityForPresentationTime:nextPresentationTime:];
-[BLSAlwaysOnTimeline initWithIdentifier:configure:];
-[BLSAlwaysOnTimeline unconfiguredEntriesForDateInterval:previousEntry:];
-[BLSAlwaysOnTimeline configureEntries:previousEntry:];
-[BLSAlwaysOnTimeline configureEntry:previousEntry:];
```
