# `CMOnBodyStatus`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
i fResult;
i fConfidence;
```

## Properties

```
@property (Tq,R,N) result;
@property (Tq,R,N) confidence;
```

## Class methods

```
+[CMOnBodyStatus supportsSecureCoding];
```

## Instance methods

```
-[CMOnBodyStatus result];
-[CMOnBodyStatus encodeWithCoder:];
-[CMOnBodyStatus description];
-[CMOnBodyStatus initWithCoder:];
-[CMOnBodyStatus copyWithZone:];
-[CMOnBodyStatus confidence];
-[CMOnBodyStatus initWithOnBodyResult:confidence:timestamp:];
```
