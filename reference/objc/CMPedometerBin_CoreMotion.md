# `CMPedometerBin`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 7 properties, 13 instance methods, 1 class methods

## Instance variables

```
d _valueOut;
d _begin;
d _end;
q _state;
```

## Properties

```
@property (Td,R,N,V_valueOut) valueOut;
@property (Td,R,N,V_begin) begin;
@property (Td,R,N) lowerQuartile;
@property (Td,R,N) center;
@property (Td,R,N) upperQuartile;
@property (Td,R,N,V_end) end;
@property (Tq,R,N,V_state) state;
```

## Class methods

```
+[CMPedometerBin supportsSecureCoding];
```

## Instance methods

```
-[CMPedometerBin begin];
-[CMPedometerBin dealloc];
-[CMPedometerBin end];
-[CMPedometerBin center];
-[CMPedometerBin encodeWithCoder:];
-[CMPedometerBin description];
-[CMPedometerBin initWithCoder:];
-[CMPedometerBin isEqual:];
-[CMPedometerBin state];
-[CMPedometerBin initWithValueOut:begin:end:state:];
-[CMPedometerBin lowerQuartile];
-[CMPedometerBin upperQuartile];
-[CMPedometerBin valueOut];
```
