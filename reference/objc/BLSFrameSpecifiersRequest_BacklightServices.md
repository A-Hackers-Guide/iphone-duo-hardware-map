# `BLSFrameSpecifiersRequest`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@? _completion;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_completed;
B _shouldReset;
@"NSDateInterval" _dateInterval;
@"NSDate" _previousPresentationDate;
```

## Properties

```
@property (T@"NSDateInterval",R,N,V_dateInterval) dateInterval;
@property (T@"NSDate",R,N,V_previousPresentationDate) previousPresentationDate;
@property (TB,R,N,V_shouldReset) shouldReset;
```

## Instance methods

```
-[BLSFrameSpecifiersRequest dateInterval];
-[BLSFrameSpecifiersRequest hash];
-[BLSFrameSpecifiersRequest description];
-[BLSFrameSpecifiersRequest isEqual:];
-[BLSFrameSpecifiersRequest shouldReset];
-[BLSFrameSpecifiersRequest completeWithDateSpecifiers:];
-[BLSFrameSpecifiersRequest initWithDateInterval:previousPresentationDate:shouldReset:completion:];
-[BLSFrameSpecifiersRequest previousPresentationDate];
```
