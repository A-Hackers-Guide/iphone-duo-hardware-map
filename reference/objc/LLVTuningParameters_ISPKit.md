# `LLVTuningParameters`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logger;
@"NSDictionary" _tuningConfig;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_tuningConfig) tuningConfig;
```

## Class methods

```
+[LLVTuningParameters sharedInstance];
+[LLVTuningParameters modelNameForPortType:quadraBinFactor:resolution:];
```

## Instance methods

```
-[LLVTuningParameters init];
-[LLVTuningParameters enumerateGroupsWithName:enumerator:];
-[LLVTuningParameters groupForPortType:quadraBinFactor:name:];
-[LLVTuningParameters loadTuningParameters:];
-[LLVTuningParameters setTuningConfig:];
-[LLVTuningParameters tuningConfig];
```
