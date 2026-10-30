# `CAState`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 8 instance variables, 8 properties, 28 instance methods, 2 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _basedOn;
@"NSMutableArray" _elements;
d _nextDelay;
d _previousDelay;
B _enabled;
B _locked;
B _initial;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSString",C,V_basedOn) basedOn;
@property (TB,GisEnabled,V_enabled) enabled;
@property (T@"NSArray",C,N) elements;
@property (Td,V_nextDelay) nextDelay;
@property (Td,V_previousDelay) previousDelay;
@property (TB,N,GisLocked,V_locked) locked;
@property (TB,GisInitial,V_initial) initial;
```

## Class methods

```
+[CAState supportsSecureCoding];
+[CAState CAMLParserStartElement:];
```

## Instance methods

```
-[CAState removeElement:];
-[CAState setElements:];
-[CAState CAMLTypeForKey:];
-[CAState isLocked];
-[CAState addElement:];
-[CAState debugDescription];
-[CAState setLocked:];
-[CAState elements];
-[CAState CAMLParser:setValue:forKey:];
-[CAState isInitial];
-[CAState init];
-[CAState dealloc];
-[CAState setBasedOn:];
-[CAState isEnabled];
-[CAState encodeWithCAMLWriter:];
-[CAState setEnabled:];
-[CAState encodeWithCoder:];
-[CAState setName:];
-[CAState initWithCoder:];
-[CAState setInitial:];
-[CAState basedOn];
-[CAState previousDelay];
-[CAState foreachLayer:];
-[CAState copyWithZone:];
-[CAState setPreviousDelay:];
-[CAState setNextDelay:];
-[CAState name];
-[CAState nextDelay];
```
