# `CMLogItem`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 1 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@ _internalLogItem;
```

## Properties

```
@property (Td,R,N) continuousTimestamp;
@property (Td,R,N) timestamp;
```

## Class methods

```
+[CMLogItem supportsSecureCoding];
```

## Instance methods

```
-[CMLogItem initWithTimestamp:continuousTimestamp:];
-[CMLogItem dealloc];
-[CMLogItem timestamp];
-[CMLogItem initWithTimestamp:];
-[CMLogItem encodeWithCoder:];
-[CMLogItem initWithCoder:];
-[CMLogItem copyWithZone:];
-[CMLogItem continuousTimestamp];
```
