# `CMFlipEvent`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 2 instance variables, 2 properties, 8 instance methods, 2 class methods

## Instance variables

```
q fFlipState;
q fFlipReason;
```

## Properties

```
@property (Tq,R,N) flipState;
@property (Tq,R,N) flipReason;
```

## Class methods

```
+[CMFlipEvent stringForFlipReasonType:];
+[CMFlipEvent stringForFlipStateType:];
```

## Instance methods

```
-[CMFlipEvent dealloc];
-[CMFlipEvent encodeWithCoder:];
-[CMFlipEvent description];
-[CMFlipEvent initWithCoder:];
-[CMFlipEvent copyWithZone:];
-[CMFlipEvent flipReason];
-[CMFlipEvent flipState];
-[CMFlipEvent initWithFlipStateType:flipReasonType:timestamp:continuousTimestamp:];
```
