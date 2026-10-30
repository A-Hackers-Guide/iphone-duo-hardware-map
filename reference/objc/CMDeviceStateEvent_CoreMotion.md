# `CMDeviceStateEvent`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 6 instance variables, 10 properties, 21 instance methods, 10 class methods

## Instance variables

```
q fPropertyA;
q fPropertyA0;
q fPropertyA1;
q fPropertyB;
q fPropertyC;
q fPropertyD;
```

## Properties

```
@property (Tq,R,N) propertyA;
@property (Tq,R,N) propertyA0;
@property (Tq,R,N) propertyA1;
@property (Tq,R,N) propertyB;
@property (Tq,R,N) propertyC;
@property (Tq,R,N) propertyD;
@property (TB,R,N) progressValid;
@property (Tq,R,N) fromPropertyB;
@property (Tq,R,N) toPropertyB;
@property (Td,R,N) progressValue;
```

## Class methods

```
+[CMDeviceStateEvent isValidPropertyA:];
+[CMDeviceStateEvent isValidPropertyB:];
+[CMDeviceStateEvent isValidPropertyBAngle:];
+[CMDeviceStateEvent isValidPropertyC:];
+[CMDeviceStateEvent isValidPropertyD:];
+[CMDeviceStateEvent propertyAForConfigType:propertyA:propertyB:propertyC:];
+[CMDeviceStateEvent stringForDeviceStatePropertyAType:];
+[CMDeviceStateEvent stringForDeviceStatePropertyBType:];
+[CMDeviceStateEvent stringForDeviceStatePropertyCType:];
+[CMDeviceStateEvent stringForDeviceStatePropertyDType:];
```

## Instance methods

```
-[CMDeviceStateEvent dealloc];
-[CMDeviceStateEvent encodeWithCoder:];
-[CMDeviceStateEvent hash];
-[CMDeviceStateEvent description];
-[CMDeviceStateEvent initWithCoder:];
-[CMDeviceStateEvent copyWithZone:];
-[CMDeviceStateEvent isEqual:];
-[CMDeviceStateEvent progressValue];
-[CMDeviceStateEvent fromPropertyB];
-[CMDeviceStateEvent initWithDeviceStatePropertyAType:deviceStatePropertyA0Type:deviceStatePropertyA1Type:deviceStatePropertyBType:deviceStatePropertyCType:deviceStatePropertyDType:timestamp:continuousTimestamp:];
-[CMDeviceStateEvent initWithDeviceStatePropertyAType:deviceStatePropertyBType:deviceStatePropertyCType:deviceStatePropertyDType:timestamp:continuousTimestamp:];
-[CMDeviceStateEvent initWithDeviceStatePropertyAType:deviceStatePropertyBType:deviceStatePropertyCType:isProgressValid:propertyBFrom:propertyBTo:progressValue:timestamp:continuousTimestamp:];
-[CMDeviceStateEvent initWithDeviceStatePropertyAType:deviceStatePropertyBType:deviceStatePropertyCType:timestamp:continuousTimestamp:];
-[CMDeviceStateEvent progressValid];
-[CMDeviceStateEvent propertyA];
-[CMDeviceStateEvent propertyA0];
-[CMDeviceStateEvent propertyA1];
-[CMDeviceStateEvent propertyB];
-[CMDeviceStateEvent propertyC];
-[CMDeviceStateEvent propertyD];
-[CMDeviceStateEvent toPropertyB];
```
