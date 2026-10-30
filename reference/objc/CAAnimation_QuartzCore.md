# `CAAnimation`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSMutableCopying`, `CAPropertyInfo`, `NSSecureCoding`, `NSCopying`, `CAMediaTiming`, `CAAction`
- 2 instance variables, 19 properties, 67 instance methods, 11 class methods

## Instance variables

```
^v _attr;
I _flags;
```

## Properties

```
@property (T@"CAStateControllerTransition",W,D) CAStateControllerTransition;
@property (TB,GisEnabled) enabled;
@property (T@"NSString",C) beginTimeMode;
@property (Td) frameInterval;
@property (Tq) preferredFramesPerSecond;
@property (TI) highFrameRateReason;
@property (TB) discretizesTime;
@property (T@"CAMediaTimingFunction",&) timingFunction;
@property (T@"<CAAnimationDelegate>",&) delegate;
@property (TB,GisRemovedOnCompletion) removedOnCompletion;
@property (T{CAFrameRateRange=fff}) preferredFrameRateRange;
@property (Td) beginTime;
@property (Td) duration;
@property (Tf) speed;
@property (Td) timeOffset;
@property (Tf) repeatCount;
@property (Td) repeatDuration;
@property (TB) autoreverses;
@property (T@"NSString",C) fillMode;
```

## Class methods

```
+[CAAnimation supportsSecureCoding];
+[CAAnimation properties];
+[CAAnimation defaultValueForKey:];
+[CAAnimation CA_automaticallyNotifiesObservers:];
+[CAAnimation animation];
+[CAAnimation resolveInstanceMethod:];
+[CAAnimation automaticallyNotifiesObserversForKey:];
+[CAAnimation CAMLParserStartElement:];
+[CAAnimation CA_getterForProperty:];
+[CAAnimation CA_encodesPropertyConditionally:type:];
+[CAAnimation CA_setterForProperty:];
```

## Instance methods

```
-[CAAnimation setAutoreverses:];
-[CAAnimation setHighFrameRateReason:];
-[CAAnimation setBeginTime:];
-[CAAnimation setSpeed:];
-[CAAnimation fillMode];
-[CAAnimation CAMLTypeForKey:];
-[CAAnimation setRemovedOnCompletion:];
-[CAAnimation mutableCopyWithZone:];
-[CAAnimation setRepeatCount:];
-[CAAnimation setFrameInterval:];
-[CAAnimation setFillMode:];
-[CAAnimation repeatCount];
-[CAAnimation debugDescription];
-[CAAnimation setTimingFunction:];
-[CAAnimation isRemovedOnCompletion];
-[CAAnimation CAMLParser:setValue:forKey:];
-[CAAnimation valueForUndefinedKey:];
-[CAAnimation speed];
-[CAAnimation _setCARenderAnimation:layer:];
-[CAAnimation setTimeOffset:];
-[CAAnimation setPreferredFrameRateRange:];
-[CAAnimation repeatDuration];
-[CAAnimation dealloc];
-[CAAnimation autoreverses];
-[CAAnimation timingFunction];
-[CAAnimation setPreferredFramesPerSecond:];
-[CAAnimation setValue:forKeyPath:];
-[CAAnimation highFrameRateReason];
-[CAAnimation _propertyFlagsForLayer:];
-[CAAnimation setDefaultDuration:];
-[CAAnimation timeOffset];
-[CAAnimation CA_copyRenderValue];
-[CAAnimation preferredFrameRateRange];
-[CAAnimation setValue:forKey:];
-[CAAnimation duration];
-[CAAnimation isEnabled];
-[CAAnimation setDelegate:];
-[CAAnimation valueForKey:];
-[CAAnimation shouldArchiveValueForKey:];
-[CAAnimation encodeWithCAMLWriter:];
-[CAAnimation setEnabled:];
-[CAAnimation CAMLTypeSupportedForKey:];
-[CAAnimation setRepeatDuration:];
-[CAAnimation encodeWithCoder:];
-[CAAnimation frameInterval];
-[CAAnimation preferredFramesPerSecond];
-[CAAnimation delegate];
-[CAAnimation valueForKeyPath:];
-[CAAnimation setValue:forUndefinedKey:];
-[CAAnimation initWithCoder:];
-[CAAnimation applyForTime:presentationObject:modelObject:];
-[CAAnimation setDuration:];
-[CAAnimation copyWithZone:];
-[CAAnimation runActionForKey:object:arguments:];
-[CAAnimation beginTime];
-[CAAnimation discretizesTime];
-[CAAnimation beginTimeMode];
-[CAAnimation isCompleteForTime:];
-[CAAnimation preferredFrameRateRangeMaximum];
-[CAAnimation preferredFrameRateRangeMinimum];
-[CAAnimation preferredFrameRateRangePreferred];
-[CAAnimation removedOnCompletion];
-[CAAnimation setBeginTimeMode:];
-[CAAnimation setDiscretizesTime:];
-[CAAnimation setPreferredFrameRateRangeMaximum:];
-[CAAnimation setPreferredFrameRateRangeMinimum:];
-[CAAnimation setPreferredFrameRateRangePreferred:];
```
