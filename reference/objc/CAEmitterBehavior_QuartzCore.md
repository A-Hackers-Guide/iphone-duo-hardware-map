# `CAEmitterBehavior`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 3 properties, 20 instance methods, 5 class methods

## Instance variables

```
I _type;
@"NSString" _name;
^v _attr;
^v _cache;
I _flags;
```

## Properties

```
@property (T@"NSString",R) type;
@property (T@"NSString",C) name;
@property (TB,GisEnabled) enabled;
```

## Class methods

```
+[CAEmitterBehavior supportsSecureCoding];
+[CAEmitterBehavior automaticallyNotifiesObserversForKey:];
+[CAEmitterBehavior CAMLParserStartElement:];
+[CAEmitterBehavior behaviorTypes];
+[CAEmitterBehavior behaviorWithType:];
```

## Instance methods

```
-[CAEmitterBehavior didChangeValueForKey:];
-[CAEmitterBehavior CAMLTypeForKey:];
-[CAEmitterBehavior mutableCopyWithZone:];
-[CAEmitterBehavior CAMLParser:setValue:forKey:];
-[CAEmitterBehavior initWithType:];
-[CAEmitterBehavior dealloc];
-[CAEmitterBehavior setValue:forKeyPath:];
-[CAEmitterBehavior CA_copyRenderValue];
-[CAEmitterBehavior setValue:forKey:];
-[CAEmitterBehavior isEnabled];
-[CAEmitterBehavior valueForKey:];
-[CAEmitterBehavior encodeWithCAMLWriter:];
-[CAEmitterBehavior type];
-[CAEmitterBehavior setEnabled:];
-[CAEmitterBehavior encodeWithCoder:];
-[CAEmitterBehavior valueForKeyPath:];
-[CAEmitterBehavior setName:];
-[CAEmitterBehavior initWithCoder:];
-[CAEmitterBehavior copyWithZone:];
-[CAEmitterBehavior name];
```
