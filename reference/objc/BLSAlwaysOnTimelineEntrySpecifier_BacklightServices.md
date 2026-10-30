# `BLSAlwaysOnTimelineEntrySpecifier`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 7 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
q _requestedFidelity;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _didChange;
@"BLSAlwaysOnTimelineEntry" _timelineEntry;
q _grantedFidelity;
d _percentComplete;
@"BLSAlwaysOnTimelineEntry" _previousTimelineEntry;
```

## Properties

```
@property (TB,V_didChange) didChange;
@property (Tq,V_grantedFidelity) grantedFidelity;
@property (Tq) requestedFidelity;
@property (T@"BLSAlwaysOnTimelineEntry",R,V_timelineEntry) timelineEntry;
@property (Td,R,V_percentComplete) percentComplete;
@property (T@"BLSAlwaysOnTimelineEntry",R,V_previousTimelineEntry) previousTimelineEntry;
```

## Instance methods

```
-[BLSAlwaysOnTimelineEntrySpecifier percentComplete];
-[BLSAlwaysOnTimelineEntrySpecifier debugDescription];
-[BLSAlwaysOnTimelineEntrySpecifier compare:];
-[BLSAlwaysOnTimelineEntrySpecifier hash];
-[BLSAlwaysOnTimelineEntrySpecifier description];
-[BLSAlwaysOnTimelineEntrySpecifier copyWithZone:];
-[BLSAlwaysOnTimelineEntrySpecifier grantedFidelity];
-[BLSAlwaysOnTimelineEntrySpecifier isEqual:];
-[BLSAlwaysOnTimelineEntrySpecifier requestedFidelity];
-[BLSAlwaysOnTimelineEntrySpecifier timelineEntry];
-[BLSAlwaysOnTimelineEntrySpecifier didChange];
-[BLSAlwaysOnTimelineEntrySpecifier setDidChange:];
-[BLSAlwaysOnTimelineEntrySpecifier previousTimelineEntry];
-[BLSAlwaysOnTimelineEntrySpecifier appendFidelityToTarget:];
-[BLSAlwaysOnTimelineEntrySpecifier initWithTimelineEntry:percentComplete:previousTimelineEntry:didChange:];
-[BLSAlwaysOnTimelineEntrySpecifier setGrantedFidelity:];
-[BLSAlwaysOnTimelineEntrySpecifier setRequestedFidelity:];
```
