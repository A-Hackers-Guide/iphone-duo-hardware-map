# `CAPresentationModifier`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
^v _impl;
@ _keyPath;
@ _value;
@ _velocity;
@"CAPresentationModifierGroup" _group;
Q _value_count;
i _l;
I _f;
```

## Properties

```
@property (T@"NSString",R,C) keyPath;
@property (TB,R) additive;
@property (T@"CAPresentationModifierGroup",R) group;
@property (T@,&) value;
@property (TB,GisEnabled) enabled;
```

## Instance methods

```
-[CAPresentationModifier keyPath];
-[CAPresentationModifier initWithKeyPath:initialValue:additive:];
-[CAPresentationModifier additive];
-[CAPresentationModifier initWithKeyPath:initialValue:additive:group:];
-[CAPresentationModifier debugDescription];
-[CAPresentationModifier write];
-[CAPresentationModifier init];
-[CAPresentationModifier dealloc];
-[CAPresentationModifier group];
-[CAPresentationModifier value];
-[CAPresentationModifier CA_copyRenderValue];
-[CAPresentationModifier initWithKeyPath:initialValue:initialVelocity:additive:preferredFrameRateRangeMaximum:group:];
-[CAPresentationModifier isEnabled];
-[CAPresentationModifier setValue:velocity:];
-[CAPresentationModifier setValue:];
-[CAPresentationModifier setEnabled:];
```
