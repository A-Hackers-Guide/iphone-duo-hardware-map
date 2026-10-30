# `BLSAlwaysOnFrameSpecifier`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 7 properties, 19 instance methods, 2 class methods

## Instance variables

```
q _grantedFidelity;
Q _lowPowerRenderingPresentationTime;
B _lowPowerRendering;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSArray" _entrySpecifiers;
@"NSDateInterval" _presentationInterval;
```

## Properties

```
@property (Tq) grantedFidelity;
@property (TQ) lowPowerRenderingPresentationTime;
@property (TB,GisLowPowerRendering) lowPowerRendering;
@property (T@"NSArray",R,V_entrySpecifiers) entrySpecifiers;
@property (T@"NSDateInterval",R,V_presentationInterval) presentationInterval;
@property (Tq,R) requestedFidelity;
@property (T@"NSDate",R) lowPowerRenderingPresentationDate;
```

## Class methods

```
+[BLSAlwaysOnFrameSpecifier loggingStringForPresentationInterval:];
+[BLSAlwaysOnFrameSpecifier shortLoggingStringForPresentationInterval:];
```

## Instance methods

```
-[BLSAlwaysOnFrameSpecifier debugDescription];
-[BLSAlwaysOnFrameSpecifier compare:];
-[BLSAlwaysOnFrameSpecifier setLowPowerRenderingPresentationTime:];
-[BLSAlwaysOnFrameSpecifier isLowPowerRendering];
-[BLSAlwaysOnFrameSpecifier hash];
-[BLSAlwaysOnFrameSpecifier description];
-[BLSAlwaysOnFrameSpecifier copyWithZone:];
-[BLSAlwaysOnFrameSpecifier grantedFidelity];
-[BLSAlwaysOnFrameSpecifier isEqual:];
-[BLSAlwaysOnFrameSpecifier lowPowerRenderingPresentationTime];
-[BLSAlwaysOnFrameSpecifier setLowPowerRendering:];
-[BLSAlwaysOnFrameSpecifier entrySpecifierForTimelineIdentifier:];
-[BLSAlwaysOnFrameSpecifier presentationInterval];
-[BLSAlwaysOnFrameSpecifier requestedFidelity];
-[BLSAlwaysOnFrameSpecifier entrySpecifiers];
-[BLSAlwaysOnFrameSpecifier correctedSpecifierWithNextSpecifier:];
-[BLSAlwaysOnFrameSpecifier initWithTimelineEntrySpecifiers:presentationInterval:];
-[BLSAlwaysOnFrameSpecifier lowPowerRenderingPresentationDate];
-[BLSAlwaysOnFrameSpecifier setGrantedFidelity:];
```
