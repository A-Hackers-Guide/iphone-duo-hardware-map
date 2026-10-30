# `LLVTuningGroup`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _portType;
Q _quadraBinFactor;
@"NSDictionary" _tuningConfig;
```

## Properties

```
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSString",&,N,V_portType) portType;
@property (TQ,N,V_quadraBinFactor) quadraBinFactor;
@property (T@"NSDictionary",&,N,V_tuningConfig) tuningConfig;
```

## Class methods

```
+[LLVTuningGroup convertLUTArraysInDictionary:];
```

## Instance methods

```
-[LLVTuningGroup portType];
-[LLVTuningGroup setPortType:];
-[LLVTuningGroup setName:];
-[LLVTuningGroup name];
-[LLVTuningGroup setQuadraBinFactor:];
-[LLVTuningGroup quadraBinFactor];
-[LLVTuningGroup floatForTuningKey:];
-[LLVTuningGroup initWithPortType:quadraBinFactor:name:dictionary:];
-[LLVTuningGroup intForTuningKey:];
-[LLVTuningGroup interpolateLUT:input:];
-[LLVTuningGroup interpolatedFloatForTuningKey:input:];
-[LLVTuningGroup setTuningConfig:];
-[LLVTuningGroup tuningConfig];
-[LLVTuningGroup valueForTuningKey:];
```
