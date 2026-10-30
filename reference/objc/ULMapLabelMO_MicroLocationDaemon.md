# `ULMapLabelMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 12 properties, 1 instance methods, 2 class methods

## Properties

```
@property (Td,D,N) timestamp;
@property (T@"NSNumber",&,D,N) x;
@property (T@"NSNumber",&,D,N) y;
@property (T@"NSNumber",&,D,N) z;
@property (T@"NSNumber",&,D,N) rotationX;
@property (T@"NSNumber",&,D,N) rotationY;
@property (T@"NSNumber",&,D,N) rotationZ;
@property (T@"NSNumber",&,D,N) rotationW;
@property (T@"NSData",&,D,N) probabilityVector;
@property (T@"NSData",&,D,N) imageIdentifiersVector;
@property (T@"ULModelMO",&,D,N) model;
@property (T@"ULLabelMO",&,D,N) label;
```

## Class methods

```
+[ULMapLabelMO fetchRequest];
+[ULMapLabelMO createFromDO:withLabelMO:modelMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULMapLabelMO convertToDO];
```
