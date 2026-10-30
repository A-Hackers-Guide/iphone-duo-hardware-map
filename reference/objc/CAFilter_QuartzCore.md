# `CAFilter`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 25 instance methods, 6 class methods

## Instance variables

```
I _type;
@"NSString" _name;
I _flags;
^v _attr;
^v _cache;
```

## Properties

```
@property (T@"NSString",R) type;
@property (T@"NSString",C) name;
@property (TB,GisEnabled) enabled;
@property (TB) cachesInputImage;
@property (TB,GisAccessibility) accessibility;
```

## Class methods

```
+[CAFilter supportsSecureCoding];
+[CAFilter automaticallyNotifiesObserversForKey:];
+[CAFilter CAMLParserStartElement:];
+[CAFilter filterWithType:];
+[CAFilter filterWithName:];
+[CAFilter filterTypes];
```

## Instance methods

```
-[CAFilter CAMLTypeForKey:];
-[CAFilter mutableCopyWithZone:];
-[CAFilter setDefaults];
-[CAFilter enabled];
-[CAFilter CAMLParser:setValue:forKey:];
-[CAFilter initWithType:];
-[CAFilter dealloc];
-[CAFilter setCachesInputImage:];
-[CAFilter CA_copyRenderValue];
-[CAFilter setValue:forKey:];
-[CAFilter isEnabled];
-[CAFilter valueForKey:];
-[CAFilter encodeWithCAMLWriter:];
-[CAFilter type];
-[CAFilter cachesInputImage];
-[CAFilter setEnabled:];
-[CAFilter encodeWithCoder:];
-[CAFilter description];
-[CAFilter setName:];
-[CAFilter initWithCoder:];
-[CAFilter copyWithZone:];
-[CAFilter isAccessibility];
-[CAFilter setAccessibility:];
-[CAFilter name];
-[CAFilter initWithName:];
```
