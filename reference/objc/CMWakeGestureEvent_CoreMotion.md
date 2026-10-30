# `CMWakeGestureEvent`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 5 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
i _orientation;
q _state;
q _type;
q _config;
q _propertyC;
```

## Properties

```
@property (Tq,R,N,V_state) state;
@property (Tq,R,N,V_type) type;
@property (Tq,R,N,V_config) config;
@property (Tq,R,N,V_propertyC) propertyC;
@property (Ti,R,N,V_orientation) orientation;
```

## Class methods

```
+[CMWakeGestureEvent supportsSecureCoding];
```

## Instance methods

```
-[CMWakeGestureEvent config];
-[CMWakeGestureEvent orientation];
-[CMWakeGestureEvent type];
-[CMWakeGestureEvent encodeWithCoder:];
-[CMWakeGestureEvent description];
-[CMWakeGestureEvent initWithCoder:];
-[CMWakeGestureEvent copyWithZone:];
-[CMWakeGestureEvent state];
-[CMWakeGestureEvent initWithState:type:config:propertyC:orientation:timestamp:];
-[CMWakeGestureEvent initWithState:type:orientation:timestamp:];
-[CMWakeGestureEvent propertyC];
```
