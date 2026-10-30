# `ULMagnetometerMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 7 properties, 1 instance methods, 2 class methods

## Properties

```
@property (Td,D,N) horizontalField;
@property (Td,D,N) verticalField;
@property (Tf,D,N) biasEstimateVarianceX;
@property (Tf,D,N) biasEstimateVarianceZ;
@property (Tf,D,N) biasEstimateVarianceY;
@property (Td,D,N) timestamp;
@property (T@"ULScanningEventMO",&,D,N) scanningEvent;
```

## Class methods

```
+[ULMagnetometerMO fetchRequest];
+[ULMagnetometerMO createFromDO:withScanningEventMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULMagnetometerMO convertToDO];
```
