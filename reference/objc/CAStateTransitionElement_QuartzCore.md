# `CAStateTransitionElement`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 6 properties, 21 instance methods, 2 class methods

## Instance variables

```
@"CALayer" _target;
@"CAAnimation" _animation;
@"NSString" _key;
B _enabled;
```

## Properties

```
@property (TB,GisEnabled,V_enabled) enabled;
@property (T@"CALayer",W,N,V_target) target;
@property (T@"CAAnimation",&,N,V_animation) animation;
@property (T@"NSString",C,N,V_key) key;
@property (Td,N) beginTime;
@property (Td,N) duration;
```

## Class methods

```
+[CAStateTransitionElement supportsSecureCoding];
+[CAStateTransitionElement CAMLParserStartElement:];
```

## Instance methods

```
-[CAStateTransitionElement setBeginTime:];
-[CAStateTransitionElement CAMLTypeForKey:];
-[CAStateTransitionElement debugDescription];
-[CAStateTransitionElement CAMLParser:setValue:forKey:];
-[CAStateTransitionElement init];
-[CAStateTransitionElement dealloc];
-[CAStateTransitionElement setKey:];
-[CAStateTransitionElement duration];
-[CAStateTransitionElement setAnimation:];
-[CAStateTransitionElement isEnabled];
-[CAStateTransitionElement encodeWithCAMLWriter:];
-[CAStateTransitionElement setEnabled:];
-[CAStateTransitionElement setTarget:];
-[CAStateTransitionElement encodeWithCoder:];
-[CAStateTransitionElement initWithCoder:];
-[CAStateTransitionElement setDuration:];
-[CAStateTransitionElement target];
-[CAStateTransitionElement copyWithZone:];
-[CAStateTransitionElement animation];
-[CAStateTransitionElement beginTime];
-[CAStateTransitionElement key];
```
